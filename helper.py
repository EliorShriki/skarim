from difflib import SequenceMatcher
import pandas as pd

def load_frames(kod_path, label_path):
    """
    Load Frames:
        Arguments: 
            - kod_path (Str): the path to the kod file of the survey.
            - label_path (Str): the path to the label file of the survey.
    
        Returns:
            - data (Panda's DataFrame): contains a merged data frame from the kod and label files.
                * Index: Mezahe_Reshuma.
                * Columns: Mezahe_Sheela for each question in kod and label with the suffix '_kod'/'_label' according to the file it's taken from.
            
            - questions_df (Panda's DataFrame): contains each question, it's id and it's description.
                * Index: Mezahe_Sheela.
                * Columns: Mezahe_Sheela, Shem_Sheela, Kod_Sug_Sheela, Kod_Skala.
            
            - semi_open (List): List of all the questions that are semi open.
    """
    kod_file = pd.read_excel(kod_path)
    label_file = pd.read_excel(label_path)
    kod_file.set_index(keys=kod_file.columns[0], drop=True, inplace=True)
    label_file.set_index(keys=label_file.columns[0], drop=True, inplace=True)

    q_names = kod_file.columns.tolist()
    q_mezahe = kod_file.iloc[0]
    questions = list(zip(q_names, q_mezahe))

    questions_df = pd.DataFrame(questions, columns=['shem_sheela','mezahe_sheela'])
    questions_df = questions_df[questions_df['mezahe_sheela'].isnull() == False] # fetch just the actual questions (minus the meta data of the seker).
    questions_df.set_index(keys=questions_df.columns[1], drop=False, inplace=True) # set the index as mezahe_sheela.
    questions_df['kod_sug_sheela'] = 1 # all the questions start as regular question until handled according their actual type.
    questions_df['kod_skala'] = 0 # all questions have a default kod_skala as 0

    kod_df = kod_file[questions_df['shem_sheela']]
    kod_df.columns = kod_df.iloc[0].tolist()
    kod_df.drop(index=kod_df.index[0], inplace=True) # set the index to mezahe_reshuma (equivalent to mispar_ishi).

    label_df = label_file[questions_df['shem_sheela']]
    label_df.columns = label_df.iloc[0].tolist()
    label_df.drop(index=label_df.index[0], inplace=True) # set the index to mezahe_reshuma (equivalent to mispar_ishi).

    questions_df, semi_open = handle_semi_open_questions(questions_df) 
    kod_df = handle_semi_open_tshuvut(kod_df)
    label_df = handle_semi_open_tshuvut(label_df)

    data = pd.merge(kod_df, label_df, on=kod_df.index, how='inner', suffixes=('_kod', '_label')) # join the label and kod dfs.
    data.set_index(keys=data.columns[1], drop=False, inplace=True) # set the index to mezahe_reshuma (equivalent to mispar_ishi).

    return data, questions_df, semi_open

def handle_semi_open_tshuvut(t_df):
    """
    Handle Semi Open Tshuvut:
        Arguments: 
            - t_df (Panda's DataFrame): A DataFrame that contains an answer to a question in each row.
                * Index: Mezahe_Reshuma.
                * Columns: Mezahe_Sheela for each question in kod
    
        Returns:
            - t_df (Panda's DataFrame): A DataFrame that contains an answer to a question in each row. (After handeling semi open answers)
                * Index: Mezahe_Reshuma.
                * Columns: Mezahe_Sheela for each question in label

    """
    # loop over each questions, if the questions id is the same as the previous one, it is a semi open question.
    # combine both columns into one that contains a tuple of both values.
    # deletes the dulpicate columns.
    cols = t_df.columns.tolist()
    x = []
    for i in range(1,len(cols)):
        cols[i] = str(cols[i])
        if cols[i] == cols[i-1]:
            cols[i] = cols[i] + '_dup'
            x.append(cols[i-1])
    t_df.columns = cols
    for dup in x:
        to_drp = dup + '_dup'
        t_df[dup] = list(zip(t_df[dup].astype('str'),t_df[to_drp].astype('str')))
        t_df.drop(columns=to_drp, inplace=True)
    return t_df

