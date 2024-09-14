from django.http import HttpResponse
from django.shortcuts import render


def secret_santa(request):
    return render(request, "santa.html")
