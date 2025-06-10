# Create this file: QR_Generator/middleware.py

import os
from django.http import HttpResponse, Http404
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from mimetypes import guess_type

class MediaFilesMiddleware(MiddlewareMixin):
    """
    Middleware to serve media files in production when not using Nginx/Apache
    """
    def process_request(self, request):
        if not settings.DEBUG and request.path.startswith(settings.MEDIA_URL):
            # Remove the MEDIA_URL prefix to get the relative path
            relative_path = request.path[len(settings.MEDIA_URL):]
            file_path = os.path.join(settings.MEDIA_ROOT, relative_path)
            
            if os.path.exists(file_path) and os.path.isfile(file_path):
                # Guess the content type based on file extension
                content_type, _ = guess_type(file_path)
                if content_type is None:
                    content_type = 'application/octet-stream'
                
                try:
                    with open(file_path, 'rb') as f:
                        response = HttpResponse(f.read(), content_type=content_type)
                        return response
                except IOError:
                    raise Http404("File not found")
            else:
                raise Http404("File not found")
        
        return None