import pandas as pd

def load_data(file_path="thailand_flights_updated_schedule (1) (1).csv"):
    return pd.read_csv(file_path)