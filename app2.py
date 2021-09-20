from sklearn.preprocessing import LabelEncoder
import pandas as pd
print(chr(27) + "[2J")

df = pd.read_csv("/Datasets/joint.csv")
ds = LabelEncoder()
cr = LabelEncoder()
se = LabelEncoder()
df['district_encoded'] = ds.fit_transform(df['district'].values)
df['crop_encoded'] = cr.fit_transform(df['crop'].values)
df['season_encoded'] = se.fit_transform(df['season'].values)

print(df.head())

# df.to_csv("joint_encoded.csv")
