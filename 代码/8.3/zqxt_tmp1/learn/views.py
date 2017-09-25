# coding: utf-8
#显示字典中内容

from django.shortcuts import render

# Create your views here.

def home(request):
        info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
        return render(request,'home.html',{'info_dict':info_dict})
