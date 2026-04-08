def validate_positive_number(value):
    try:
        val = float(value)
        return val if val > 0 else None
    except ValueError:
        return None
