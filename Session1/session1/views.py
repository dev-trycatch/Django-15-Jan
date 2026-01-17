from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello Dev</h1>")

def about(request):
    return HttpResponse("About page")

def blog(request,name):
    return HttpResponse(f"This is <strong>{name}</strong>.")

def course(request,id):
    return HttpResponse(f"<strong>{id}</strong>")