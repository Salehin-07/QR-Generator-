"""
URL configuration for QR_Generator project - Django serving media files
"""
from django.contrib import admin
from django.urls import path
from qr import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
]

# Serve media and static files through Django (even in production)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Alternative: You can also be more explicit
# if True:  # Always serve media files through Django
#     from django.views.static import serve
#     from django.urls import re_path
#     
#     urlpatterns += [
#         re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
#         re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
#     ]