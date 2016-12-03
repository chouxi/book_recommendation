from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import json
import os
import use
from models import BxBookAvg
from models import BxBooks
from book_db import get_book_by_ISBN
import user_login
from rating_db import get_rating_by_ISBN
from rating_db import add_rating
from book_db import get_book_list_like
def search(request):
#    return render(request, 'search.html')
    return render(request, 'main.html')
def searchbook(request):
    like_str = request.GET.get('put')
    key = request.GET.get('id')
    #key = 123456
    research_res = get_book_list_like(like_str)
    if research_res == None:
        return
    return render(request,'search.html',{'researchList':research_res,'key':key})

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
    key = request.GET.get('id')
    #key = 123456
    city = request.GET.get('city')
    state = request.GET.get('state')
    country = request.GET.get('country')
    age = request.GET.get('age')
    Listrec = []
    Listp = user_login.check_user(123456)
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
            book = get_book_by_ISBN(item[0])
            if not book == None:
                Listrec.append((book ,item[2],round(item[3],2)))
        return render(request,'index.html', {'Listrec':Listrec,'key':key})    
    elif int(Listp[0]) == 1:
        #if city == None or city == None or country == None or age == None:
            #warning here
        user_res = user_login.new_user(key, age, city, state, country)
        if len(user_res) < 3:
            return
        if not user_res[0] == None:
            for item in user_res[0]:
                book = get_book_by_ISBN(item.isbn)
                if not book == None:
                    newListpop.append((book,item.rating_sum,round(item.rating_avg,2)))
        if not user_res[1] == None:
            for item in user_res[1]:
                book = get_book_by_ISBN(item[0])
                if not book == None:
                    newListage.append((book ,item[2],round(item[3], 2)))
        if not user_res[2] == None:
            for item in user_res[2]:
                book = get_book_by_ISBN(item[0])
                if not book == None:
                    newListregion.append((book ,item[2],round(item[3], 2)))
        return render(request,'index2.html', {'Listpop':newListpop,'Listregion':newListregion,'Listage':newListage,'key':key})    
    elif int(Listp[0]) == 2:
        Listpop = Listp[1]
        if not Listpop == None:
            for item in Listpop:
                book = get_book_by_ISBN(item.isbn)
                if not book == None:
                    newListpop.append((book,item.rating_num,round(item.rating_avg), 2))
        Listage = Listp[2]
        if not Listage == None:
            for item in Listage:
                book = get_book_by_ISBN(item[0])
                if not book == None:
                    newListage.append((book,item[2],round(item[3]), 2))
        Listregion = Listp[3]
        if not Listregion == None:
            for item in Listregion:
                book = get_book_by_ISBN(item[0])
                if not book == None:
                    newListregion.append((book,item[2],round(item[3]), 2))
        return render(request,'index3.html', {'Listpop':newListpop,'Listregion':newListregion,'Listage':newListage,'key':key})    

    #Lista = ["html","CSS","jQuery","python","django"]
    #message = use.test()
    #message = "http://images.amazon.com/images/P/0001046438.01.THUMBZZZ.jpg"
    #oic = "qweqwehttp://images.amazon.com/images/P/0001046438.01.THUMBZZZ.jpg22222"
    #return render(request,'index.html', {'Lista':Lista, 'message':message, 'oic':oic, 'Listpopular':Listpopular})
def pic(request):
    key = request.GET.get('key')
    web = request.GET.get('isbn')
    book = get_book_by_ISBN(web)
    rating = get_rating_by_ISBN(web)
    ratingavg = round(rating.rating_avg,2)
    return render(request, 'book.html',{'web':web, 'rating':rating, 'book':book,'ratingavg':ratingavg,'key':key })

def backtorec(request):
    key = request.GET.get('key')
    isbntmp = request.GET.get('bookisbn')
    ratetmp = request.GET.get('rating')
    print isbntmp, ratetmp, key
    mani_rating(key, isbntmp, ratetmp)
    Listrec = []
    Listp = user_login.check_user(int(key))
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
            book = get_book_by_ISBN(item[0])
            if not book == None:
                Listrec.append((book ,item[2],round(item[3],2)))
        return render(request,'index.html', {'Listrec':Listrec,'key':key})    
    elif int(Listp[0]) == 2:
        Listpop = Listp[1]
        if not Listpop == None:
            for item in Listpop:
                book = get_book_by_ISBN(item.isbn)
                if not book == None:
                    newListpop.append((book,item.rating_num,round(item.rating_avg), 2))
        Listage = Listp[2]
        if not Listage == None:
            for item in Listage:
                book = get_book_by_ISBN(item[0])
                if not book == None:
                    newListage.append((book,item[2],round(item[3]), 2))
        Listregion = Listp[3]
        if not Listregion == None:
            for item in Listregion:
                book = get_book_by_ISBN(item[0])
                if not book == None:
                    newListregion.append((book,item[2],round(item[3]), 2))
        return render(request,'index3.html', {'Listpop':newListpop,'Listregion':newListregion,'Listage':newListage,'key':key})    

def mani_rating(user_id, isbn, rating):
    add_rating(user_id, isbn, rating)


#def recommend(request):
#   key = request.GET.get('q')
#   judge is old or new
#    if key == '1'
#        message= ""
#   else if key == '2'
#        message= ""
#   return render(request,'result.html',{'message':message})


# Create your views here.