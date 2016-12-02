from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import json
import os
import use
from models import BxBookAvg
from user_login import check_user 
from models import BxBooks
from book_db import get_book_by_ISBN

def search(request):
#    return render(request, 'search.html')
    return render(request, 'main.html')
def back(request):
    return render(request, 'index.html')
def image(request):
    Lista = ["html","CSS","jQuery","python","django"]
    Listb = [("1","2"),("3","4",),("5","6")]
    picture = "http://images.amazon.com/images/P/0001046438.01.THUMBZZZ.jpg"
    return render(request, 'index.html',{'Lista':Lista, 'picture':picture, 'Listb':Listb})
def home(request):
    string = "My recommand book is harry porter"
    return render(request, 'home.html',{'string':string})
    #return render(request, 'home.html')
def result(request):
    #key = request.GET.get('q')
    key = request.GET.get('id')
    Listp = check_user(144455)
    Listpop = []
    Listregion = []
    Listage = []
    Listbook = []
    newListpop = []
    newListregion = []
    newListage = []
    if int(Listp[0]) == 3:
        mostp = Listp[1]
        for item in mostp:
            Listrec.append((get_book_by_ISBN(item[0]),item[2],item[3]))
        return render(request,'index.html', {'Lista':Lista, 'message':message, 'oic':oic, 'Listpopular':Listpopular})    
    else if int(Listp[0]) == 1:
        Listpop = Listp[1]
        for item in Listpop:
            newListpop.append((get_book_by_ISBN(item[0]),item[2],item[3]))
        Listregion = Listp[2]
        for item in Listregion:
            newListregion.append((get_book_by_ISBN(item[0]),item[2],item[3]))
        Listage = Listp[3]
        for item in Listage:
            newListage.append((get_book_by_ISBN(item[0]),item[2],item[3]))

    else if int(Listp[0]) == 2:
        Listpop = Listp[1]
        for item in Listpop:
            newListpop.append((get_book_by_ISBN(item[0]),item[2],item[3]))
        Listregion = Listp[2]
        for item in Listregion:
            newListregion.append((get_book_by_ISBN(item[0]),item[2],item[3]))
        Listage = Listp[3]
        for item in Listage:
            newListage.append((get_book_by_ISBN(item[0]),item[2],item[3]))


    Lista = ["html","CSS","jQuery","python","django"]
    #message = use.test()
    message = "http://images.amazon.com/images/P/0001046438.01.THUMBZZZ.jpg"
    oic = "qweqwehttp://images.amazon.com/images/P/0001046438.01.THUMBZZZ.jpg22222"
    return render(request,'index.html', {'Lista':Lista, 'message':message, 'oic':oic, 'Listpopular':Listpopular})
def index(request):
    return HttpResponse("hello,by polls")
def test(request):
        Lista = ["html","CSS","jQuery","python","django"]
        return render(request, 'result.html', {'Lista':Lista})
def pic(request):
    Lista = ["html","CSS","jQuery","python","django"]
    Listb = [("1","2"),("3","4",),("5","6")]
    picture = "http://images.amazon.com/images/P/0001046438.01.THUMBZZZ.jpg"
    return render(request, 'main.html',{'Lista':Lista, 'picture':picture, 'Listb':Listb})
#def recommend(request):
#   key = request.GET.get('q')
#   judge is old or new
#    if key == '1'
#        message= ""
#   else if key == '2'
#        message= ""
#   return render(request,'result.html',{'message':message})


# Create your views here.