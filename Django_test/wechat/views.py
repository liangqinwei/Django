# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    #return HttpResponse(U'欢迎光临，这里是37手游')

    return render(request,'preload.html')