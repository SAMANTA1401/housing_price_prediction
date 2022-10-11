import json
import pickle
import numpy as np


__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,total_sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())  # ??? AXIS 0 0 row column
    except:
        loc_index = -1

    x1 = np.zeros(len(__data_columns))
    x1[0] = total_sqft
    x1[1] = bath
    x1[2] = bhk
    if loc_index >= 0:
        x1[loc_index] = 1
    return round(__model.predict([x1])[0],2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading ...")
    global __data_columns
    global __locations


    with open("./artifacts/housing_price_columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    global __model
    if __model is None:
        with open("./artifacts/housing_price.pickle", 'rb') as f:
            __model = pickle.load(f)
    print("done")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))

