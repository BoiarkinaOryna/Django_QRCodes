from django.shortcuts import render
from create_code.models import Code
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest

# Create your views here.

@login_required
def render_my_codes_page(request: HttpRequest):
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