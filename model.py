import joblib
import pandas as pd

loaded_model = joblib.load('random_forest.sav')
print("Loaded Successfully")



df = pd.read_csv('Datasets\joint_encoded.csv')
print(df.head())

# df_district = df.drop_duplicates(
#     subset=['district', 'district_encoded'],
#     keep='last').reset_index(drop=True)
# df_district = df_district.drop(['year', 'crop', 'season', 'area',
#                                'yield', 'AvgRain', 'AvgTemp', 'crop_encoded', 'season_encoded', 'production'], axis=1)
# print(df_district.head())
# df_district.to_csv('district_encoded.csv')

# df_crop = df.drop_duplicates(
#     subset=['crop', 'crop_encoded'],
#     keep='last').reset_index(drop=True)
# df_crop = df_crop.drop(['year', 'district', 'season', 'area',
#                         'yield', 'AvgRain', 'AvgTemp', 'district_encoded', 'season_encoded', 'production'], axis=1)
# df_crop.sort_values(by=['crop_encoded'], inplace=True)
# print(df_crop.head())
# df_crop.to_csv('crop_encoded.csv')

df_season = df.drop_duplicates(
    subset=['season', 'season_encoded'],
    keep='last').reset_index(drop=True)
df_season = df_season.drop(['year', 'district', 'crop', 'area',
                            'yield', 'AvgRain', 'AvgTemp', 'district_encoded', 'crop_encoded', 'production'], axis=1)
df_season.sort_values(by=['season_encoded'], inplace=True)
print(df_season.head())
df_season.to_csv('season_encoded.csv')
