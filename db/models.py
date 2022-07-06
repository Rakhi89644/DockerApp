from lib2to3.pytree import Base
from db.database import Base
from sqlalchemy import Column,Integer,String
#from sqlalchemy.types import String, Integer

class Users(Base):
        __tablename__="user"
        id=Column(Integer,primary_key=True,index=True)
        name=Column(String(50))
        email=Column(String(100),unique=True)
        password=Column(String(100))
