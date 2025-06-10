from django.shortcuts import render,redirect
from django.conf import settings
import qrcode
import os
# Create your views here.
def home(request):
  if request.method == 'POST':
    title = request.POST.get('title')
    url = request.POST.get('url')
    qr = qrcode.make(url)
    file_name = title.replace(" ","_").lower()+'.png'
    file_path = os.path.join(settings.MEDIA_ROOT,file_name)
    qr.save(file_path)
    #qr img url
    qr_url = os.path.join(settings.MEDIA_URL, file_name)
    
    context = {
      'title':title,
      'qr_url': qr_url,
      'file_name': file_name,
    }
    return render(request,"qr_img.html", context)
  else:
    return render(request,"home.html")