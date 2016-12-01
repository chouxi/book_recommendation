__author__ = 'Zane'
from models import BxBookRatings
from django.db.models import Q
import numpy as np

BOUND = 20
def selecte_data():
    rating_res = BxBookRatings.objects.filter(~Q(book_rating=0)).values_list('user_id','isbn','book_rating')
    return rating_res

def gene_orig_mat():
    book_dict={}
    user_dict={}
    user_count = 0
    book_count = 0
    results = selecte_data()
    print len(results)
    if results == None:
        return None
    for (user, book, rating) in results:
        if not user_dict.has_key(user):
            user_dict.setdefault(user, [0, 1])
        else:
            user_dict[user][1] += 1
            if user_dict[user][1] == BOUND:
                user_dict[user][0] = user_count
                user_count += 1;

        if not book_dict.has_key(book):
            book_dict.setdefault(book, [0, 1])
        else:
            book_dict[book][1] += 1
            if book_dict[book][1] == BOUND:
                book_dict[book][0] = book_count
                book_count += 1;

    for key, value in book_dict.items():
        if value[1] < int(BOUND):
            del book_dict[key]
    for key, value in user_dict.items():
        if value[1] < int(BOUND):
            del user_dict[key]
    orig_mat = np.zeros((user_count, book_count), dtype=np.int8)
    for (user, book, rating) in results:
        if user_dict.has_key(user) and book_dict.has_key(book):
            orig_mat[user_dict[user][0],book_dict[book][0]] = rating
    return [orig_mat, user_dict, book_dict]
#if __name__ == '__main__':
#	gene_orig_mat()