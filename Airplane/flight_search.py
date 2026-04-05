def find_flights(df, from_city, to_city):
    
    filtered_flights = df[(df["From City"] == from_city) & (df["To City"] == to_city)]
    sorted_flights = filtered_flights.sort_values(by="Economy Class")
    return sorted_flights