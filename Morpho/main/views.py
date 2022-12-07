from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import *
from .models import *
from django.db.models import CharField, Value

FORM_DICT = dict({
    'Idea': IdeaForm,
    'Character':CharacterForm,
    'Theme': ThemeForm,
    'Chapter': ChapterForm,
    'Poem': PoemForm,
    'Book':BookForm,
    'Series':SeriesForm,
    'Anthology': AnthologyForm,
    'Media':MediaForm})

TYPE_DICT = dict({
    'Idea': Idea,
    'Character':Character,
    'Theme': Theme,
    'Chapter': Chapter,
    'Poem': Poem,
    'Book':Book,
    'Series':Series,
    'Anthology': Anthology,
    'Media':Media})

def codeify(lst, existing):
    if existing:
        complete = existing
    else:
        complete = '#'
    for c in lst:
        complete = complete + c + '#'
    return complete

def getCreations(usr):
    creations = {}
    creations["ideas"] = Idea.objects.filter(author=usr)
    creations["themes"] = Theme.objects.filter(author=usr)
    creations["chapters"] = Chapter.objects.filter(author=usr)
    creations["characters"] = Character.objects.filter(author=usr)
    creations["poems"] = Poem.objects.filter(author=usr)
    creations["books"] = Book.objects.filter(author=usr)
    creations["series"] = Series.objects.filter(author=usr)
    creations["anthologies"] = Anthology.objects.filter(author=usr)
    creations["media"] = Media.objects.filter(author=usr)
    return creations

def populate(comp,tbl, lst):
    curr_list=list()
    for i in lst:
        curr_list.append(tbl.objects.get(id=i))
    for j in curr_list:
        comp.add(j)
    return curr_list

# Create your views here.
def index(response):
    return render(response, "main/base.html", {})

@login_required(login_url='/login')
def home(response):
    creations = getCreations(response.user)
    full_collection = ""
    if creations:
        print("creations entered")
        print(creations.__len__())
        for lst in creations.values():
            if lst.__len__() != 0:
                field_type_name= str(lst[0].__class__).split("main.models.",1)[1]
                field_type_name = field_type_name.split("'>",1)[0]
                lst = lst.annotate(field_type=Value(field_type_name,output_field=CharField()))
                lst = lst.values_list('name','last_modified', 'field_type','id')
                if full_collection == "":
                    full_collection = lst
                else:
                    full_collection = full_collection.union(lst)
    print(full_collection.__class__)
    if full_collection != "":
        full_collection = full_collection.order_by('-last_modified')[:5]
    print(full_collection)
    return render(response, 'main/home.html',{"recent":full_collection})

@login_required(login_url='/login')
def create(response):
    return render(response, 'main/create.html',{})

@login_required(login_url='/login')
def create_type(request,type):
    if request.method =='GET':
        if type in FORM_DICT:
            form = FORM_DICT.get(type)()
        else:
            return render(request, 'main/create.html')
    if request.method == 'POST':
        caught_type = request.POST.get("type","")
        fill_form = FORM_DICT.get(caught_type)(request.POST)
        if fill_form.is_valid():
            # Make a factory to dynamically fill out objects of forms
            fill_form.clean()
            obj = fill_form.save(commit=False)
            obj.author = request.user
            #fill_form.author = request.user.id
            obj.save()
            return render(request, 'main/create.html')
    return render(request, 'main/create_type.html',{"type":type,'form':form})

@login_required(login_url='/login')
def view(request):
    creations = getCreations(request.user)
    return render (request, 'main/view.html',{"creations": creations})

@login_required(login_url='/login')
def viewCreation(request,type,id):
    view_type = TYPE_DICT.get(type)
    creation = view_type.objects.get(id=id)
    if view_type == Media:
        print("is media")
        print(creation.media_type)
        if creation.media_type == 1:
            media_url = creation.url
            if media_url.__contains__("https://youtu.be/"):
                creation.yt_link = True
            creation.media_url = media_url.split("https://youtu.be/",1)[1]
    pile = Compilation.objects.filter(container_type=type, container_id=id)
    if pile:
        pile = Compilation.objects.get(container_type=type, container_id=id)
        pile.ideas_lst = pile.ideas.all()
        pile.themes_lst = pile.themes.all()
        pile.anthologies_lst = pile.anthologies.all()
        pile.books_lst = pile.books.all()
        pile.poems_lst = pile.poems.all()
        pile.series_lst = pile.series.all()
        pile.chapters_lst = pile.chapters.all()
        pile.characters_lst = pile.characters.all()
        pile.media_lst = pile.media.all()
    return render(request, "main/viewcreation.html",{"creation":creation, "pile":pile})

@login_required(login_url='/login')
def chooseContainer(request):
    creations = getCreations(request.user)
    return render (request, 'main/compileContainer.html',{"creations": creations})

@login_required(login_url='/login')
def chooseComponents(request, type,id):
    if request.method == "POST":
        if Compilation.objects.filter(container_type=type, container_id=id).exists():
            comp = Compilation.objects.get(container_type=type, container_id=id)
        else:
            comp = Compilation.create(type)
            comp.container_id = id
        return Compile(request,comp)
    
    creations = getCreations(request.user)
    return render (request, 'main/compileComponents.html',{"creations": creations})

@login_required(login_url='/login')
def Compile(request,comp):
    comp.author = request.user
    comp.save()
    ideas = request.POST.getlist('Ideas')
    populate(comp.ideas,Idea,ideas)

    themes = request.POST.getlist('Themes')
    populate(comp.themes,Theme,themes)

    chapters = request.POST.getlist('Chapters')
    populate(comp.chapters, Chapter,chapters)

    characters = request.POST.getlist('Characters')
    populate(comp.characters,Character,characters)

    poems = request.POST.getlist('Poems')
    populate(comp.poems, Poem,poems)

    books = request.POST.getlist('Books')
    populate(comp.books, Book,books)

    sers = request.POST.getlist('Series')
    populate(comp.series, Series,sers)

    anthologies = request.POST.getlist('Anthologies')
    populate(comp.anthologies, Anthology,anthologies)

    media = request.POST.getlist('Media')
    populate(comp.media, Media,media)
    return redirect('ViewCreation', type=comp.container_type, id = comp.container_id)