"""
URL configuration for Codes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authorization import render_authorization
from registration import render_registretion
# from main import render_main
# from create_code import render_code
# from my_codes import render_codes
# from contacts import render_contacts

urlpatterns = [
    # path('', admin.site.urls),
    path('log/', render_authorization, name='authorization'),
    path('reg/', render_registretion, name='registration'),
    # path('', render_main, name='main'),
    # path('', render_code, name='create_code'),
    # path('', render_codes, name='my_codes'),
    # path('', render_contacts, name='contacts')
]
