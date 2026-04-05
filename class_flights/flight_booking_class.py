import pandas as pd

# ฟังก์ชันโหลดข้อมูลเที่ยวบินจากไฟล์ CSV
def load_data(file_path="thailand_flights_updated_schedule (1) (1).csv"):
    # โหลดข้อมูลจากไฟล์ CSV
    df = pd.read_csv(file_path)
    
    # ตรวจสอบว่ามีข้อมูลอยู่หรือไม่
    if df.empty:
        print("No flight data found.")
        return None
    return df

# ฟังก์ชันการจองตั๋ว
def flight_booking_class():
    # โหลดข้อมูลจากไฟล์
    df = load_data()
    if df is None:
        return
    

    # ให้ผู้ใช้เลือก flight number
    flight_number = input("\nPlease enter the flight number you want to book: ").strip()

    # ค้นหาข้อมูลของเที่ยวบินที่เลือก
    flight = df[df['Flight Number'] == flight_number]

    if flight.empty:
        print("\nInvalid flight number. Please try again.")
        return

    # แสดงข้อมูลของเที่ยวบินที่เลือก
    print(f"\nYou have selected flight {flight_number} from {flight['From City'].values[0]} to {flight['To City'].values[0]}")
    
    # แสดงราคาคลาสที่นั่ง
    print("\nAvailable seat classes and prices:")
    print(f"Economy Class: {flight['Economy Class'].values[0]} THB")
    print(f"Business Class: {flight['Business Class'].values[0]} THB")
    print(f"First Class: {flight['First Class'].values[0]} THB")



    # ให้ผู้ใช้เลือกคลาสที่นั่ง
    seat_class = input("\nPlease choose a seat class (First Class, Business Class, Economy Class): ").strip()

    if seat_class == "First Class":
        price = flight['First Class'].values[0]
    elif seat_class == "Business Class":
        price = flight['Business Class'].values[0]
    elif seat_class == "Economy Class":
        price = flight['Economy Class'].values[0]
    else:
        print("\nInvalid seat class. Please try again.")
        return

    # ขอจำนวนที่นั่งจากผู้ใช้
    try:
        num_seats = int(input(f"How many seats would you like to book in {seat_class}? "))
    except ValueError:
        print("\nInvalid number of seats entered. Please try again.")
        return

    # คำนวณราคา
    total_price = price * num_seats
    print(f"\nBooking successful! {num_seats} seat(s) reserved in {seat_class}.")
    return total_price

if __name__ == "__main__":
    flight_booking_class()
