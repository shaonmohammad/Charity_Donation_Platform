from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('get/', views.DetailsUser.as_view()),
    #path('login/',views.UserLoginView.as_view()),
    path('logout/', views.UserLogout.as_view()),
    path('user_register/', views.UserRegister.as_view()),
    path('success/', views.CheckoutSuccessView, name = 'success'),
    path('Failed/', views.CheckoutFailedView, name = 'Failed'),
    path('signup/', views.signup, name = 'signup'),
    path('user_login/', views.user_login, name = 'login'),
    path('user_logout/',views.user_logout, name = 'logout'),
]