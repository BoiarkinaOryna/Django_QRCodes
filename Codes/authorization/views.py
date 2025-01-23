from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def render_authorization(request):
    fail = False
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(
            request = request,
            email = email,
            password = password
        )
        if user:
            login(request = request, user = user)
            return redirect("main")
        else:
            fail = True
    return render(
        request=request,
        template_name='authorization.html',
        context = {
            'fail': fail,
            'authenticated': request.user.is_authenticated
            }
    )
    
def render_logout(request):
    logout(request = request)
    return redirect('authorization')