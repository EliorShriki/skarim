from sqlalchemy import Column,String,Numeric,Sequence
from sqlalchemy.sql.expression import text

from base import Base

class KodeyStatus(Base):
    __tablename__='kodey_status'

    kod_status=Column(Numeric(precision=3,scale=0),Sequence(name='kod_status_seq',start=0, minvalue=0),primary_key=True)
    shem_status=Column(name='SHEM_STATUS',type_=String(length=100),nullable=False,server_default='ללא סטטוס')

    def __init__(self,
                    kod_status=None,
                    shem_status=None):
        
        kodey_status_attr=['kod_status','shem_status']

        for attr in kodey_status_attr:
            if attr:
                exec(f'self.{attr}={attr}')