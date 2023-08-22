

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse

from .forms import UserProfileForm
from .forms import AuthorForm
from .forms import PublisherForm
from .forms import BooksForm
from .models import User
from .models import Author
from .models import Publisher
from .models import Books
import logging
from django.shortcuts import redirect


# Create your views here.

def shop(request):
    return HttpResponse("hello world")


def demo(request):
    temp = loader.get_template('demo.html')
    return HttpResponse(temp.render())


def createUser(request):
    user_created = False
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            print("success")
            user_created = True
        else:
            print(form.errors)
    else:
        form = UserProfileForm()
    context = {}
    context['form'] = form
    users = User.objects.all().values()
    context['user'] = users
    
    
    return render(request, 'user_profile.html', {'form': form, 'user_created': user_created})




def author_profile(request):
    author_id = ""
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            saved_instance = form.save()
            author_id = saved_instance.id
            print("save -- ",author_id)
            author = Author.objects.all()
            publisher = Publisher.objects.all()
            print("success")
            target_url = reverse(books_profile)+ f'?author_id={author_id}'
            return redirect(target_url)
        else:
            print(form.errors)
    else:
        form = AuthorForm()
        return render(request, 'author.html', {'form':form, 'author_id':author_id})
    
    


def publisher_profile(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            print("success")
        else:
            print(form.errors)
    else:
        form = PublisherForm()
    
    return render(request, 'publisher.html', {'form':form})

def books_profile(request):
    context = {}
    author = Author.objects.all()
    publisher = Publisher.objects.all()
    context['publisher'] = publisher
    context['author'] = author
    record_info =''
    
    
    try:
        author_id = request.GET.get('author_id')
        context['author_id'] = author_id
        record_info = Author.objects.get(id=author_id)
        context['record_info'] = record_info
        print("record id == ",author_id)
        print("record id == ",record_info)
    except:
        pass

    print(author)
    if request.method == 'POST':
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save()
            print("success")
            nav_to = 'book_info.html'
            books = Books.objects.all()
            context['books'] = books
            return render(request, nav_to, context)
        else:
            print(form.errors)
    else:
        form = BooksForm()
        nav_to = 'books.html'
        return render(request, nav_to, context)


def books_info(request):
    books = Books.objects.all()
    return render(request, 'book_info.html', {'books': books})



def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
