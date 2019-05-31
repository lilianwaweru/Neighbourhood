from django.shortcuts import render

# Create your views here.
def welcome(request):

    return render(request,'welcome.html')

def index(request):
    title = "Index Page"
    return render (request, 'index.html', {"title":title})
