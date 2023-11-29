from django.urls import path

from api import views


app_name = 'api'
urlpatterns = [
    path('buy/<int:id>/', views.BuyItemView.as_view(), name='buy'),
]
