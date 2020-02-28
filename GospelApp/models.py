from django.db import models
from django.utils import timezone
from datetime import datetime


# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    picture = models.ImageField(upload_to='images')

    class Meta:
        verbose_name= "about"
        verbose_name_plural="about"
    
    def __str__(self):
        return self.title

class Contact(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    comment = models.TextField()

    class Meta:
        verbose_name = "contact"
        verbose_name_plural ="contact"

    def __str__(self):
        return self.email 

class Companygoals(models.Model):
    title = models.CharField(max_length=100)
    context = models.TextField(max_length=100)
    logo = models.ImageField(upload_to='images') 

    class Meta: 
        verbose_name= "company_values"
        verbose_name_plural= "company_values"

    def __str__(self):
        return self.title

class Article(models.Model):
    book_title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date_posted = models.DateField(null=True, blank=True) 
    book_summary = models.TextField()
    photo = models.ImageField(upload_to='images')
    article_detail = models.TextField(default='article details')
    
    class Meta:
        verbose_name = "articles"
        verbose_name_plural = "articles"

    def __str__(self):
            return self.book_title

class Books(models.Model):
    book_photho = models.ImageField(upload_to='images')
    book_title = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    book_summary = models.TextField()
    content_details = models.TextField(default="details")


    class Meta:
        verbose_name = "book"
        verbose_name_plural = "book"
    
    def __str__(self):
        return self.book_title
        

class Videos(models.Model):
    Video = models.FileField(upload_to='videos')
    video_title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "video"
        verbose_name_plural = "video"
    
    def __str__(self):
        return self.video_title

class Slides(models.Model):
    slide_image = models.ImageField(upload_to='images')
    slide_title =models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "slides"
        verbose_name_plural = "slides"
    
    def __str__(self):
        return self.slide_title
    
    
        
