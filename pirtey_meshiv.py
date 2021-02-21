from sqlalchemy import Column,String,DateTime,Numeric,Sequence,CLOB,ForeignKey
from sqlalchemy.orm import relationship,backref
from sqlalchemy.sql.expression import text

from base import Base

class PirteyMeshiv(Base):
    __tablename__='pirtey_meshiv'

    seq=Column(Numeric(precision=8,scale=0),Sequence('meshiv_seq'))

    mezahe_reshuma=Column(type_=Numeric(precision=8,scale=0),nullable=False,primary_key=True)#name='MEZAHE_RESHUMA',

    kod_seker=Column(Numeric(precision=6,scale=0),ForeignKey('kodey_skarim.kod_seker'))
    seker=relationship("KodeySkarim",backref=backref("kodey_skarim_pirtey_meshiv",uselist=False))

    mispar_ishi=Column(name='MISPAR_ISHI',type_=Numeric(precision=9,scale=0))
    teudat_zehut=Column(name='TEUDAT_ZEHUT',type_=Numeric(precision=9,scale=0))

    t_yetzira=Column(name='T_YETZIRA',type_=DateTime(timezone=True),nullable=False,server_default=text('SYSDATE'))
    t_miluy=Column(name='T_MILUY',type_=DateTime(timezone=True),nullable=False,server_default=text('SYSDATE'))

    mispar_maarich=Column(name='MISPAR_MAARICH',type_=Numeric(precision=9,scale=0))
    shem_maarich=Column(name='SHEM_MAARICH',type_=String(length=100),nullable=True)
    mail_maarich=Column(name='MAIL_MAARICH',type_=String(length=100),nullable=True)
    phone_maarich=Column(name='PHONE_MAARICH',type_=String(length=100),nullable=True)
    achuz_miluy=Column(name='ACHUZ_MILUY',type_=String(length=100),nullable=True)
    status=Column(name='STATUS',type_=String(length=100),nullable=True)
    amud_acharon_miluy=Column(name='AMUD_ACHARON_MILUY',type_=String(length=100),nullable=True)
    rechiv_maane=Column(name='RECHIV_MAANE',type_=String(length=100),nullable=True)

    c1=Column(name='C1',type_=String(length=100),nullable=True)
    c2=Column(name='C2',type_=String(length=100),nullable=True)
    c3=Column(name='C3',type_=String(length=100),nullable=True)
    c4=Column(name='C4',type_=String(length=100),nullable=True)
    c5=Column(name='C5',type_=String(length=100),nullable=True)
    c6=Column(name='C6',type_=String(length=100),nullable=True)
    c7=Column(name='C7',type_=String(length=100),nullable=True)
    c8=Column(name='C8',type_=String(length=100),nullable=True)
    c9=Column(name='C9',type_=String(length=100),nullable=True)
    c10=Column(name='C10',type_=String(length=100),nullable=True)

    ind_pail=Column(Numeric(precision=3,scale=0),ForeignKey('kodey_status.kod_status'),server_default=text('0'))
    pail=relationship("KodeyStatus",backref=backref("kodey_status_pirtey_meshiv",uselist=False))

    t_rishum=Column(name='T_RISHUM',type_=DateTime(timezone=True),nullable=False,server_default=text('SYSDATE'))

    def __init__(self,
                    seq=None,
                    mezahe_reshuma=None,
                    seker=None,
                    mispar_ishi=None,
                    teudat_zehut=None,
                    t_yetzira=None,
                    t_miluy=None,
                    mispar_maarich=None,
                    shem_maarich=None,
                    mail_maarich=None,
                    phone_maarich=None,
                    achuz_miluy=None,
                    status=None,
                    amud_acharon_miluy=None,
                    rechiv_maane=None,
                    c1=None,
                    c2=None,
                    c3=None,
                    c4=None,
                    c5=None,
                    c6=None,
                    c7=None,
                    c8=None,
                    c9=None,
                    c10=None,
                    pail=None,
                    t_rishum=None,):
        
        kodey_skarim_attr=['seq','mezahe_reshuma','seker','mispar_ishi','teudat_zehut','t_yetzira','t_miluy','mispar_maarich','shem_maarich','mail_maarich','phone_maarich','achuz_miluy','status','amud_acharon_miluy','rechiv_maane','c1','c2','c3','c4','c5','c6','c7','c8','c9','c10','pail','t_rishum']

        for attr in kodey_skarim_attr:
            if attr:
                exec(f'self.{attr}={attr}')