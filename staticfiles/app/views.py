from app.serializer import URLSerializers
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.fields import URLField
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
import joblib
from rest_framework.parsers import JSONParser
import json
from sklearn import preprocessing
from .models import URL
from .forms import urlForm
import pandas as pd
from .features2 import extract
from django.contrib import messages


# Create your views here.
class urlView(viewsets.ModelViewSet):
    queryset=URL.objects.all()
    serializer_class=URLSerializers

def result(unit):
    try: 
        mdl=joblib.load("my_random_forest.joblib")
        sample=extract(unit)
        y_pred=mdl.predict(sample)
        
        if y_pred==1:
           ans="PHISHING"
        elif y_pred==0:
            ans="LEGITMATE"
        return ans
        
    except ValueError as e:
        return (e.args[0])


def enter(request):
    if request.method=='POST':
        form=urlForm(request.POST)
        if form.is_valid():
            url=form.cleaned_data['url']
            answer=result(url)
            print(answer)
            messages.success(request,"'{}'   is a {} site.".format(url,answer))
            
    form= urlForm()
    return render(request,'checkurl.html', {'form':form})


def home(request):
    return render(request,'homepage.html', {})

def login(request):
    return render(request,'signin.html',{})