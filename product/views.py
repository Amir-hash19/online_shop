from django.shortcuts import render
from django.http import HttpResponse


def show_products_page(request):
    return HttpResponse("this is products page")
