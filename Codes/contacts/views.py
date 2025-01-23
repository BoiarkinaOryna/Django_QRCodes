from django.shortcuts import render

def render_contacts(request):
    return render(
        request = request,
        template_name = "contacts.html",
        context = {
            'authenticated': request.user.is_authenticated
        }
        )

# Create your views here.
