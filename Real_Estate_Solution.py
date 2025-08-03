
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn import tree
import pickle

# Load data
df = pd.read_csv('final.csv')

# Ensure correct data types
df['property_type_Condo'] = df['property_type_Condo'].astype(object)
df['property_type_Bunglow'] = df['property_type_Bunglow'].astype(object)

# Split features and target
x = df.drop('price', axis=1)
y = df['price']

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, stratify=x['property_type_Bunglow'])

# Linear Regression
lrmodel = LinearRegression().fit(x_train, y_train)
train_pred = lrmodel.predict(x_train)
print('Linear Regression Train MAE:', mean_absolute_error(train_pred, y_train))
test_pred = lrmodel.predict(x_test)
print('Linear Regression Test MAE:', mean_absolute_error(test_pred, y_test))

# Decision Tree
dtmodel = DecisionTreeRegressor(max_depth=3, max_features=10, random_state=567).fit(x_train, y_train)
train_pred = dtmodel.predict(x_train)
print('Decision Tree Train MAE:', mean_absolute_error(train_pred, y_train))
test_pred = dtmodel.predict(x_test)
print('Decision Tree Test MAE:', mean_absolute_error(test_pred, y_test))

# Plot and save tree
plt.figure(figsize=(20,10))
tree.plot_tree(dtmodel, feature_names=dtmodel.feature_names_in_)
plt.savefig('tree.png', dpi=300)

# Random Forest
rfmodel = RandomForestRegressor(n_estimators=200, criterion='absolute_error').fit(x_train, y_train)
test_pred = rfmodel.predict(x_test)
print('Random Forest Test MAE:', mean_absolute_error(test_pred, y_test))

# Save model
pickle.dump(dtmodel, open('RE_Model', 'wb'))

# Predict from loaded model
RE_Model = pickle.load(open('RE_Model', 'rb'))
print('Sample Prediction:', RE_Model.predict([x_train.iloc[0].to_numpy()]))
