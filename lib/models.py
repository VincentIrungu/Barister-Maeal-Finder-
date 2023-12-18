from sqlalchemy import Column,Table, Integer, String, VARCHAR, INT, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref


Base = declarative_base()
meal_cards = Table(
    "meal_card",
    Base.metadata,
    Column('meal_card_id',Integer),
    Column('meal_served', VARCHAR(40)),
    Column('specifications', VARCHAR(40)),
    Column('satisfaction_rank', Integer),
    Column('comments', VARCHAR(40)),
    Column('barista_id',ForeignKey('baristas.barista_id')),
    Column('client_id',ForeignKey('clients.client_id')),
    extend_existing = True
)

class Baristas(Base):
    __tablename__ = 'baristas'

    barista_id = Column(Integer, primary_key=True)
    first_name = Column(VARCHAR(40))
    last_name = Column(VARCHAR(40))
    meal_served = Column(VARCHAR(40))
    age = Column(INT)

    served_client = relationship('Clients', backref = 'barista')
    client = relationship('Clients', secondary = meal_cards, back_populates ='barista')
    

    def __repr__(self):
        return f"Barista; {self.first_name} {self.last_name}"

class Clients(Base):
    __tablename__ = 'clients'
    
    client_id = Column(Integer, primary_key=True)
    first_name = Column(VARCHAR(40))
    last_name = Column(VARCHAR(40))
    meal_served = Column(VARCHAR(40))
    rank = Column(INT)
    barista_id = Column(INT, ForeignKey('baristas.barista_id'))

    meals = relationship('Baristas', secondary = meal_cards, back_populates = 'client')


    def __repr__(self):
        return f"Client:{self.first_name} {self.last_name}" 

engine = create_engine('sqlite:///parlor.db')

Session = sessionmaker(bind=engine)

session = Session()
# Base.metadata.create_all(bind=engine) """ 


