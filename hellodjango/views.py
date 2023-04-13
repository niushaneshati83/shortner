from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def hello(req_uest):
    return HttpResponse("helllo world!")
