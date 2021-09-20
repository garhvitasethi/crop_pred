from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

import pandas as pd
print(chr(27) + "[2J")

# df = pd.read_csv("joint_encoded.csv")
# df = df.drop(["district", "crop", "season", "yield"], axis=1)
# print(df.head())

# df.to_csv("joint_encoded_mainRem.csv")

df2 = pd.read_csv('/Datasets/joint_encoded_mainRem.csv')
df2 = df2.drop(["Unnamed: 0"], axis=1)
print(df2.head())

Xfeatures = ["district_encoded", "year", "crop_encoded",
             "season_encoded", "area", "AvgRain", "AvgTemp"]
X = df2[Xfeatures]
# print(X)
Y = df2["production"]
# print(Y)
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.3, random_state=0)
print(type(X_test), type(X_train), type(Y_test), type(Y_train))
# X_test.to_csv("X_test.csv")
# X_train.to_csv("X_train.csv")
# Y_train.to_csv("Y_train.csv")
# Y_test.to_csv("Y_test.csv")
