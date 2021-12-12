from django.shortcuts import render

from .models import *
# Create your views here.


def homepage(request):
    template_name = "admin/homepage.html"

    return render(request, template_name)


def user_accounts_list(request):
    """
        Managing user accounts list
    """
    template_name = "authentication/user_accounts.html"
    user = User.objects.all()
    context = {
        "user": user
    }
    return render(request, template_name, context)
