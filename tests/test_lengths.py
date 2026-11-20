from raia.lengths import count_lengths, distance_fits_pool


def test_1500_meters_in_25_meter_pool_is_60_lengths():
    assert count_lengths(1500, 25) == 60


def test_1500_meters_fits_25_meter_pool():
    assert distance_fits_pool(1500, 25)


def test_1510_meters_does_not_fit_25_meter_pool():
    assert not distance_fits_pool(1510, 25)
    