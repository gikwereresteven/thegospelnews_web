from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from .models import  About,Companygoals,Article,Books,Contact,Videos,Slides

# Create your views here.

# fetching from db
about_us = About.objects.all()
values = Companygoals.objects.all()
book_articles = Article.objects.all()
books = Books.objects.all()
videospage = Videos.objects.all()
slides = Slides.objects.all()
  

# send to user
context = {
    'about': about_us,
    'value': values,
    'article': book_articles,
    'book' : books,
    'video': videospage,
    'slide': slides,
    
}

def home(request):
    if request.method =='POST':
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        comment = request.POST.get("comment")
        data = Contact(firstname = firstname, lastname = lastname, email = email, comment = comment)
        data.save()
    book_articles = Article.objects.all()[:2]
        
       
       
    return render(request, 'pages/home.html', context, {'article': book_articles})

def book(request, pk):
    bk = get_object_or_404(Books, pk = pk)
    return render(request, 'pages/books.html', {'page': bk})


def bookpage(request):
    return render(request, 'pages/bookpage.html', {'bookp': books})

def articlepage(request):
    book_articles = Article.objects.all()
    return render(request, 'pages/articlepage.html', {'articlepage': book_articles}, context)

def articles(request, pk):
    post = get_object_or_404(Article, pk=pk)  
    return render(request, 'pages/articles.html', {'article':post})

def videos(request):
    return render(request, 'pages/videos.html', {'vidopage': videospage})