from .baggage_calculator import calculate_baggage_fee
from .utils import validate_weight
def main():
    weight = float(input("Enter baggage weight (kg): "))
    print("Baggage weight is (Kg) : " , weight)
    try:
        validate_weight(weight)
        fee = calculate_baggage_fee(weight)
        return round(fee)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()