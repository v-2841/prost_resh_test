from django.conf import settings
from django.shortcuts import render

from items.models import Item


def index(request):
    items = Item.objects.all()
    return render(request, 'items/index.html', {'items': items})


def item(request, id):
    item = Item.objects.get(id=id)
    context = {
        'item': item,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    }
    return render(request, 'items/item.html', context)
