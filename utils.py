import pandas as pd

def preprocess_input(year, beds, baths, stories, garage, area, lot, pool, fireplace, renovated, rating, condo, bunglow):
    columns = [
        'year', 'beds', 'baths', 'stories', 'garage',
        'area', 'lot', 'pool', 'fireplace', 'renovated',
        'rating', 'property_type_Condo', 'property_type_Bunglow'
    ]
    values = [[
        year, beds, baths, stories, garage, area, lot, pool,
        fireplace, renovated, rating, condo, bunglow
    ]]
    return pd.DataFrame(values, columns=columns)
