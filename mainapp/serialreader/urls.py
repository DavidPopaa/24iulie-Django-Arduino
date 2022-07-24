from django.urls import path
from .views import post_data, redirect_func


app_name = "serialread"
urlpatterns = [
    path("postdata/", post_data, name="postdata"),
    path("redirect/", redirect_func, name="redirect")
]
