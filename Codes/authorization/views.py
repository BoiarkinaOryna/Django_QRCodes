from django.shortcuts import render

def render_authorization(request):
    return render(
        request=request,
        template_name='authorization.html'
    )
    
    
