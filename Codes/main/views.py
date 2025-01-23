from django.shortcuts import render

def render_main(request):
    return render(
        request = request,
        template_name = "main.html",
        context = {
            # 'authenticated': True
            'authenticated': request.user.is_authenticated
        }
    )
# Create your views here.
