from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URL = "mysql://27.0.0.1:3306/test_db"

engine=create_engine(DB_URL)

Base=declarative_base()

SessionLocal=sessionmaker(autocommit=False,bind=engine)

