from datetime import datetime, timedelta

import stripe

from users.models import User


def create_good(name, description, unit_amount):
    """
    Функция для создания товара
    """
    stripe.api_key = "sk_test_51OQ4orKl6ydiyHB88UxS6MYFffcyg8jkgdJGFUGuVbAiu82WOvLbnAywGA1UjdwXhuRhs5i76yb5fKGVPSwOa4cW00Utc8t2kT"

    starter_subscription = stripe.Product.create(
        name=name,
        description=description,
    )

    starter_subscription_price = stripe.Price.create(
        unit_amount=unit_amount,
        currency="usd",
        product=starter_subscription['id'],
    )

    # Save these identifiers
    #print(f"Success! Here is your starter subscription product id: {starter_subscription.id}")
    #print(f"Success! Here is your starter subscription price id: {starter_subscription_price.id}")
    return starter_subscription_price.id


def get_payment(price):
    stripe.api_key = "sk_test_51OQ4orKl6ydiyHB88UxS6MYFffcyg8jkgdJGFUGuVbAiu82WOvLbnAywGA1UjdwXhuRhs5i76yb5fKGVPSwOa4cW00Utc8t2kT"
    stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[{"price": price, "quantity": 1}],
        mode="payment",
    )
    #print(stripe.checkout.Session.list(limit=1).data[0].url)
    return stripe.checkout.Session.list(limit=1).data[0].url

def check_user_last_login():
    print("sadasdsa")
    for user in User.objects.all():
        if user.last_login <= datetime.now() - timedelta(month=4):
            user.is_active = False
            user.save()
        print(user)
        print(user.last_login)
