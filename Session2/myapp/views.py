from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    li1 = [
        {'name':'abc','marks':23,'email':'abc@gmail.com'},
        {'name':'pqr','marks':45,'email':'pqr@gmail.com'},
        {'name':'mno','marks':76,'email':'mno@gmail.com'},
        {'name':'xyz','marks':73,'email':'xyz@gmail.com'},
        ]

    # for  i in li1:
    #     print(i['name'])
    context = {
        'data':li1
    }

    # context = {
    #     "name":'Dev',
    #     'age':33,
    #     'page_url':'Home page'
    # }
    return render(request,'index.html',context)

def about(request):
    context = {
         'page_url':'About page'
    }
    return render(request,'about.html',context)
    # return render(request,'about.html',{'page_url':'About page'})

def contact(request):
    return render(request,'contact.html')