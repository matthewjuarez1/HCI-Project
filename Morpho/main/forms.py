from django.db import models
from .models import *
from django.forms import ModelForm, forms

class ThemeForm(ModelForm):
    class Meta:
        model = Theme
        fields = ['name','contents']

class SeriesForm(ModelForm):
    class Meta:
        model = Series
        fields = ['name','expected_works','premise','genre','driver']



class MediaForm(ModelForm):
    class Meta:
        model = Media
        fields = ['name', 'media_type','description', 'url']

class AnthologyForm(ModelForm):
    class Meta:
        model = Anthology
        fields = ['name','expected_works','premise','genre','driver']

class PoemForm(ModelForm):
    class Meta:
        model = Poem
        fields = ['name','contents']

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name','premise','genre','driver']

class ChapterForm(ModelForm):
    class Meta:
        model = Chapter
        fields = ['name', 'contents']

class IdeaForm(ModelForm):
    class Meta:
        model = Idea
        fields = ['name','contents']

class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = ['name','contents']
