
def calc_percentage(a, b) -> float:
    """Return the percentage of b that a represents."""
    if b == 0:
        b = 1
    return round((a / b) * 100, 2)
