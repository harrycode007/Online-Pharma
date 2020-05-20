from django.urls import path
from .import views

# All the functions which are created in views.py are assigned URLs here and called in the same way.

urlpatterns = [
     path('', views.index, name='index'), # Empty argument in the first index defaults to Homepage in the application.
     path('signup/',views.signup, name='signup'),
     path('login/',views.login, name='login'),
     path('contactus/', views.contactus, name='contactus'),
     path('store/', views.store, name='store'),
     path('contactuslogin/', views.contactuslogin, name='contactuslogin'),
     path('cart/',views.cart, name='cart'),
     path('orderplace/',views.orderplace,name="orderplace")
]