def handle_semi_open_questions(q_df):
    """
    Handle Semi Open Questions:
        Arguments: 
            - q_df (Panda's DataFrame): contains each question, it's id and it's description.
                * Index: Mezahe_Sheela.
                * Columns: Mezahe_Sheela, Shem_Sheela, Kod_Sug_Sheela, Kod_Skala.
    
        Returns:
            - q_df (Panda's DataFrame): contains each question, it's id and it's description.
                * Index: Mezahe_Sheela.
                * Columns: Mezahe_Sheela, Shem_Sheela, Kod_Sug_Sheela, Kod_Skala.
            
            - semi_open (List): A list of all the semi open questions.

    """
    # loop over each questions, if the questions id is the same as the previous one, it is a semi open question.
    # unite both columns into one that represent the actual questions.
    # deletes the dulpicate columns.
    idxs = q_df.index.tolist()
    semi_open = []
    for i in range(1,len(idxs)):
        idxs[i] = str(idxs[i])
        if idxs[i] == idxs[i-1]:
            idxs[i] = idxs[i] + '_dup'
            semi_open.append(idxs[i-1])

    q_df.index = idxs
    for dup in semi_open:
        to_drp = dup + '_dup'
        q_df.drop(index=to_drp, inplace=True)

    return q_df, semi_open

def lcs(s1, s2):
    match = SequenceMatcher(None, s1, s2).find_longest_match(0, len(s1), 0, len(s2))
    return s1[match.a:match.a + match.size - 1]

def get_lcs_list(strings):
    val = strings[0]
    rest = iter(strings[1:-1])
    for s in rest:
        val = lcs(val, s)
    return val

def create_tshuvot(df, questions_df, semi_open):
    """
    Load Frames:
        Arguments: 
            - df (Panda's DataFrame): contains a merged data frame from the kod and label files.
                * Index: Mezahe_Reshuma.
                * Columns: Mezahe_Sheela for each question in kod and label with the suffix '_kod'/'_label' according to the file it's taken from.
            
            - questions_df (Panda's DataFrame): contains each question, it's id and it's description.
                * Index: Mezahe_Sheela.
                * Columns: Mezahe_Sheela, Shem_Sheela, Kod_Sug_Sheela, Kod_Skala.
            
            - semi_open (List): List of all the questions that are semi open.
        
        Returns:
            - tshuvot (Panda's DataFrame): contains a DataFrame of all the questions and the answers for each paticipant in the survey.
                * Index: Mezahe_Reshuma, Mezahe_Sheela.
                * Columns: Mezahe_Reshuma, Mezahe_Sheela, Kod_Tshuva, Shem_Tshuva, Ind_Free_Text.

            - questions_df (Panda's DataFrame): contains each question, it's id and it's description.
                * Index: Mezahe_Sheela.
                * Columns: Mezahe_Sheela, Shem_Sheela, Kod_Sug_Sheela, Kod_Skala.
    """
    frames = []
    for q in questions_df.index.to_list():
        temp_df = df[['key_0', str(q) + '_kod', str(q) + '_label']]
        temp_df['mezahe_sheela'] = q
        temp_df.columns = ['mezahe_reshuma', 'kod_tshuva', 'shem_tshuva', 'mezahe_sheela']
        frames.append(temp_df)

    tshuvot = pd.concat(frames)
    tshuvot.set_index(keys=['mezahe_reshuma', 'mezahe_sheela'], drop=False, inplace=True)
    tshuvot['ind_free_text'] = 0

    tshuvot, questions_df = handle_all_tshuvot(tshuvot, questions_df, semi_open)

    return tshuvot, questions_df

def handle_tshuvot_ptuchut(sheelot_ptuchut, tshuvot_df, questions_df):
    open_q = []
    for p in sheelot_ptuchut:
        df = tshuvot_df.query(f"mezahe_sheela == '{p}'")
        df['kod_tshuva'] = range(len(df['kod_tshuva'].tolist()))
        df['ind_free_text'] = 1
        questions_df['kod_sug_sheela'][p] = 3
        open_q.append(df)
    open_q_df = pd.concat(open_q)
    return open_q_df, questions_df

def handle_tshuvot_semi_ptuchut(semi_open, tshuvot_df, questions_df):
    semi_q = []
    for s in semi_open:
        df = tshuvot_df.query(f"mezahe_sheela == '{s}'")
        df['kod_tshuva'] = [tshu[0] for tshu in df['kod_tshuva'].tolist()]
        ans = [(tshu[1] if tshu[1] != 'nan' else tshu[0], 1 if tshu[1] != 'nan' else 0) for tshu in df['shem_tshuva'].tolist()]
        tshu_list = [x[0] for x in ans]
        ind_list = [x[1] for x in ans]
        df['ind_free_text'] = ind_list
        df['shem_tshuva'] = tshu_list
        questions_df['kod_sug_sheela'][s] = 4
        semi_q.append(df)
    semi_q_df = pd.concat(semi_q)
    return semi_q_df, questions_df

