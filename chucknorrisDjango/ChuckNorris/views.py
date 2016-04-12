from django.shortcuts import render
from django.http import HttpResponse

import redis, json, urllib, urllib2
# Create your views here.
def index(request):
    return render(request,'ChuckNorris/index.html')
