from models import BxUsers
def add_user(ins_user_id, ins_city, ins_state, ins_country, ins_age):
    insert_user = BxUsers(user_id = int(ins_user_id), city=ins_city.lower(), country = ins_county.lower(), age = ins_age)

def select_user(sel_user_id):
    return BxUsers.objects.get(user_id=sel_user_id)