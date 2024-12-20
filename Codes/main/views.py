from django.shortcuts import render

def render_main(request):
    return render(
        request = request,
        template_name = "main.html"
    )
# Create your views here.
