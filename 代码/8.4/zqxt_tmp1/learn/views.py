# coding: utf-8
#实例四，在模板进行 条件判断和 for 循环的详细操作

from django.shortcuts import render

# Create your views here.

def home(request):
        List = map(str,range(100))   # yi ge chang du wei 100 de List
        return render(request, 'home.html',{'List':List})
