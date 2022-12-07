from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Theme(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contents = models.CharField(max_length=1000)
    last_modified = models.DateField(auto_now=True)
    def __str__(self):
        return self.name


class Series(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    expected_works = models.IntegerField()
    premise = models.TextField(max_length=1000)
    genre = models.CharField(max_length=50)
    driver = models.CharField(max_length=500)
    last_modified = models.DateField(auto_now=True)
    def __str__(self):
        return self.name


class Media(models.Model):
    MEDIA_TYPES=(
        (1,"Song"),
        (2,"Image")
    )
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    media_type = models.IntegerField(choices=MEDIA_TYPES, default=1)
    description = models.CharField(max_length=1000)
    url = models.CharField(max_length=256)
    last_modified = models.DateField(auto_now=True)
    def __str__(self):
        return self.name



class Anthology(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    expected_works = models.IntegerField()
    premise = models.TextField(max_length=1000)
    genre = models.CharField(max_length=50)
    driver = models.CharField(max_length=500)
    last_modified = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

class Poem(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    contents = models.TextField(max_length=1000)
    last_modified = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

class Character(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    contents = models.TextField(max_length=1000)
    last_modified = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

class Book(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    premise = models.TextField(max_length=1000)
    genre = models.CharField(max_length=50)
    driver = models.TextField(max_length=500)
    last_modified = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

class Chapter(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    contents= models.TextField(max_length=1000)
    last_modified = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

class Idea(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    contents = models.TextField(max_length=1000)
    last_modified = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

class Compilation(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    container_type = models.CharField(max_length=20)
    container_id = models.CharField(max_length=3)
    ideas = models.ManyToManyField(Idea)
    themes = models.ManyToManyField(Theme)
    books = models.ManyToManyField(Book)
    characters = models.ManyToManyField(Character)
    chapters = models.ManyToManyField(Chapter)
    poems = models.ManyToManyField(Poem)
    series = models.ManyToManyField(Series)
    anthologies = models.ManyToManyField(Anthology)
    media = models.ManyToManyField(Media)
    @classmethod
    def create(cls,type):
        comp = cls(container_type=type)
        return comp
    def __str__(self):
        return self.container_type + str(self.container_id)