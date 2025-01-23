from django.shortcuts import render

# Create your views here.

def render_my_codes_page(request):
    return render(
        request = request,
        template_name = "my_codes.html",
        context = {
            'authenticated': request.user.is_authenticated
        }
    )