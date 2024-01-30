from django.shortcuts import render
from django.http import HttpResponse

def index(req):
    return HttpResponse("<h1> INDEX PAGE </h1>")
def contact(req):
    return HttpResponse("<h1> Contact PAGE </h1>")