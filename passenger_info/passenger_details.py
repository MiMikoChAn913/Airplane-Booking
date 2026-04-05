def get_passenger_details():
    def get_input(prompt):
        while True:
            value = input(prompt)
            if value.strip():
                return value
            else:
                print("This field is required. Please enter a value.")

    name = get_input("Please enter your first name: ")
    surname = get_input("Please enter your surname: ")
    birthday = get_input("Please enter your birthday (YYYY-MM-DD): ")
    sex = get_input("Please enter your sex (M/F): ")
    passenger_id = get_input("Please enter your ID number: ")

    return {
        "name": name,
        "surname": surname,
        "birthday": birthday,
        "sex": sex,
        "id": passenger_id
    }