from django.shortcuts import render
from create_code.models import Code

# Create your views here.

def render_my_codes_page(request):
    codes = Code.objects.filter(creator = request.user)
    return render(
        request = request,
        template_name = "my_codes.html",
        context = {
            'authenticated': request.user.is_authenticated,
            "user": request.user,
            "codes": codes
        }
    )