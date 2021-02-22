from datetime import date

from base import Session,engine,Base
from kodey_status import KodeyStatus 
from kodey_sug_shela import KodeySugShela
from kodey_olam_tochen import KodeyOlamTochen
from kodey_uchlusia import KodeyUchlusia
from kodey_skarim import KodeySkarim
from shelot import Shelot
from skalot import Skalot  

from pirtey_meshiv import PirteyMeshiv
from tshuvot import Tshuvot

from time import perf_counter 

def insert():
    # Start the stopwatch / counter 
    t_start = perf_counter() 

    # Generate DB schema
    Base.metadata.create_all(engine)

    # Create a new session
    session=Session()

    status_pail=KodeyStatus(shem_status='פעיל')
    status_lo_pail=KodeyStatus(shem_status='לא פעיל')

    shela_regila=KodeySugShela(shem_sug='שאלה רגילה')
    shela_semi_ptucha=KodeySugShela(shem_sug='שאלה חצי פתוחה')
    shela_ptucha=KodeySugShela(shem_sug='שאלה פתוחה')
    shela_rav_brera=KodeySugShela(shem_sug='שאלת רב ברירה')

    uc_keva=KodeyUchlusia(shem_uchlsia='קבע')
    uc_chova=KodeyUchlusia(shem_uchlsia='חובה')

    olam_keva=KodeyOlamTochen(shem_olam_tochen='עולם קבע')
    olam_chova=KodeyOlamTochen(shem_olam_tochen='עולם חובה')

    sekarim_list=[]

    for s in range(10):
        sekarim_list.append(
            KodeySkarim(\
                # kod_seker=,
                uchlusia=uc_keva,
                shem_seker=f'סקר בדיקה מספר {s}',
                orech_seker=s,
                kamut_meshivim=s*10,
                moed_seker='זמן מסויים',
                shnat_seker='2020',
                hearot='כאן ייכתבו הערות על הסקר. לרוב לא מעניין אף אחד'
            )     
        )    

    skala_1=Skalot(\
        list_kodim='1 # 2 # 3 # 4 # 5', 
        list_thuvot='במידה רבה מאוד # במידה רבה # במידה מועטה # במידה מועטה מאוד # ללא תשובה', 
        pail=status_pail
    )
    shela=Shelot(seker=sekarim_list[0],mezahe_shela='4.5', melel_shela='בדיקה בדיקה 1 2', sug_shela=shela_regila, skala=skala_1)
    # Create Uchlusiyot
    # uchlusia_Chova=KodeyUchlusia(shem_uchlsia='חובה') 
    # uchlusia_keva=KodeyUchlusia(shem_uchlsia='קבע') 
    # uchlusia_atz=KodeyUchlusia(shem_uchlsia='אעצ') 

    # Create surveys
    # dummy_survey1=KodeySekarim(
    #                             uchlusia=uchlusia_Chova,
    #                             shem_seker='',
    #                             orech_seker=33,
    #                             kamut_meshivim=4,
    #                             hearot=10000*'blat '
    # )

    session.add_all([status_pail,status_lo_pail])    
    session.add_all([shela_regila,shela_semi_ptucha,shela_ptucha,shela_rav_brera])    
    session.add_all([shela_regila,shela_semi_ptucha,shela_ptucha,shela_rav_brera])    
    session.add_all([uc_keva,uc_chova])    
    session.add_all([olam_keva,olam_chova])    
    session.add_all(sekarim_list)    
    session.add_all([skala_1])    
    session.add_all([shela])    

    session.commit()
    session.close()

    # Stop the stopwatch / counter 
    t_stop = perf_counter() 

    print(f'Total time is: {t_stop-t_start}')

def query():
    # Create a new session
    session=Session()

    # shelot=session.query(Shelot).all()

    # print(f'\n### All shelot:')
    
    # for s in shelot:
    #     print(f'{s.seq} is {s.melel_shela')

def inspector():
    from sqlalchemy import inspect

    # engine = create_engine("oracle+cx_oracle://s:t@dsn")
    inspector = inspect(engine)
    all_check_constraints = inspector.get_check_constraints(
        "shelot", include_all=True)  
    print(all_check_constraints)     

    all_tables=all_check_constraints = inspector.get_table_names()
    print(all_tables)     

def query():
    session=Session()

    temp=session.query(Shelot).filter(Shelot.kod_shela == 1)

    for sh in temp:
        print(f'{sh}')

# insert()

# inspector()

query()