from models import BxBookAvg
from models import BxBookRatings
from heapq import nlargest
REC_NUM = int(10)
'''
//init popular data 
def init_popular_data():
    conn = mani_db.db_conn()
    sql = "SELECT `ISBN`,`Book-Rating` FROM `bx-book-ratings` where `book-rating` <> 0;"
    rating_res = mani_db.db_select(sql, conn)
    rating_dict = {}
    for (book, rating) in rating_res:
        if not rating_dict.has_key(book):
            rating_dict.setdefault(book, [rating, 1])
        else:
            rating_dict[book][0] += rating
            rating_dict[book][1] += 1
    for (ISBN, value) in rating_dict.items():
        avg = float(value[0]) / value[1]
        sql = "INSERT INTO `bx-book-avg` VALUES ('%s', '%d', '%d', '%f')" % \
        (ISBN, value[0], value[1], avg)
        mani_db.db_insert(sql, conn)
    mani_db.db_close(conn)
'''

def most_popular():
    #sql = "SELECT * FROM `bx-book-avg` where `rating_num` > 20 ORDER BY `rating_avg` DESC LIMIT 100"
    most_pop_res = BxBookAvg.objects.filter(rating_num__gt=20).order_by('-rating_avg')[:100]
    return nlargest(REC_NUM, most_pop_res, key=lambda ele:ele.rating_sum)

def most_popular(sel_user_id):
    most_pop_res = list(BxBookAvg.objects.filter(rating_num__gt=20).order_by('-rating_avg')[:100])
    already_rated = list(BxBookRatings.objects.filter(user_id=sel_user_id))
    for pop_res in most_pop_res:
        for rated in already_rated:
            if rated.isbn == pop_res.isbn:
                already_rated.remove(rated)
                most_pop_res.remove(pop_res)
    return nlargest(REC_NUM, most_pop_res, key=lambda ele:ele.rating_sum)
