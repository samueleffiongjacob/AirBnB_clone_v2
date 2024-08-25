#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv


# if getenv("HBNB_TYPE_STORAGE") == "db":
#     storage = DBStorage()
# else:
#     storage = FileStorage()
# storage.reload()



storage_type = getenv("HBNB_TYPE_STORAGE")

if storage_type == "db":
    storage = DBStorage()
elif storage_type == "file":
    storage = FileStorage()
else:
    raise ValueError("Invalid HBNB_TYPE_STORAGE value. Must be 'db' or 'file'.")

storage.reload()
