
import mani_db
def get_rating_by_ISBN():
    
def update_rating_avg(conn, ISBN, rating):


def add_rating(user_id, ISBN, rating):
    conn = mani_db.db_conn()
    sql = "INSERT INTO `bx-books-rating` VALUES (%d, '%s', '%d')"\
    % (int(user_id), ISBN, rating)
    mani_db.db_insert(sql, conn)

    mani_db.db_close(conn)