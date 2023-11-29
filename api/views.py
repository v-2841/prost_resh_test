import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from dotenv import load_dotenv

from items.models import Item


load_dotenv()
stripe.api_key = settings.STRIPE_SECRET_KEY


class BuyItemView(View):
    def get(self, request, id):
        item = get_object_or_404(Item, id=id)
        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': item.name,
                            'description': item.description,
                        },
                        'unit_amount': int(item.price * 100),
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=request.build_absolute_uri('/success/'),
                cancel_url=request.build_absolute_uri('/cancel/'),
            )
            return JsonResponse({'session_id': checkout_session.id})
        except stripe.error.StripeError as e:
            return JsonResponse({'error': str(e)}, status=400)
