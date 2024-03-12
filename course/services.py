import stripe


def get_link(name, amount):
    stripe.api_key = 'sk_test_51OtQdzRvD4zY7qa1MO62ehkSRlOnP31GpiF5IgZR62B9LR1PzzfX2zlyFgUOGzPpeYT9DNHqtZzZ6Tl90PjZd8GX00N7kx1Re4'
    product = stripe.Product.create(
        name=name
    )
    payment_amount = stripe.Price.create(
        currency="rub",
        unit_amount=amount*100,
        product_data={"name": product["name"]},
    )
    session = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[{"price": payment_amount['id'], "quantity": 1}],
        mode="payment",
    )
    return product["name"], session["url"], session["id"]

