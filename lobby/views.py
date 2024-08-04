from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def main(req):
    f = open('./html/index.html').readlines()
    return HttpResponse(f, content_type='text/html')
