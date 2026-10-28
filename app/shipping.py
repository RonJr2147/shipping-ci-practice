def shipping_fee(total, is_member):
    """Return the shipping fee in dollars."""
    fee = 5.99
    if is_member:
        fee = 0
    return fee

def express_fee(total, distance_km):
    """Return the express-delivery fee in dollars."""

    if distance_km > 50:
        return 25.00

    if total >= 100:
        return 10.00

    return 15.00