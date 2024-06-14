from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from u4ebka import settings
from vpirivau.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vpirivau.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)