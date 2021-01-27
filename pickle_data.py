import pandas as pd
df = pd.read_csv('data/uber_data.csv').dropna(how='all')
df.drop(df[df['day'] < 9].index, inplace = True)
df.drop(df[df['day'] > 16].index, inplace = True)
df.to_pickle('data/pickle.pkl')