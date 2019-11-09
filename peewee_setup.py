from config import Config
from peewee import PostgresqlDatabase, Model

### SETUP peewee

# Initialize db_helper with Peewee; static variable
db = PostgresqlDatabase(
    Config.DATABASE,
    user=Config.USERNAME,
    password=Config.PASSWORD,
    host=Config.HOST,
    port=Config.PORT,
)

db.connect()

# BaseModel needed for Peewee ORM models and connect to db_helper for all Pra.select() and other db calls
class BaseModel(Model):
    class Meta:
        database = db
