#!/usr/bin/python3
""" new class for sqlAlchemy """
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine  #(create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity






# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, scoped_session
# from models.base_model import Base
# from models.state import State
# from models.city import City
# from models.user import User
# from models.place import Place
# from models.review import Review
# from models.amenity import Amenity
# from os import getenv

class DBStorage:
    """Create tables in the environment"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{passwd}@{host}/{db}', 
            pool_pre_ping=True
        )

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of all objects of a given class"""
        dic = {}
        classes = {
            'State': State,
            'City': City,
            'User': User,
            'Place': Place,
            'Review': Review,
            'Amenity': Amenity
        }

        if cls:
            if isinstance(cls, str):
                cls = classes.get(cls)
            if cls:
                query = self.__session.query(cls)
                for elem in query:
                    key = f"{type(elem).__name__}.{elem.id}"
                    dic[key] = elem
        else:
            for clase in classes.values():
                query = self.__session.query(clase)
                for elem in query:
                    key = f"{type(elem).__name__}.{elem.id}"
                    dic[key] = elem
        return dic

    def new(self, obj):
        """Adds a new element to the table"""
        self.__session.add(obj)

    def save(self):
        """Commits changes to the database"""
        try:
            self.__session.commit()
        except Exception as e:
            self.__session.rollback()
            raise e

    def delete(self, obj=None):
        """Deletes an element from the table"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Configures and initializes the database"""
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """Closes the session"""
        if self.__session:
            self.__session.remove()  # Use remove() to handle scoped sessions

# class DBStorage:
#     """ create tables in environmental"""
#     __engine = None
#     __session = None

#     def __init__(self):
#         user = getenv("HBNB_MYSQL_USER")
#         passwd = getenv("HBNB_MYSQL_PWD")
#         db = getenv("HBNB_MYSQL_DB")
#         host = getenv("HBNB_MYSQL_HOST")
#         env = getenv("HBNB_ENV")

#         self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
#                                       .format(user, passwd, host, db),
#                                       pool_pre_ping=True)

#         if env == "test":
#             Base.metadata.drop_all(self.__engine)

#     def all(self, cls=None):
#         """returns a dictionary
#         Return:
#             returns a dictionary of __object
#         """
#         dic = {}
#         if cls:
#             if type(cls) is str:
#                 cls = eval(cls)
#             query = self.__session.query(cls)
#             for elem in query:
#                 key = "{}.{}".format(type(elem).__name__, elem.id)
#                 dic[key] = elem
#         else:
#             lista = [State, City, User, Place, Review, Amenity]
#             for clase in lista:
#                 query = self.__session.query(clase)
#                 for elem in query:
#                     key = "{}.{}".format(type(elem).__name__, elem.id)
#                     dic[key] = elem
#         return (dic)

#     def new(self, obj):
#         """add a new element in the table
#         """
#         self.__session.add(obj)

#     def save(self):
#         """save changes
#         """
#         self.__session.commit()

#     def delete(self, obj=None):
#         """delete an element in the table
#         """
#         if obj:
#             self.session.delete(obj)

#     def reload(self):
#         """configuration
#         """
#         Base.metadata.create_all(self.__engine)
#         sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
#         Session = scoped_session(sec)
#         self.__session = Session()

#     def close(self):
#         """ calls remove()
#         """
#         self.__session.close()
