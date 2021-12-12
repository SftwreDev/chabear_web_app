from django.urls import path, include

from .views import *

app_name = "auth"

urlpatterns = [
    path("app/v1/accounts/", include('django.contrib.auth.urls')),
    path("", homepage, name="homepage"),
    path("app/v1/accounts/manage-user-accounts/",
         user_accounts_list, name="user_accounts_list"),
]
