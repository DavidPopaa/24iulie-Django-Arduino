from django.shortcuts import redirect, render
from .models import SerialModel
from .serialReader import dist


def post_data(request):
    if request.method == "POST":
        data = SerialModel(distance1=dist[0], distance2=dist[1], distance3=dist[2], distance4=dist[3])
        data.save()
        return redirect("serialread:redirect") 
    else:
        return render(request, "serialread/post.html")


def redirect_func(request):
    return render(request, "serialread/redirect.html")