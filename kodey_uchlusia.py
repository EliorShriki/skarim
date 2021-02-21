from sqlalchemy import Column,String,Numeric,CLOB,Sequence,ForeignKey
from sqlalchemy.orm import relationship,backref

from sqlalchemy.sql.expression import text

from base import Base

class KodeyUchlusia(Base):
    __tablename__='kodey_uchlusia'

    kod_uchlusia=Column(Numeric(precision=3,scale=0),Sequence('kod_uchlusia_seq'),primary_key=True)
    shem_uchlsia=Column(name='SHEM_UCHLUSIA',type_=String(length=100),nullable=False,server_default='ללא אוכלוסיה')

    ind_pail=Column(Numeric(precision=3,scale=0),ForeignKey('kodey_status.kod_status'),server_default=text('0'))
    pail=relationship("KodeyStatus",backref=backref("kodey_status_kodey_uchlusia",uselist=False))

    def __init__(self,
                    kod_uchlusia=None,
                    shem_uchlsia=None,
                    pail=None):
        
        kodey_uchlusia_attr=['kod_uchlusia','shem_uchlsia','pail']

        for attr in kodey_uchlusia_attr:
            if attr:
                exec(f'self.{attr}={attr}')