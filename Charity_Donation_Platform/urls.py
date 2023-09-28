
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
<<<<<<< HEAD
=======
    path('', include('blog.urls')),
    # path('', include('events.urls')),

    ,
<<<<<<< HEAD
>>>>>>> 0e5bc350d89c41a8125aff51bbce11fdf6d3b03f
    path('feedback/', include('feedback.urls')),
    path('', include('user_app.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
