from pipline.model import Database,db
from pipline.config import URL,DATABASE_DEBUG

db.drop_all()
db.create_all()