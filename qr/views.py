from django.shortcuts import render
import qrcode
import io
import base64

def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        url = request.POST.get('url')

        # Generate QR code
        qr = qrcode.make(url)

        # Save to memory
        buffer = io.BytesIO()
        qr.save(buffer, format='PNG')
        buffer.seek(0)

        # Convert to base64
        img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

        # Construct data URI
        qr_url = f"data:image/png;base64,{img_base64}"

        # Generate filename (for download)
        file_name = title.replace(" ", "_").lower() + '.png'

        context = {
            'title': title,
            'qr_url': qr_url,
            'file_name': file_name,
        }
        return render(request, "qr_img.html", context)

    return render(request, "home.html")
