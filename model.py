import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

def load_data(path):
    df = pd.read_csv(path)
    df['property_type_Condo'] = df['property_type_Condo'].astype(object)
    df['property_type_Bunglow'] = df['property_type_Bunglow'].astype(object)
    return df

def train_model(df):
    x = df.drop('price', axis=1)
    y = df['price']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, stratify=x['property_type_Bunglow'])
    model = DecisionTreeRegressor(max_depth=3, max_features=10, random_state=567)
    model.fit(x_train, y_train)
    return model, x_train, x_test, y_train, y_test

def save_model(model, path='models/RE_Model.pkl'):
    with open(path, 'wb') as f:
        pickle.dump(model, f)

def load_model(path='models/RE_Model.pkl'):
    with open(path, 'rb') as f:
        return pickle.load(f)

def evaluate_model(model, x_test, y_test):
    y_pred = model.predict(x_test)
    return mean_absolute_error(y_test, y_pred)
