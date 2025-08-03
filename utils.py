import pandas as pd

def preprocess_input(year, beds, baths, stories, garage, area, lot, pool, fireplace, renovated, rating, condo, bunglow):
    # Use exact feature names from training data
    columns = [
        'year',                  # match column name
        'beds',
        'baths',
        'stories',
        'garage',
        'area',
        'lot',
        'pool',
        'fireplace',
        'renovated',
        'rating',
        'property_type_Condo',   # match one-hot column
        'property_type_Bunglow'  # match one-hot column
    ]
    
    values = [[
        year, beds, baths, stories, garage, area, lot,
        pool, fireplace, renovated, rating, condo, bunglow
    ]]
    
    return pd.DataFrame(values, columns=columns)
