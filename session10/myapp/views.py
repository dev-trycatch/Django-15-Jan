from django.shortcuts import render,redirect
from .models import *
from .forms import CategoryForm,ProductForm

# Create your views here.
def category_list(request):
    category = Category.objects.all()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/category_list/')
    else:
        form = CategoryForm()
    return render(request,'category_list.html',{"form":form,'category':category})

def product_list(request):
    product = Product.objects.all()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/product_list/')
    else:
        form = ProductForm()
    return render(request,'product_list.html',{"form":form,'products':product})

def product_Update(request,pk):
    product = Product.objects.get(pk = pk)
    if request.method == "POST":
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('/product_list/')
    else:
        form = ProductForm(instance=product)
    return render(request,'product_update.html',{"form":form})
    

def product_delete(request,pk):
    Product.objects.get(pk = pk).delete()
    return redirect('/product_list/')