import pytest

from raia.pool import PoolLength


def test_25_meter_pool_keeps_its_length():
    assert PoolLength(25).meters == 25


def test_pool_with_zero_meters_is_rejected():
    with pytest.raises(ValueError):
        PoolLength(0)


def test_pool_with_negative_meters_is_rejected():
    with pytest.raises(ValueError):
        PoolLength(-25)


def test_1500_meters_in_25_meter_pool_is_60_lengths():
    assert PoolLength(25).count_lengths(1500) == 60


def test_1510_meters_does_not_fit_25_meter_pool():
    assert not PoolLength(25).fits(1510)


def test_1500_meters_fits_25_meter_pool():
    assert PoolLength(25).fits(1500)
