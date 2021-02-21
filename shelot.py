from sqlalchemy import Column,String,DateTime,Numeric,Sequence,ForeignKey,Index,UniqueConstraint
from sqlalchemy.orm import relationship,backref
from sqlalchemy.sql.expression import text

from base import Base

class Shelot(Base):
    __tablename__='shelot'
    # __table_args__ = (
        # UniqueConstraint('kod_seker','mezahe_shela'), 
    #     # Index('myindex', 'kod_seker','mezahe_shela', unique=True),
    # )

    kod_seker=Column(Numeric(precision=6,scale=0),ForeignKey('kodey_skarim.kod_seker'), comment='test comment')
    seker=relationship("KodeySkarim",backref=backref("kodey_skarim_shelot",uselist=False))

    kod_shela=Column(Numeric(precision=6,scale=0),Sequence('kod_shela_seq'),primary_key=True)

    mezahe_shela=Column(name='MEZAHE_SHELA',type_=String(length=10),nullable=False)
    melel_shela=Column(name='MELEL_SHELA',type_=String(length=500),nullable=False)

    kod_sug_shela=Column(Numeric(precision=2,scale=0),ForeignKey('kodey_sug_shela.kod_sug'))
    sug_shela=relationship("KodeySugShela",backref=backref("kodey_sug_shela_shelot",uselist=False))

    kod_skala=Column(Numeric(precision=6,scale=0),ForeignKey('skalot.kod_skala'))
    skala=relationship("Skalot",backref=backref("skalot_shelot",uselist=False))

    # UniqueConstraint('kod_seker','mezahe_shela',name='uix_1')
    # Index('kod_seker', 'mezahe_shela', name="some_index", unique=False)

    t_rishum=Column(name='T_RISHUM',type_=DateTime(timezone=True),nullable=False,server_default=text('SYSDATE'))

    def __init__(self,
                    seker=None,
                    kod_shela=None,
                    mezahe_shela=None,
                    melel_shela=None,
                    sug_shela=None,
                    skala=None,
                    t_rishum=None):
        
        shelot_attr=['seker','kod_shela','mezahe_shela','melel_shela','sug_shela','skala','t_rishum']

        for attr in shelot_attr:
            if attr:
                exec(f'self.{attr}={attr}')

UniqueConstraint(None, Shelot.kod_seker, Shelot.mezahe_shela)                