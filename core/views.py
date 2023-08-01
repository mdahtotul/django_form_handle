from django.shortcuts import render


def init_home(request):
    return render(request, "home.html")
