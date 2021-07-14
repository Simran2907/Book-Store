import MySQLdb
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import CreateView, DetailView
from django.db.models import CharField, Model
from django_mysql.models import ListCharField

class Book(models.Model):
    book = models.CharField(max_length=200)
    author = models.CharField( max_length=100)
    genre = ListCharField( base_field = CharField(max_length=20),size=10,max_length = (10*21))
    language = ListCharField( base_field = CharField(max_length=20),size=10,max_length = (10*21))

    def __str__(self):
        return self.book

    def get_absolute_url(self):
        return reverse('book-detail',kwargs={'pk':self.pk})