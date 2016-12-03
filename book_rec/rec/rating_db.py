from models import BxBookAvg
from models import BxBookRatings
from models import BxUsers
def get_rating_by_ISBN(ISBN):
    #sql = "SELECT * FROM `bx-books-avg` WHERE `ISBN` == '%s'" %(ISBN)
    try:
        result = BxBookAvg.objects.get(isbn=ISBN)
    except BxBookAvg.DoesNotExist:
        result = None
    return result

def update_rating_avg(ISBN, rating):
    #sql = "SELECT `rating-sum`, `rating-num` FROM `bx-books-avg` WHERE `ISBN` == '%s'" %(ISBN)
    #result = mani_db.db_select(sql, conn)
    rating_num = 1
    rating_sum = int(rating)
    rating_res = get_rating_by_ISBN(ISBN)
    if not rating_res == None:
        rating_sum += rating_res.rating_sum
        rating_num += rating_res.rating_num
    #sql = "UPDATE `bx-books-avg` SET `rating_sum` = '%d', `rating_num` = '%d', `rating_avg`='%f' WHERE `ISBN` == '%s'" \
    #% (rating_sum, rating_num, rating_avg, ISBN)
    rating_res.rating_sum = rating_sum
    rating_res.rating_num = rating_num
    rating_res.rating_avg = float(rating_sum) /rating_num
    rating_res.save()

def add_rating(sle_user_id, ISBN, rating):
    #sql = "INSERT INTO `bx-books-rating` VALUES (%d, '%s', '%d')"\
    #% (int(user_id), ISBN, rating)
    insert_rating = BxBookRatings(user_id = BxUsers.objects.get(user_id=sle_user_id), isbn = ISBN, book_rating=rating)
    insert_rating.save()
    update_rating_avg(ISBN, rating)
