from models import BxUsers
def add_user(user_id, city, state, country, age):
    
def select_user(user_id):
    return BxUsers.objects.get(user_id=user_id)