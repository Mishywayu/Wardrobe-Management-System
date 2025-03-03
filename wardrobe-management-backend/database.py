from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# MySQL DB URL
DATABASE_URL = "mysql+pymysql://root:Sa%24%24yMi%24%24y%40254@localhost/wardrobe_db"

# CREATE DB ENGINE
engine = create_engine(DATABASE_URL)

# CREATE SessionLocal class to interact with the DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# base class for defining models
Base = declarative_base()

# dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.closed()