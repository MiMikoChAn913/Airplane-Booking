def validate_weight(weight):
    """Validate that the weight is a positive number."""
    if weight < 0:
        raise ValueError("Weight cannot be negative.")
    return True