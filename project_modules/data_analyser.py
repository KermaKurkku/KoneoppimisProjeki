# !/usr/bin/python
# coding=utf-8

import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
data_X = np.array([5, 15, 25, 35, 45, 55, 66, 67, 77]).reshape((-1, 1))
data_y = np.array([5, 20, 14, 32, 22, 18, 36, 28, 14])

# Use only one feature
# data_X = data_X[:, np.newaxis, 2]

# Split the data into training/testing sets
data_X_train = data_X[:-3]
data_X_test = data_X[-3:]

# Split the targets into training/testing sets
data_y_train = data_y[:-3]
data_y_test = data_y[-3:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(data_X_train, data_y_train)

# Make predictions using the testing set
data_y_pred = regr.predict(data_X_test)

# The intercept (B0)
print('intercept:', regr.intercept_)
# The coefficients (B1)
print("Coefficients: \n", regr.coef_)
# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error(data_y_test, data_y_pred))
# The coefficient of determination: 1 is perfect prediction
print("Coefficient of determination: %.2f" % r2_score(data_y_test, data_y_pred))

# Plot outputs
#plt.scatter(data_X_test, data_y_test, color="black")
#plt.plot(data_X_test, data_y_pred, color="blue", linewidth=3)

#plt.xticks(())
#plt.yticks(())

#plt.show()
