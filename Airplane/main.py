from Airplane.data_loader import load_data
from Airplane.display_options import show_available_cities
from Airplane.flight_search import find_flights

import pandas as pd

def flight_booking():
   
    df = load_data()
    show_available_cities(df)
    
    
    from_city = input("Please enter your province of origin: ").strip()
    to_city = input("Please enter your destination province: ").strip()
    
    
    # Find flights
    result = find_flights(df, from_city, to_city)
    result_df = pd.DataFrame(result)

    
    if not result.empty:
        print(f"\nAvailable flights from {from_city} to {to_city}:")
        # result
    else:
        print(f"\nNo flights found from {from_city} to {to_city}.")

    return result_df



if __name__ == "__main__":
    flight_booking()

