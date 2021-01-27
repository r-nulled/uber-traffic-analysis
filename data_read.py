import pandas as pd
df = pd.read_pickle('data/pickle.pkl')
pd.set_option('display.max_columns', 20)
print(df.head())