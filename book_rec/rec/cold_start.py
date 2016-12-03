from models import BxBookRatings
from models import BxUsers
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
    for user in user_list:
        result = user.ratings.all().values_list('isbn','book_rating')
        for (isbn, book_rating) in result:
            if book_rate.has_key(isbn):
                book_rate[isbn][1] += 1
                book_rate[isbn][0] += book_rating
            else:
                book_rate.setdefault(isbn, [book_rating, 1])
    return book_rate

def popular_region(country, state):
    sql = {}
    sql['country'] = country.lower()
    if country.lower() == "usa":
        sql['state'] = state.lower()
    region_user = BxUsers.objects.filter(**sql)
    book_rate = get_rating_by_user(region_user)
    return get_top_rating(book_rate)

def popular_region(sel_user_id, country, state):
    sql = {}
    sql['country'] = country.lower()
    if country.lower() == "usa":
        sql['state'] = state.lower()
    region_user = BxUsers.objects.filter(**sql)
    book_rate = get_rating_by_user(region_user)
    already_rated = list(BxBookRatings.objects.filter(user_id=sel_user_id))
    for (key, value) in book_rate.items():
        for rated in already_rated:
            if rated.isbn == key:
                already_rated.remove(rated)
                del book_rate[key]
    return get_top_rating(book_rate)

def popular_age(age):
    book_rate = {}
    age_int = age
    if age_int < 0 or age_int > 100:
        return None
    age_ten = age_int / 10
    age_one = age_int % 10
    if age_one >= 5:
        age_one = 5
    else:
        age_one = 0
    age_int = age_ten * 10 + age_one
    #sql = "SELECT `User-id` FROM `bx-users` where `age` >= '%s' and `age` < '%s'" \
    #% (str(age_int), str((age_int + 5)))
    age_user = BxUsers.objects.filter(age__range=["%s"%(age_int), "%s"%((age_int + 4))])
    book_rate = get_rating_by_user(age_user)
    return get_top_rating(book_rate)

def popular_age(sel_user_id,age):
    book_rate = {}
    age_int = age
    if age_int < 0 or age_int > 100:
        return None
    age_ten = age_int / 10
    age_one = age_int % 10
    if age_one >= 5:
        age_one = 5
    else:
        age_one = 0
    age_int = age_ten * 10 + age_one
    #sql = "SELECT `User-id` FROM `bx-users` where `age` >= '%s' and `age` < '%s'" \
    #% (str(age_int), str((age_int + 5)))
    age_user = BxUsers.objects.filter(age__range=["%s"%(age_int), "%s"%((age_int + 4))])
    book_rate = get_rating_by_user(age_user)
    already_rated = list(BxBookRatings.objects.filter(user_id=sel_user_id))
    for (key, value) in book_rate.items():
        for rated in already_rated:
            if rated.isbn == key:
                already_rated.remove(rated)
                del book_rate[key]
    return get_top_rating(book_rate)

#if __name__ == '__main__':
    #print popular_age(25)
    #print popular_region("usa","california")