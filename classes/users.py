from peewee import CharField, TextField
from peewee_setup import BaseModel, db


class Users(BaseModel):
    user_id = CharField(primary_key=True)
    user_name = CharField()
    profile_pic_url = TextField()
    auth_token = TextField(null=True)


db.create_tables([Users])


# Get a user as dict by id
# Args: user_id (string/int of user_id)
# Return: User as dictionary if found, None if not found
def get_user(user_id):
    try:
        user_array = Users.select().where(
            Users.user_id == user_id).limit(1).dicts().execute()
        return user_array[0]
    # in case of user not found or incorrect parameter user_id
    except:
        return None

# Create a user with provided fields
# Args: User_fields (dictionary- key = field, value = field_value)
# Return: Number of rows created, -1 if error


def create_user(user_field_mappings):
    # try:
    return Users.insert(**user_field_mappings).execute()
    # in case of incorrect user field mapping
    # except:
    #     return -1


# Updates user using field_mapping
# Args: user_id (string/int of user_id), User_fields (dictionary- key = field, value = field_value)
# Return: Number of rows updated, -1 if error
def update_user(user_id, user_field_mappings):
    # try:
    return Users.update(**user_field_mappings).where(Users.user_id == user_id).execute()
    # in case of incorrect user field mapping

    # except:
    #     return -1

# Deletes a user using id
# Args: user_id (string/int of user_id)
# Return: Number of rows deleted


def delete_user(user_id):
    return Users.delete().where(Users.user_id == user_id).execute()
