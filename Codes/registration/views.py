from django.shortcuts import render

def render_registretion(request):
    return render(
        request=request,
        template_name='registration.html'
    )
