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
