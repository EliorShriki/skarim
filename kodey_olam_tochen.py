from sqlalchemy import Column,String,Numeric,Sequence,ForeignKey
from sqlalchemy.orm import relationship,backref
from sqlalchemy.sql.expression import text

from base import Base

class KodeyOlamTochen(Base):
    __tablename__='kodey_olam_tochen'

    kod_olam_tochen=Column(Numeric(precision=3,scale=0),Sequence('kod_olam_tochen_seq'),primary_key=True)
    shem_olam_tochen=Column(name='SHEM_OLAM_TOCHEN',type_=String(length=100),nullable=False,server_default='ללא עולם תוכן')

    ind_pail=Column(Numeric(precision=3,scale=0),ForeignKey('kodey_status.kod_status'),server_default=text('0'))
    pail=relationship("KodeyStatus",backref=backref("kodey_status_kodey_kodey_olam_tochen",uselist=False))

    def __init__(self,
                    kod_olam_tochen=None,
                    shem_olam_tochen=None,
                    pail=None):
        
        kodey_olam_tochen_attr=['kod_olam_tochen','shem_olam_tochen','pail']

        for attr in kodey_olam_tochen_attr:
            if attr:
                exec(f'self.{attr}={attr}')