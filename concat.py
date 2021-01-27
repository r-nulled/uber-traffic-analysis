import pandas as pd
'''
df = pd.read_csv('/Users/deanlong/Desktop/MLPROJ/work/2019Q2.csv', usecols = ["osm_start_node_id","osm_end_node_id", "speed_mph_mean"])
cf = pd.read_csv('/Users/deanlong/Desktop/MLPROJ/work/2019Q3.csv', usecols = ["osm_start_node_id","osm_end_node_id", "speed_mph_mean"])
ef = pd.read_csv('/Users/deanlong/Desktop/MLPROJ/work/2019Q4.csv', usecols = ["osm_start_node_id","osm_end_node_id", "speed_mph_mean"])
gf = pd.read_csv('/Users/deanlong/Desktop/MLPROJ/work/2020Jan.csv', usecols = ["osm_start_node_id","osm_end_node_id", "speed_mph_mean"])
ff = pd.read_csv('/Users/deanlong/Desktop/MLPROJ/work/2020Feb.csv', usecols = ["utc_timestamp","osm_way_id","osm_start_node_id","osm_end_node_id", "speed_mph_mean"])
ff.to_pickle("Feb_data2.pkl")
'''

data = pd.read_pickle("Feb_data2.pkl")
data["Date"] = data["utc_timestamp"].apply(lambda x: str(x[:-14]))
data.drop(columns = ["utc_timestamp"], inplace = True)
data.set_index("Date", inplace = True)


weather = pd.read_csv('/Users/deanlong/Desktop/MLPROJ/work/data/output.csv')
weather.dropna(inplace = True)
weather['Temperature'] = weather['Temperature'].apply(lambda x: float(x.split()[0]))
weather['Humidity'] = weather['Humidity'].apply(lambda x: float(x[:-1])/100)
weather['WindSpeed'] = weather['WindSpeed'].apply(lambda x: float(x.split()[0]))
weather = weather.groupby('Date')["Temperature", "Humidity", "WindSpeed"].mean()
weather.reset_index(inplace = True)
weather['Date'] = weather['Date'].apply(lambda x: str(x.split()[0]))
weather.set_index("Date", inplace = True)

result = data.join(weather, how = "inner")
result.to_pickle("result.pkl")
result.to_csv("result.csv")

