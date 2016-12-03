from models import BxBooks
def get_book_by_ISBN(sel_isbn):
    try:
        result = BxBooks.objects.get(isbn=sel_isbn)
    except BxBooks.DoesNotExist:
        result = None
    return result

def get_book_list_like(like_str):
    try:
        result = BxBooks.objects.filter(book_title__contains=like_str)
    except BxBooks.DoesNotExist:
        result = None
    return result
