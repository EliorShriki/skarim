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