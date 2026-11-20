from raia.lengths import count_lengths


def test_1500_meters_in_25_meter_pool_is_60_lengths():
    assert count_lengths(1500, 25) == 60
