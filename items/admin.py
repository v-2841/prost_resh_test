from django.contrib import admin
from django.contrib.auth.models import Group

from items.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'price',
    )


admin.site.site_title = 'django_stripe'
admin.site.site_header = 'django_stripe'
admin.site.index_title = 'Администрирование сайта'
admin.site.unregister(Group)
