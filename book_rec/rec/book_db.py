from models import BxBooks

def get_book_by_ISBN(sel_isbn):
    return BxBooks.objects.get(isbn=sel_isbn)

def get_book_list_like(like_str):
    print BxBooks.objects.filter(book_title__contains=like_str)