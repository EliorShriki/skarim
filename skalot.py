from sqlalchemy import Column,DateTime,Numeric,Sequence,CLOB,ForeignKey
from sqlalchemy.orm import relationship,backref
from sqlalchemy.sql.expression import text

from base import Base

class Skalot(Base):
    __tablename__='skalot'

    kod_skala=Column(Numeric(precision=6,scale=0),Sequence('kod_skala_seq'),primary_key=True)
    list_kodim=Column(name='LIST_KODIM',type_=CLOB())
    list_thuvot=Column(name='LIST_THUVOT',type_=CLOB())

    ind_pail=Column(Numeric(precision=3,scale=0),ForeignKey('kodey_status.kod_status'),server_default=text('0'))
    pail=relationship("KodeyStatus",backref=backref("kodey_status_skalot",uselist=False))

    t_rishum=Column(name='T_RISHUM',type_=DateTime(timezone=True),nullable=False,server_default=text('SYSDATE'))

    def __init__(self,
                    kod_skala=None,
                    list_kodim=None,
                    list_thuvot=None,
                    pail=None,
                    t_rishum=None):
        
        skalot_attr=['kod_skala','list_kodim','list_thuvot','pail','t_rishum']

        for attr in skalot_attr:
            if attr:
                exec(f'self.{attr}={attr}')