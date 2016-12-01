import mani_db
def get_rating_by_ISBN(ISBN):
    conn = mani_db.db_conn()
    sql = "SELECT * FROM `bx-books-avg` WHERE `ISBN` == '%s'" %(ISBN)
    ISBN_list = mani_db.db_select(sql, conn)
    mani_db.db_close()
    return ISBN_list

def update_rating_avg(conn, ISBN, rating):
    sql = "SELECT `rating-sum`, `rating-num` FROM `bx-books-avg` WHERE `ISBN` == '%s'" %(ISBN)
    result = mani_db.db_select(sql, conn)
    rating_num = 1
    rating_sum = rating
    if not result == None:
        rating_sum += result[0]
        rating_num += result[1]
    rating_avg = float(rating_sum) /rating_num
    sql = "UPDATE `bx-books-avg` SET `rating_sum` = '%d', `rating_num` = '%d', `rating_avg`='%f' WHERE `ISBN` == '%s'" \
    % (rating_sum, rating_num, rating_avg, ISBN)


def add_rating(user_id, ISBN, rating):
    conn = mani_db.db_conn()
    sql = "INSERT INTO `bx-books-rating` VALUES (%d, '%s', '%d')"\
    % (int(user_id), ISBN, rating)
    mani_db.db_insert(sql, conn)
    update_rating_avg(conn, ISBN, rating)
    mani_db.db_close(conn)