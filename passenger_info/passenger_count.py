def get_passenger_count():
    while True:
        try:
            count = int(input("Please enter the number of passengers: "))
            if count > 0:
                return count
            else:
                print("Number of passengers must be at least 1.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_passport_numbers(count):
    passport_numbers = []
    for i in range(count):
        passport_number = input(f"Please enter the passport number for passenger {i + 1}: ")
        passport_numbers.append(passport_number)
    return passport_numbers