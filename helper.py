from difflib import SequenceMatcher

def handle_semi_open(df):
    cols = df.columns.tolist()
    x = []
    for i in range(1,len(cols)):
        cols[i] = str(cols[i])
        if cols[i] == cols[i-1]:
            cols[i] = cols[i] + '_dup'
            x.append(cols[i-1])
    df.columns = cols
    for dup in x:
        to_drp = dup + '_dup'
        df[dup] = list(zip(df[dup].astype('str'),df[to_drp].astype('str')))
        df.drop(columns=to_drp, inplace=True)
    return df

def lcs(s1, s2):
    match = SequenceMatcher(None, s1, s2).find_longest_match(0, len(s1), 0, len(s2))
    return s1[match.a:match.a + match.size - 1]

def get_lcs_list(strings):
    val = strings[0]
    rest = iter(strings[1:-1])
    for s in rest:
        val = lcs(val, s)
    return val