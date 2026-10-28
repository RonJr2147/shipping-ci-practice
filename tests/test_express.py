from app.shipping import express_fee


def test_far_away_costs_25():
    assert express_fee(40, 80) == 25.00


def test_big_order_nearby_costs_10():
    assert express_fee(120, 10) == 10.00


def test_small_order_nearby_costs_15():
    assert express_fee(40, 10) == 15.00