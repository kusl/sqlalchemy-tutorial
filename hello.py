from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import logging 
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    logging.basicConfig(filename='example.log', level=logging.DEBUG)
    logging.debug('Hello from the instantiation of User class')
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        logging.info('no we are __repr__ esenting usa')
        return "<User(name='%s', fullname='%s', password='%s')>" % (
            self.name, self.fullname, self.password)
