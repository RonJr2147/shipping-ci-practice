from app.shipping import shipping_fee


def test_member_ships_free():
    total = 80
    is_member = True

    result = shipping_fee(total, is_member)

    assert result == 0

def test_non_member_pays_standard_fee():
    result = shipping_fee(80, False)

    assert result == 5.99