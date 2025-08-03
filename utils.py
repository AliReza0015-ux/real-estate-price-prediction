import pandas as pd

def preprocess_input(year_sold, property_tax, insurance, beds, baths, sqft,
                     year_built, lot_size, basement, popular, property_age,
                     condo, bunglow):
    
    columns = [
        'year_sold', 'property_tax', 'insurance', 'beds', 'baths', 'sqft',
        'year_built', 'lot_size', 'basement', 'popular', 'property_age',
        'property_type_Condo', 'property_type_Bunglow'
    ]
    
    values = [[
        year_sold, property_tax, insurance, beds, baths, sqft,
        year_built, lot_size, basement, popular, property_age,
        condo, bunglow
    ]]
    
    return pd.DataFrame(values, columns=columns)
