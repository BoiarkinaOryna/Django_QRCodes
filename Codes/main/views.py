from django.shortcuts import render
from Codes import settings

def render_main(request):
    return render(
        request = request,
        template_name = "main.html",
        context = {
            'authenticated': request.user.is_authenticated,
            'MEDIA_URL': settings.MEDIA_URL,
        }
    )
# Create your views here.
