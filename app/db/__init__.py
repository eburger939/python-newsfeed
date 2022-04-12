from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

#connect to database using env variable
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
#handles the connection to the db
Session = sessionmaker(bind=engine)
#generates temporary connections for performing create, read, update, and delete operations
Base = declarative_base()
#helps map the models to real mysql tables