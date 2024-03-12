from rest_framework import viewsets, generics, permissions, serializers
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from course.models import Course, Lesson, Subscription, CoursePayment
from course.paginators import CoursePaginator, LessonPaginator
from course.permissions import IsOwner
from course.serializers import CourseSerializer, LessonSerializer, SubscriptionSerializer, CoursePaymentSerializer
from course.services import get_link


class CourseViewSet(viewsets.ModelViewSet):
    """ Viewset for courses """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CoursePaginator

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.IsAdminUser]
        elif self.action == 'destroy':
            permission_classes = [permissions.IsAdminUser]

        else:
            permission_classes = [permissions.AllowAny]

        return [permission() for permission in permission_classes]


class LessonCreateAPIView(generics.CreateAPIView):
    """ Create lesson """
    serializer_class = LessonSerializer
    permission_classes = [AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class LessonListAPIView(generics.ListAPIView):
    """ All lesson """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [permissions.AllowAny]
    pagination_class = LessonPaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [permissions.AllowAny]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """ Update lesson """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """ Delete lesson """
    queryset = Lesson.objects.all()
    permission_classes = [permissions.IsAdminUser]


class SubscribeAPIView(APIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get('course_id')
        course_item = get_object_or_404(Course, pk=course_id)
        subs_item = Subscription.objects.filter(user=user, course=course_item)

        if subs_item.exists():
            subs_item.delete()
            message = 'Subscription delete'
        else:
            Subscription.objects.create(user=user, course=course_item)
            message = 'Subscription create'

        return Response({"message": message})


class CoursePaymentCreateAPIView(generics.CreateAPIView):
    queryset = CoursePayment.objects.all()
    serializer_class = CoursePaymentSerializer

    def perform_create(self, serializer):
        new_payment_amount = serializer.save()
        # product_name = get_product(new_payment_amount.name)
        # new_payment_amount.name = product_name
        product_name, payment_link, session_id = get_link(new_payment_amount.name, new_payment_amount.payment_amount)
        new_payment_amount.name = product_name
        new_payment_amount.payment_link = payment_link
        new_payment_amount.payment_id = session_id
        new_payment_amount.save()

