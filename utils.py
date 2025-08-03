import pandas as pd

def preprocess_input(
    year_sold, property_tax, insurance, beds, baths, sqft,
    year_built, lot_size, basement, popular, property_age,
    bunglow, condo
):
    """
    Prepare a single-row DataFrame for prediction with the correct feature order.
    The order must exactly match the trained model's input.
    """
    data = {
        'year_sold': [year_sold],
        'property_tax': [property_tax],
        'insurance': [insurance],
        'beds': [beds],
        'baths': [baths],
        'sqft': [sqft],
        'year_built': [year_built],
        'lot_size': [lot_size],
        'basement': [basement],
        'popular': [popular],
        'property_age': [property_age],
        'property_type_Bunglow': [bunglow],   # 🟢 Correct mapping
        'property_type_Condo': [condo]        # 🟢 Correct mapping
    }

    return pd.DataFrame(data)
