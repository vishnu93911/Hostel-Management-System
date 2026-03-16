from django.urls import path
from .views import login_page,register,register_page

urlpatterns = [
    path("", login_page, name="login_page"),   
    path("register/", register_page, name="register"),
    path("api/register/", register, name="register_api"),
]






