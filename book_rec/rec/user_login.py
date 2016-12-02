from user_db import select_user
from rating_db import get_rating_by_ISBN
from svd_rec import recommend
from orig_matrix import gene_orig_mat
import cold_start
#1 is new user
#2 is old user but no data
#3 is old user can recmmend
def check_user(user_id):
    result = []
    user_obj = select_user(user_id)
    if user_obj == None:
        result.append(1)
        return result
    else:
        result_list = gene_orig_mat()
        myMat = result_list[0]
        user_dict = result_list[1]
        book_dict = result_list[2]
        if user_dict.has_key(int(user_id)):
            rec_result  = recommend(myMat, user_dict[user_id][0])
            if rec_result == None:
                result.append(1)
                result.append(most_popular())
                result.append(popular_age(user_obj.age))
                result.append(popular_region(user_obj.country, user_obj.state))
                return result
        else:
            result.append(2)
            result.append(popular_age(user_obj.age))
            result.append(popular_region(user_obj.country, user_obj.state))
            return result
        rating_list = []
        for (key, value) in book_dict.items():
            for val in rec_result:
                if value[0] == val[0]:
                    rating_obj = get_rating_by_ISBN(key)
                    rating_list.append((rating_obj.isbn, rating_obj.rating_sum, rating_obj. rating_num, rating_obj.rating_avg))
        result.append(3)
        result.append(rating_list)
        print result[1]
        return result