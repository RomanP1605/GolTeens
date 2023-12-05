from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Article, News


# Create your views here.
def index(request):
    # author = Author.objects.create(name="Author") # одразу створити
    # title = News.objects.create(title='Name', content='123') # dz
    # get_more_3 = News.objects.filter(id>3) # dz error!!!!!!!!!!!!!!!!!!!!
    get_apple = News.objects.filter(title='Apple')  # dz
    get_banana = News.objects.filter(content='Banana')  # dz
    get_pineapple = News.objects.filter(content='pineapple')  # dz
    get_cherry = News.objects.filter(content='cherry')  # dz
    get_name = News.objects.filter(title='Name')  # dz
    # author = Author(name='Author')
    # author.name = 'Author'
    # author.save() # Saving
    # authors = Author.objects.all() # take all list of authors
    # author = Author.objects.get(id=2) # only one by id. If author.object.filter print list of peoples who has this id or name
    # author.name = 'Vasil' # change name
    # author.save() # save
    # author.delete() # delete
    print(get_apple)
    print(get_banana)
    print(get_pineapple)
    print(get_cherry)
    print(get_name)
    authors = Author.objects.all()
    context = {"authors": authors}
    return render(request, "testapp/index.html", context=context)
