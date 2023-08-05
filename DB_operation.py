from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///clients.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)

Base.metadate.creat_all(engine)

def get_client_data(client_id):
    session = Session()
    client_data = session.query(Client).filter_by(id=client_id).first()
    session.close()

    if client_data:
        return {
            "id": client_data.id,
            "name": client_data.name,
            "email": client_data.email,
            "phone": client_data.phone
        }
    else:
        return None
    

def add_client_data(name, email, phone):
    session = Session()
    new_client = Client(name=name, email=email, phone=phone)
    session.add(new_client)
    session.commit()
    client_id = new_client.id
    session.close()

    return client_id 