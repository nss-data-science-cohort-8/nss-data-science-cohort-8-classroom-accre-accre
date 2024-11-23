import pandas as pd

# slurm log csv conversion
def log_to_df(log):
    df = pd.read_csv(log,
        header=None,
        delimiter=' - ',
        engine='python')
    return df

# slurm log finding for user 9204, with a return code of 1, and time of 15 seconds, and in sbatch. pulling only the timestamps out of the log
def df_to_datelist(df1):
    df = df1.copy(deep = True)
    df[3] = df[3].str.replace('time ', '')
    df[3] = df[3].astype(float)
    df = df[df[1] == 'user 9204']
    df = df[df[3] >= 15]
    df = df[df[4] == "returncode 1"]
    df['sbatch'] = df[5].apply(lambda x: 1 if 'sbatch' in x else 0)
    df = df[df['sbatch'] == 1]
    df[0] = pd.to_datetime(df[0])
    return df[0].to_list()
