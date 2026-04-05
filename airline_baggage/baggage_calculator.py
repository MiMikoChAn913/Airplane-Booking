def calculate_baggage_fee(weight):
    """Calculate the baggage fee based on weight."""
    if weight <= 10:
        fee = 450
    elif weight <= 20:
        fee = 950
    else:
        excess_weight = weight - 20
        fee = (950 + (excess_weight * 320))
    return fee