from django.urls import path
from . import views

app_name = 'sales'

urlpatterns = [
    path('',views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('contact/', views.contact, name='contact'),
    #path('view/<id>/', views.viewItem, name='view-item'),
   # path('blog/', views.blog, name='blog'),
    path('shop/', views.shop, name='shop'),
    path('checkout/', views.checkout, name='checkout'),
    path('cart/', views.cart, name='cart'),
    #path('services/', views.services, name='services'),
    #path('thankyou/', views.thankyou, name='thankyou'),
]
