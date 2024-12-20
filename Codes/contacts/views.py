from django.shortcuts import render

def render_contacts(request):
    return render(
        request = request,
        template_name = "contacts.html"
        )

# Create your views here.
