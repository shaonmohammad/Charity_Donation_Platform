from django.urls import path
from feedback import views

urlpatterns = [
    # path('', views.feedback_form, name='feedback_form'),
    # path('', views.feedback_show),
    path('feedback_write/',views.feedback_write, name='feedback_write'),
    # path('', views.feedback_show, name='show_feedback'),
    
    # path('feedback_data/', views.feedback_data, name='feedback_data'),
    path('feedback_list/', views.Feedback_list.as_view()),
    path('create_list/', views.Create.as_view()),
    path('delete_item/<int:pk>/', views.Delete_item.as_view()),
    path('update_item/<int:pk>/', views.UpdateItem.as_view()),
    
    
    # path('blog_details/')
    # Blog-Detail
    
]




