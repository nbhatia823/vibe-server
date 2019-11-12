from peewee import CharField, DecimalField
from peewee_setup import BaseModel, db

class User(BaseModel):
    user_id = CharField(primary_key=True)
    user_name = CharField()
    profile_pic_url = CharField()
    sentiment_score = DecimalField()
    auth_token = CharField(null=True)

db.create_tables([User])


# Get a user as dict by id
# Args: user_id (string/int of user_id)
# Return: User as dictionary if found, None if not found
def get_user(id):
    try:
        user_array = User.select().where(User.id == user_id).limit(1).dicts().execute()
        return user_array[0]
    # in case of user not found or incorrect parameter user_id
    except:
        return None

# Create a user with provided fields
# Args: User_fields (dictionary- key = field, value = field_value)
# Return: Number of rows created, -1 if error
def create_user(user_fields):
    try:
        return User.insert(**user_fields).execute()
    # in case of incorrect user field mapping
    except:
        return -1 


# Updates user using field_mapping
# Args: user_id (string/int of user_id), User_fields (dictionary- key = field, value = field_value)
# Return: Number of rows updated, -1 if error
def update_user(user_id, user_fields):
    try:
        return User.update(**field_mapping).where(User.user_id == user_id).execute()
    # in case of incorrect user field mapping
    except:
        return -1

# Deletes a user using id
# Args: user_id (string/int of user_id)
# Return: Number of rows deleted
def delete_user(user_id):
    return User.delete().where(User.user_id == user_id).execute()

