from django.shortcuts import render

# Create your views here.
def render_create_code(request):
    return render(
        request = request,
        template_name = "create_code.html",
        context = {
            'authenticated': request.user.is_authenticated
        }
    )