from django.shortcuts import render


def merch(request):
    return render(request, "merchandise/merch.html")
