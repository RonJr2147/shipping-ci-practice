def shipping_fee(total, is_member):
    """Return the shipping fee in dollars."""
    fee = 5.99
    if is_member:
        fee = 0
    return fee