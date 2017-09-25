# coding: utf-8
from django.shortcuts import render

# Create your views here.

def home(request):
        TutorialList = ['HTML', 'CSS','JQuery','Python','Django']
        return render(request,'home.html',{'TutorialList':TutorialList})
