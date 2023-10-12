from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .import views

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('success/', views.CheckoutSuccessView, name = 'success'),
    path('Failed/', views.CheckoutFailedView, name = 'Failed'),
    path('donation_report/', views.donation_report, name='donation_report'),

]