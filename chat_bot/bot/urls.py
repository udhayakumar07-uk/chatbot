from django.urls import path
from . import views

urlpatterns = [
    path("auth/", views.chatbot, name="chatbot"),
    path("", views.auth_view, name="auth"),
    # path("google-login/", views.google_login_view, name="google_login"),
]
