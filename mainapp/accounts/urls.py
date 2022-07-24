from django.urls import path
from .views import signup, redirectt, signin

app_name = "accounts"
urlpatterns = [
    path("signup/", signup, name="signup"),
    path("redirect/", redirectt, name="redirect"),
    path("signin/", signin, name="signin")
]
