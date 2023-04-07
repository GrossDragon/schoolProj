
from datetime import datetime
import email
from django.shortcuts import render
from django.http import HttpResponse
from collections import Counter

from .models import Book, Author, Publisher, Pokupka

# Create your views here.

def find_by_id(object,id):
    qs = object.objects.filter(id = id)
    if qs.count() > 0:
        return qs[0]
    else:
        return None

def check_basket(request):
    try:
        request.session['basket']
    except:
        request.session['basket']=[]

    request.session.modified = True

def check_buy(request,to_buy,book_id):
          
   
    if to_buy==1:   
        request.session['basket'].append(book_id)
    elif to_buy==2 and book_id in request.session['basket']:
        request.session['basket'].remove(book_id)

    
    


def index(request):    
    check_basket(request)
    numbersof=len(request.session['basket'])


    books=Book.objects.all() 
    return render(request,'polls/main.html',{'books':books, 'numberof':numbersof})

def info(request):
    check_basket(request)
    numbersof=len(request.session['basket'])
    


    return render(request, 'polls/info.html',{ 'numberof':numbersof})


def book(request,book_id,to_buy):
    check_basket(request)
    check_buy(request,to_buy,book_id)
    numbersof=len(request.session['basket'])


    book = find_by_id(Book, book_id)
    return render(request,'polls/book.html',{'book':book,'numberof':numbersof})



def author(request,author_id):
    check_basket(request)
    numbersof=len(request.session['basket'])


    
    author = find_by_id(Author, author_id)
    return render(request,'polls/author.html',{'author':author,'numberof':numbersof})


def publisher(request,publisher_id):
    
    check_basket(request)
    numbersof=len(request.session['basket'])


    
    publisher = find_by_id(Publisher, publisher_id)
    return render(request,'polls/publisher.html',{'publisher':publisher,'numberof':numbersof})



def basket(request):
    check_basket(request)
    numbersof=len(request.session['basket'])
    books=[]
    booksValues=[]

    for book in request.session['basket']:
        if book not in books:
            books.append(book)
            booksValues.append(1)
        else:
            booksValues[books.index(book)]+=1
    
    
    
    basket=[]
    Sum=0

    for book in books:
        basket.append(find_by_id(Book,book))
        Sum+=basket[-1].price*booksValues[len(basket)-1]

        


    
    
    return render(request,'polls/basket.html',{'books': basket,'numberof':numbersof, 'booksValues':booksValues, 'Sum':Sum})


def buy(request):
    if request.method == "POST":
        books=' '

        for item in request.session['basket']:
            books=books+find_by_id(Book,item).name
            books+=' '

        

        Pokupka.objects.create(email=request.POST.get('email'),way=request.POST.get('way'),date=datetime.now(),books=books)
        
        #value = str(request.POST.get('way'))

        request.session['basket'].clear()
    #return render(request, '1.html',{'value':value})
    return index(request)