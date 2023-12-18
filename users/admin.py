from django.contrib import admin

from users.models import User, Payments, UserSubscriptions

admin.site.register(User)

admin.site.register(UserSubscriptions)

admin.site.register(Payments)
