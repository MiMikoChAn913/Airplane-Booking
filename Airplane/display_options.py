def show_available_cities(df):
    available_from_cities = df["From City"].unique()
    available_to_cities = df["To City"].unique()
    
    print("Available provinces for origin:")
    print(available_from_cities)
    
    print("\nAvailable provinces for destination:")
    print(available_to_cities)