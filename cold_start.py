
import mani_db
from heapq import nlargest

def get_top_rating(book_rate):
    book_list = []
    for key, value in book_rate.items():
        avg = float(value[0]) / value[1]
        book_list.append([key, value[0], value[1], avg])
    first_filter = nlargest(100, book_list, key=lambda ele:ele[1])
    return nlargest(10, first_filter, key=lambda ele:ele[3])

def get_rating_by_user(user_list):
    book_rate = {}
    conn = mani_db.db_conn()
    for user in user_list:
        sql = "SELECT `ISBN`,`book-rating` FROM `bx-book-ratings` where `user-id` = %d" %(int(user[0]))
        result = mani_db.db_select(sql, conn)
        #print result
        for (ISBN, rating) in result:
            if book_rate.has_key(ISBN):
                book_rate[ISBN][1] += 1
                book_rate[ISBN][0] += rating
            else:
                book_rate.setdefault(ISBN, [rating, 1])
    #print book_rate
    mani_db.db_close(conn)
    return book_rate

def popular_region(country, state):
    conn = mani_db.db_conn()
    sql = "SELECT `User-id` FROM `bx-users` where `country` = '%s'" % (country.lower())
    if country.lower() == "usa":
        sql += " and `state` = '%s'" % (state.lower())
    region_user = mani_db.db_select(sql, conn)
    mani_db.db_close(conn)
    book_rate = get_rating_by_user(region_user)
    return get_top_rating(book_rate)

def popular_age(age):
    book_rate = {}
    age_int = int(age)
    if age_int < 0 or age_int > 100:
        return None
    age_ten = age_int / 10
    age_one = age_int % 10
    if age_one >= 5:
        age_one = 5
    else:
        age_one = 0
    age_int = age_ten * 10 + age_one
    sql = "SELECT `User-id` FROM `bx-users` where `age` >= '%s' and `age` < '%s'" \
    % (str(age_int), str((age_int + 5)))
    conn = mani_db.db_conn()
    age_user = mani_db.db_select(sql, conn)
    mani_db.db_close(conn)
    book_rate = get_rating_by_user(age_user)
    return get_top_rating(book_rate)


if __name__ == '__main__':
    #print popular_age(25)
    print popular_region("usa","california")