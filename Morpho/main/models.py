from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Theme(models.Model):
    name = models.CharField(max_length=100)
    contents = models.CharField(max_length=1000)
    def __str__(self):
        return self.text


class Series(models.Model):
    name = models.CharField(max_length=50)
    expected_works = models.IntegerField()
    premise = models.CharField(max_length=1000)
    genre = models.CharField(max_length=50)
    driver = models.CharField(max_length=500)
    def __str__(self):
        return self.text


class Picture(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    url = models.CharField(max_length=256)
    file_path = models.CharField(max_length=256)
    def __str__(self):
        return self.text

class Song(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    url = models.CharField(max_length=256)
    file_path = models.CharField(max_length=256)
    def __str__(self):
        return self.text


class Anthology(models.Model):
    name = models.CharField(max_length=50)
    expected_works = models.IntegerField()
    premise = models.CharField(max_length=1000)
    genre = models.CharField(max_length=50)
    driver = models.CharField(max_length=500)
    def __str__(self):
        return self.text

class Poem(models.Model):
    title = models.CharField(max_length=50)
    contents = models.CharField(max_length=1000)
    def __str__(self):
        return self.text

class Book(models.Model):
    name = models.CharField(max_length=50)
    expected_works = models.IntegerField()
    premise = models.CharField(max_length=1000)
    genre = models.CharField(max_length=50)
    driver = models.CharField(max_length=500)
    def __str__(self):
        return self.text

class Chapter(models.Model):
    title = models.CharField(max_length=50)
    text= models.CharField(max_length=1000)
    def __str__(self):
        return self.text

class Idea(models.Model):
    name = models.CharField(max_length=50)
    contents = models.CharField(max_length=1000)
    def __str__(self):
        return self.text
