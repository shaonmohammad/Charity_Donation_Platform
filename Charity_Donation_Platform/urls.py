
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
<<<<<<< HEAD
    path('feedback/', include('feedback.urls')),
=======
    path('',include('user_app.urls')),
>>>>>>> 7d9f9d238f9bd949a39f670d56618e9f916ea350
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
