try:
    import sys
    import csv
    import joblib
except Exception as e:
    print(e)
loaded_model = joblib.load('random_forest.sav')
# print("Loaded Successfully")
# Creating dictionaries for each encoded variable

inputDistrict = sys.argv[1]
inputYear = sys.argv[2]
inputSeason = sys.argv[3]
inputArea = sys.argv[4]
inputRain = sys.argv[5]
inputTemperature = sys.argv[6]

print("before reader 1")

try:
    reader = csv.reader(open('encoded_files\district_encoded.csv', 'r'))
except Exception as e:
    print("Reader1",e)
dict_district = {}
for row in reader:
    k = row[1]
    v = row[2]
    dict_district[k] = v

del dict_district['district']
print("before reader 2")
try:
    reader2 = csv.reader(open('encoded_files\crop_encoded.csv', 'r'))
except Exception as e:
    print("Reader2",e)
dict_crop = {}
for row in reader2:
    a = row[1]
    b = row[2]
    dict_crop[a] = b

del dict_crop['crop']
# print(dict_crop)
print("Before reader 3")
reader3 = csv.reader(open('encoded_files\season_encoded.csv', 'r'))
dict_season = {}
for row in reader3:
    x = row[1]
    y = row[2]
    dict_season[x] = y

del dict_season['season']
# print(dict_season)


def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key

    return "key doesn't exist"



predDistrict = inputDistrict
predDistrict = int(predDistrict)

# Year
predYear = int(inputYear)

predSeason = inputSeason
predSeason = int(predSeason)

predArea = float(inputArea)

predRain = float(inputRain)

predTemp = float(inputTemperature)

print("before final dict")
finalDict = {}
for x in range(21):
    Xnew2 = [[predDistrict, predYear, x,
              predSeason, predArea, predRain, predTemp]]
    predc = 10 ** loaded_model.predict(Xnew2)
    predcVal = int(predc[0])
    crop = get_key(str(x), dict_crop)
    # crop = int(crop)
    finalDict[crop] = predcVal
    # print(predc)
    Xnew2 *= 0

# {k: v for k, v in sorted(finalDict.items(), key=lambda item: item[1])}
marklist = sorted(finalDict.items(), key=lambda x: x[1])
sortdict = dict(marklist)
# print(sortdict)
# print(finalDict)
keys_list = list(sortdict)
print("keyslist",keys_list)
print("finalprint")
# print("Crops with most Yield suitable with input parameters")
# Xnew2[0].pop(2)
# print(predDistrict, predYear, predSeason, predArea, predRain, predTemp)
print(keys_list[20])
print(keys_list[19])
print(keys_list[18])
