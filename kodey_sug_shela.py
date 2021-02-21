from sqlalchemy import Column,String,Numeric,Sequence,ForeignKey
from sqlalchemy.orm import relationship,backref

from sqlalchemy.sql.expression import text

from base import Base

class KodeySugShela(Base):
    __tablename__='kodey_sug_shela'

    kod_sug=Column(Numeric(precision=2,scale=0),Sequence('kod_sug_shela_seq'),primary_key=True)
    shem_sug=Column(name='SHEM_SUG',type_=String(length=50),nullable=False,server_default='ללא סוג')
    
    ind_pail=Column(Numeric(precision=3,scale=0),ForeignKey('kodey_status.kod_status'),server_default=text('0'))
    pail=relationship("KodeyStatus",backref=backref("kodey_status_kodey_sug_shela",uselist=False))

    def __init__(self,
                    kod_sug=None,
                    shem_sug=None,
                    pail=None):
        
        kodey_sug_shela_attr=['kod_sug','shem_sug','pail']

        for attr in kodey_sug_shela_attr:
            if attr:
                exec(f'self.{attr}={attr}')