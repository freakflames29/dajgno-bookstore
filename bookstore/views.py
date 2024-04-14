from django.shortcuts import render
from .forms import BookForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Book
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(rq):
    allbooks=Book.objects.all()
    return render(rq,"bookstore/index.html",{
        "allbooks":allbooks
    })

def new(rq):
    form=BookForm()
    return render(rq,"bookstore/new.html",{
        "form":form,
        "title":"Add a new book",
        "method":"POST",
        "action":"create"
    })

@login_required(login_url="login")
def view_edit_delete(rq,id):
    book=Book.objects.get(id=id)

    if rq.method=='GET':
        # book=Book.objects.get(id=id)
        return render(rq,'bookstore/show.html',{
            "book":book
        })
  
    

def edit_and_update(rq,id):
    if rq.method=='GET':
        book=Book.objects.get(id=id)
        form=BookForm(instance=book)
        return render(rq,"bookstore/new.html",{
        "form":form,
        "title":"Edit book",
        "method":"POST",
        "action":'edit',
        "id":book.id
    })
    if rq.method=='POST':
        print("*-"*100)

        book=Book.objects.get(id=id)
        form = BookForm(rq.POST,instance=book)
        if form.is_valid():
            print("*"*100)
            print(form.cleaned_data)
            form.save()
            rooturl=reverse('root')
            return HttpResponseRedirect(rooturl)
        

def delete(rq,id):
    book=Book.objects.get(id=id)
    book.delete()
    rooturl=reverse('root')
    return HttpResponseRedirect(rooturl)


def create(rq):
    if rq.method=="POST":
        form = BookForm(rq.POST)
        if form.is_valid():
            form.save()

    rooturl=reverse('root')
    return HttpResponseRedirect(rooturl)