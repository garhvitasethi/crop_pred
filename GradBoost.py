import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import math
from sklearn import metrics
from sklearn.metrics import r2_score
from sklearn.metrics import median_absolute_error
from sklearn.metrics import mean_squared_log_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import max_error
from sklearn.metrics import explained_variance_score
import pickle
from sklearn.neighbors import KNeighborsRegressor

from sklearn import ensemble

print(chr(27) + "[2J")

df_train = pd.read_csv("X_train.csv")
df_test = pd.read_csv("X_test.csv")
y_train = pd.read_csv("Y_train.csv")
y_test = pd.read_csv("Y_test.csv")

x_train = df_train.values
x_test = df_test.values

y_train = y_train.values
y_test = y_test.values

y_train = np.log10(y_train)
y_test = np.log10(y_test)

# print(len(x_train))
# print(len(y_train))

reg = ensemble.GradientBoostingRegressor(n_estimators=800,
                                         max_depth=2,
                                         learning_rate=0.1,
                                         criterion='mse')
reg.fit(x_train, y_train)

training_accuracy = reg.score(x_train, y_train)
test_accuracy = reg.score(x_test, y_test)
rmse_train = np.sqrt(mean_squared_error(reg.predict(x_train), y_train))
rmse_test = np.sqrt(mean_squared_error(reg.predict(x_test), y_test))
print("Training Accuracy = %0.3f, Test Accuracy = %0.3f, RMSE (train) = %0.3f, RMSE (test) = %0.3f" %
      (training_accuracy, test_accuracy, rmse_train, rmse_test))

y_true = y_test
y_pred = reg.predict(x_test)

fig, ax = plt.subplots()
ax.scatter(y_test, y_pred)
plt.title('GradBoost')
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.savefig('GradBoost.png')

print("exp variance err", explained_variance_score(y_true, y_pred))
print("max error", max_error(y_true, y_pred))
print("mae", mean_absolute_error(y_true, y_pred))
print("mse", mean_squared_error(y_true, y_pred))
print("mean sq log error", mean_squared_log_error(y_true, y_pred))
print("median absolute error", median_absolute_error(y_true, y_pred))
print("r2", r2_score(y_true, y_pred))

# filename = 'GradBoost.sav'
# pickle.dump(reg, open(filename, 'wb'))

Xnew2 = [[10, 2002, 3, 0, 70000, 19.445, 28.05]]
predc = 10 ** reg.predict(Xnew2)
print(predc)
