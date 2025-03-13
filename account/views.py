from django.shortcuts import render
from django.http import HttpResponse


def show_landing(request):
    return HttpResponse("this is landing page")

