from models import BxBooks
from rating_db import get_rating_by_ISBN
from heapq import nlargest
def get_book_by_ISBN(sel_isbn):
    try:
        result = BxBooks.objects.get(isbn=sel_isbn)
    except BxBooks.DoesNotExist:
        result = None
    return result

def get_book_list_like(like_str):
    print like_str
    try:
        result = BxBooks.objects.filter(book_title__contains=like_str)
    except BxBooks.DoesNotExist:
        result = None
    if result == None:
        return result
    book_dict = []
    for res in result:
        book_rating = get_rating_by_ISBN(res.isbn)
        if book_rating == None:
            continue
        book_dict.append([res, book_rating.rating_sum, book_rating.rating_num, book_rating.rating_avg])
    if len(book_dict) <= 10:
        return book_dict
    sum_fil_book = nlargest(100, book_dict, key=lambda ele:ele[3])
    book_sum = nlargest(10, sum_fil_book, key=lambda ele:ele[1])
    for item in book_sum:
        print item[0].isbn
        item[3] = round(item[3], 2)
    return book_sum