from django.urls import path
from feedback import views

urlpatterns = [
    path('feedback/', views.feedback, name='feedback'),
    path('feedback_list/', views.Feedback_list),
    
]





