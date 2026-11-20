from raia.lengths import count_lengths, distance_fits_pool


def test_1500_meters_in_25_meter_pool_is_60_lengths():
    assert count_lengths(1500, 25) == 61


def test_1500_meters_fits_25_meter_pool():
    assert distance_fits_pool(1500, 25)


def test_1510_meters_does_not_fit_25_meter_pool():
    assert not distance_fits_pool(1510, 25)


def test_1500_meters_in_50_meter_pool_is_30_lengths():
    assert count_lengths(1500, 50) == 30


def test_1510_meters_in_25_meter_pool_is_60_point_4_lengths():
    assert count_lengths(1510, 25) == 60.4
