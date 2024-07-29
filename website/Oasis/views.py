from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'Oasis/index.html')

def about(request):
    return render(request, 'Oasis/about.html')

def contact(request):
    return render(request, 'Oasis/contact.html')

def blog(request):
    return render(request, 'Oasis/blog.html')

def news(request):
    return render(request, 'Oasis/news.html')