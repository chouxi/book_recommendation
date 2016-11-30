
import mani_db
from heapq import nlargest
REC_NUM = int(10)

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


def most_popular():
    conn = mani_db.db_conn()
    sql = "SELECT * FROM `bx-book-avg` where `rating_num` > 20 ORDER BY `rating_avg` DESC LIMIT 100"
    most_pop_res = mani_db.db_select(sql, conn)
    mani_db.db_close(conn)
    return nlargest(REC_NUM, most_pop_res, key=lambda ele:ele[1])

if __name__ == '__main__':
    #init_popular_data()
    print most_popular()