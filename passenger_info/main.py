from passenger_info.passenger_details import get_passenger_details
from passenger_info.passenger_count import get_passenger_count, get_passport_numbers

def personal_flight_booking():
    passenger_count = get_passenger_count()

    
    destination = input("Please enter your destination province: ").strip()

    passengers = []
    for _ in range(passenger_count):
        passenger = get_passenger_details()
        passengers.append(passenger)

    passport_numbers = get_passport_numbers(passenger_count)


    for i, passenger in enumerate(passengers):
        print(f"\nPassenger {i + 1} Details:")
        print(f"Name: {passenger['name']} {passenger['surname']}")
        print(f"Birthday: {passenger['birthday']}")
        print(f"Sex: {passenger['sex']}")
        print(f"ID Number: {passenger['id']}")
        print(f"Passport Number: {passport_numbers[i]}")
        print(f"Destination: {destination}")  

if __name__ == "__main__":
    personal_flight_booking()