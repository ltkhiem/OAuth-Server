from django.urls import path
from . import views

urlpatterns = [
    path("oauth", views.oauth, name='oauth'),
    path("generate-authorization-url", views.gen_auth_url, name='gen-auth-url'),
    path("get-authentication-tokens", views.get_auth_tokens, name='get-auth-token'),
    path("reading", views.update_reading, name='update-reading')
]