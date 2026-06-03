from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Gunakan database yang sudah Anda buat
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost:3306/database"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True  # Set to False in production
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()