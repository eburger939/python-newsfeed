from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from flask import g

load_dotenv()

#connect to database using env variable
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
#handles the connection to the db
Session = sessionmaker(bind=engine)
#generates temporary connections for performing create, read, update, and delete operations
Base = declarative_base()
#helps map the models to real mysql tables

def init_db(app):
    Base.metadata.create_all(engine)
    app.teardown_appcontext(close_db)


#the function saves the current connect ont he g object if it is not already there..
# then it returns the connection form the g object instead of creating a new session
def get_db():
    if 'db' not in g:
        #store db connection in app context
        g.db = Session()
    
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()