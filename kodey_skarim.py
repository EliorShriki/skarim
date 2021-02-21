from sqlalchemy import Column,String,DateTime,Numeric,Sequence,CLOB,ForeignKey
from sqlalchemy.orm import relationship,backref
from sqlalchemy.sql.expression import text

from base import Base

class KodeySkarim(Base):
    __tablename__='kodey_skarim'

    kod_seker=Column(Numeric(precision=6,scale=0),Sequence('kod_seker_seq'),primary_key=True)

    kod_uchlusia=Column(Numeric(precision=3,scale=0),ForeignKey('kodey_uchlusia.kod_uchlusia'))
    uchlusia=relationship("KodeyUchlusia",backref=backref("kodey_uchlusia_kodey_skarim",uselist=False))

    kod_olam_tochen=Column(Numeric(precision=3,scale=0),ForeignKey('kodey_olam_tochen.kod_olam_tochen'))
    olam_tochen=relationship("KodeyOlamTochen",backref=backref("kodey_olam_tochen_kodey_skarim",uselist=False))

    shem_seker=Column(name='SHEM_SEKER',type_=String(length=100),nullable=False,server_default='סקר ללא שם')
    orech_seker=Column(name='ORECH_SEKER',type_=Numeric(precision=4,scale=0))
    kamut_meshivim=Column(name='KAMUT_MESHIVIM',type_=Numeric(precision=6,scale=0))
    moed_seker=Column(name='MOED_SEKER',type_=String(length=50),nullable=False,server_default='9999')
    shnat_seker=Column(name='SHNAT_SEKER',type_=String(length=4),nullable=False,server_default='9999')
    hearot=Column(name='HEAROT',type_=CLOB())
    t_idkun=Column(name='T_IDKUN',type_=DateTime(timezone=True),nullable=False,server_default=text('SYSDATE'))
    updated_by=Column(name='UPDATED_BY',type_=String(length=100),nullable=False,server_default='NONE')

    ind_pail=Column(Numeric(precision=3,scale=0),ForeignKey('kodey_status.kod_status'),server_default=text('0'))
    pail=relationship("KodeyStatus",backref=backref("kodey_status_kodey_kodey_skarim",uselist=False))

    t_rishum=Column(name='T_RISHUM',type_=DateTime(timezone=True),nullable=False,server_default=text('SYSDATE'))

    def __init__(self,
                    kod_seker=None,
                    uchlusia=None,
                    olam_tochen=None,
                    shem_seker=None,
                    orech_seker=None,
                    kamut_meshivim=None,
                    moed_seker=None,
                    shnat_seker=None,
                    hearot=None,
                    t_idkun=None,
                    updated_by=None,
                    pail=None,
                    t_rishum=None):
        
        kodey_skarim_attr=['kod_seker','uchlusia','olam_tochen','shem_seker','orech_seker','kamut_meshivim','moed_seker','shnat_seker','hearot','t_idkun','updated_by','pail','t_rishum']

        for attr in kodey_skarim_attr:
            if attr:
                exec(f'self.{attr}={attr}')