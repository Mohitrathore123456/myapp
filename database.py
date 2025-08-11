from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Use pymysql in URL
engine = create_engine("mysql+pymysql://root:mohitrathore@localhost/myapp")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
