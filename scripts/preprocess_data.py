import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("data/raw_data.csv")
df.dropna(inplace=True)

scaler = StandardScaler()
df[["temperature", "humidity", "wind_speed"]] = scaler.fit_transform(df[["temperature", "humidity", "wind_speed"]])
df.to_csv("data/processed_data.csv", index=False)
