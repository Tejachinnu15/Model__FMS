from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    TMFO=TopicModelForm()
    d={'TMFO':TMFO}
    if request.method=='POST':
        TMFOD=TopicModelForm(request.POST)
        if TMFOD.is_valid():
            TMFOD.save()
        return HttpResponse('data is inserted')

    return render(request,'insert_topic.html',d)
def  insert_webpage(request):
    WPMFO=WebpageModelForm()
    d={'WPMFO':WPMFO}
    if request.method=='POST':
        WPMFDO=WebpageModelForm(request.POST)
        if WPMFDO.is_valid():
            WPMFDO.save()
        return HttpResponse('data is inserted')
    return render(request,'insert_webpage.html',d)
def insert_access(request):
    AMFO=RecordModelForm()
    d={'AMFO':AMFO}
    if request.method=='POST':
        AMFD=RecordModelForm(request.POST)
        if AMFD.is_valid():
            AMFD.save()
        return HttpResponse('Data inserted')
    return render(request,'insert_access.html',d)