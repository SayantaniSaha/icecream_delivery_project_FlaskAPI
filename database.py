from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine('postgresql://postgres:admin@localhost/icecream_delivery',
                       echo=True)

Base = declarative_base()

session = sessionmaker()
