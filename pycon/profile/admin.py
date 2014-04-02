from django.contrib import admin

from .models import Profile


admin.site.register(
    Profile,
    exclude=['phone'],
    list_display=[
        'user',
        'first_name',
        'first_name_ja',
        'last_name',
        'last_name_ja',
    ],
)