def helper_rav_briera(sheelot_rav_breira, questions_df):
    rav = {}
    sheelot_rav = {}
    sheelot_tshuvut = {}

    for r in sheelot_rav_breira:
        sheelat_av = '.'.join(r.split('.')[0:2])
        if sheelat_av not in rav:
            rav[sheelat_av] = []
        rav[sheelat_av].append(r)

    for sheelat_av,sheelot in rav.items():
        shemot = []
        for sh in sheelot:
            shemot.append(questions_df['shem_sheela'][sh])
        sheelot_rav[sheelat_av] = get_lcs_list(shemot)

    for r in sheelot_rav_breira:
        shem_s = questions_df['shem_sheela'][r]
        sheelat_av = '.'.join(r.split('.')[0:2])
        sheela_beemet = sheelot_rav[sheelat_av]
        tshuva = shem_s.replace(sheela_beemet, '')
        sheelot_tshuvut[r] = tshuva
    
    return rav, sheelot_rav, sheelot_tshuvut

def handle_tshuvot_rav_briera(sheelot_rav_breira, tshuvot_df, questions_df):
    rav, sheelot_rav, sheelot_tshuvut = helper_rav_briera(sheelot_rav_breira, questions_df)
    
    sheelot_av = []
    for sheelat_av,sheelot in rav.items():
        questions_df.drop(sheelot,inplace=True)
        sheelot_av.append((sheelot_rav[sheelat_av], sheelat_av, 2, 0))

    sheelot_av_df = pd.DataFrame(sheelot_av, columns=['shem_sheela','mezahe_sheela','kod_sug_sheela','kod_skala'],)
    sheelot_av_df.set_index(keys='mezahe_sheela', drop=False, inplace=True)

    questions_df = pd.concat([questions_df, sheelot_av_df])
    questions_df.reset_index(inplace=True, drop=True)

    rav_q = []
    idx_to_drp = []
    for sheelat_av,sheelot in rav.items():
        temp_df = tshuvot_df[tshuvot_df['mezahe_sheela'].isin(sheelot)]
        # tshuvot_df.drop(index=temp_df.index.tolist(), inplace=True)
        idx_to_drp.extend(temp_df.index.tolist())
        temp_idx = temp_df[temp_df['kod_tshuva'] == 0].index.tolist()
        temp_df.drop(index=temp_idx, inplace=True)
        temp_df['kod_tshuva'] = [x.split('.')[2] for x in temp_df['mezahe_sheela'].tolist()]
        temp_df['shem_tshuva'] = [sheelot_tshuvut[x] for x in temp_df['mezahe_sheela'].tolist()]
        temp_df['mezahe_sheela'] = sheelat_av
        temp_df.reset_index(inplace=True, drop=True)
        temp_df.set_index(keys=['mezahe_reshuma', 'mezahe_sheela'], inplace=True, drop=False)
        rav_q.append(temp_df)

    rav_q_df = pd.concat(rav_q)
    return rav_q_df, questions_df, idx_to_drp

def handle_all_tshuvot(tshuvot_df, questions_df, semi_open):
    sheelot_ptuchut = tshuvot_df[tshuvot_df['kod_tshuva'] == tshuvot_df['shem_tshuva']]['mezahe_sheela'].unique().tolist()
    sheelot_rav_breira = [x for x in tshuvot_df['mezahe_sheela'].unique().tolist() if len(str(x).split('.')) == 3]

    open_q_df, questions_df = handle_tshuvot_ptuchut(sheelot_ptuchut, tshuvot_df, questions_df)
    semi_q_df, questions_df = handle_tshuvot_semi_ptuchut(semi_open, tshuvot_df, questions_df)
    rav_q_df, questions_df, idx_to_drp = handle_tshuvot_rav_briera(sheelot_rav_breira, tshuvot_df, questions_df)

    tshuvot_df.drop(index=idx_to_drp,inplace=True)
    tshuvot_df.drop(index=open_q_df.index.tolist(),inplace=True)
    tshuvot_df.drop(index=semi_q_df.index.tolist(),inplace=True)

    tshuvot_df = pd.concat([tshuvot_df, open_q_df, semi_q_df, rav_q_df])
    tshuvot_df.sort_index(inplace=True)

    return tshuvot_df, questions_df