from django.urls import path, include
# from . import views

from.views import Manage_Event 
urlpatterns = [
    # path('blog/', views.blog, name = "Blog"),
    path('', Manage_Event.as_view(), name = "Events"),

]