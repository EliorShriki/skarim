from sqlalchemy import Column,String,DateTime,Numeric,Sequence, CLOB, ForeignKey
from sqlalchemy.orm import relationship,backref
from sqlalchemy.sql.expression import text

from base import Base

class Tshuvot(Base):
    __tablename__='tshuvot'

    mezahe_reshuma=Column(Numeric(precision=8,scale=0),ForeignKey('pirtey_meshiv.mezahe_reshuma'))
    mezahe=relationship("PirteyMeshiv",backref=backref("pirtey_meshiv_tshuvot",uselist=False))

    kod_seker=Column(Numeric(precision=6,scale=0),ForeignKey('kodey_skarim.kod_seker'))
    seker=relationship("KodeySkarim",backref=backref("kodey_skarim_tshuvot",uselist=False))

    kod_tshuva=Column(Numeric(precision=10,scale=0),Sequence('kod_tshuva_seq'),primary_key=True)

    melel_tshuva=Column(name='MELEL_TSHUVA',type_=CLOB())
    ind_free_text=Column(Numeric(precision=1,scale=0),nullable=False,server_default=text('0'))

    ind_pail=Column(Numeric(precision=3,scale=0),ForeignKey('kodey_status.kod_status'),server_default=text('0'))
    pail=relationship("KodeyStatus",backref=backref("kodey_status_tshuvot",uselist=False))

    t_rishum=Column(name='T_RISHUM',type_=DateTime(timezone=True),nullable=False,server_default=text('SYSDATE'))

    def __init__(self,
                    mezahe=None,
                    seker=None,
                    kod_tshuva=None,
                    melel_tshuva=None,
                    ind_free_text=None,
                    t_rishum=None):
        
        tshuvot_attr=['mezahe','seker','kod_tshuva','melel_tshuva','ind_free_text','pail','t_rishum']

        for attr in tshuvot_attr:
            if attr:
                exec(f'self.{attr}={attr}')