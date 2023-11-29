from django.urls import path

from items import views


app_name = 'items'
urlpatterns = [
    path('', views.index, name='index'),
    path('item/<int:id>/', views.item, name='item'),
]
