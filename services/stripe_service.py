import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_product(name):
    return stripe.Product.create(name=name)

def create_price(product_id, amount):
    return stripe.Price.create(
        product=product_id,
        unit_amount=amount * 100,
        currency='rub',
    )

def create_checkout_session(price_id):
    return stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': price_id,
            'quantity': 1,
        }],
        mode='payment',
        success_url='https://example.com/success',
        cancel_url='https://example.com/cancel',
    )
