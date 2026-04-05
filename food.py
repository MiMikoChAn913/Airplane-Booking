class FlightFoodService:
    def __init__(self):
        self.menu_schedule = {}
        self.menu_business = {
            'Gourmet Meal': 500,
            'Caviar': 800,
            'Champagne': 400
        }

    def add_default_menu(self):
        """เพิ่มเมนูเริ่มต้นสำหรับทุกเที่ยวบิน"""
        short_flight_menu = {
            'Snack': 100,
            'Sandwich': 150,
            'Fruit Salad': 120
        }
        long_flight_menu = {
            'Pasta': 300,
            'Chicken Rice': 350,
            'Vegetarian Dish': 320
        }
        self.menu_schedule = {
            'short': short_flight_menu,
            'long': long_flight_menu
        }

    def display_menu(self, flight_type, seat_class):
        """แสดงเมนูตามประเภทเที่ยวบินและชั้นที่นั่ง"""
        print(f"\nMenu ({flight_type} flight in {seat_class} class):")

        if flight_type == 'short':
            menu = self.menu_schedule['short']
        else:
            menu = self.menu_schedule['long']

        # หากเป็นชั้นธุรกิจ ให้เพิ่มเมนูเพิ่มเติม
        if seat_class == 'business':
            menu.update(self.menu_business)

        for index, (item, price) in enumerate(menu.items(), 1):
            print(f"{index}. {item}: {price} THB")

        return list(menu.items())  # คืนรายการเมนูในรูปแบบลำดับสำหรับการเลือก

    def calculate_total(self, food_choices, menu_items):
        """คำนวณราคารวมจากอาหารที่เลือก"""
        total_price = 0
        for choice in food_choices:
            total_price += menu_items[choice - 1][1]  # ดึงราคาจากรายการเมนูที่เลือก
        return total_price


def main():
    service = FlightFoodService()
    service.add_default_menu()  # เพิ่มเมนูเริ่มต้น

    # เลือกประเภทเที่ยวบินและชั้นโดยสาร
    flight_type = input("Enter flight type (short/long): ").strip().lower()
    while flight_type not in ["short", "long"]:
        flight_type = input("Invalid flight type. Please enter 'short' or 'long': ").strip().lower()

    seat_class = input("Enter seat class (economy/business): ").strip().lower()
    while seat_class not in ["economy", "business"]:
        seat_class = input("Invalid seat class. Please enter 'economy' or 'business': ").strip().lower()

    # แสดงเมนูและให้ผู้ใช้เลือกอาหาร
    menu_items = service.display_menu(flight_type, seat_class)

    food_choices = []
    while True:
        choice = input("\nEnter the number of the food you want to select (or type 'done' to finish): ").strip()
        if choice.lower() == 'done':
            break
        try:
            choice = int(choice)
            if 1 <= choice <= len(menu_items):
                food_choices.append(choice)
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # สรุปการเลือกอาหารและราคารวม
    if food_choices:
        total_price = service.calculate_total(food_choices, menu_items)
        print("\nYou have selected:")
        for choice in food_choices:
            print(f"- {menu_items[choice - 1][0]}: {menu_items[choice - 1][1]} THB")
        print(f"Total Price: {total_price} THB")
    else:
        print("No food selected.")


if __name__ == "__main__":
    main()