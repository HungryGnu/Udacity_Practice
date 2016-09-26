import pandas

def get_hourly_entries(df):
    df['ENTRIESn_hourly']=df.ENTRIESn-df.ENTRIESn.shift(1)
    df=df.fillna(1)
    return df


def get_hourly_exits(df):
    df['EXITSn_hourly'] = df.EXITSn - df.EXITSn.shift(1)
    df = df.fillna(0)
    return df

df=pandas.read_csv('test_df.txt')
print df
print get_hourly_exits(df)
