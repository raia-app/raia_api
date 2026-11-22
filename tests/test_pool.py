import dataclasses

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


def test_1500_meters_in_50_meter_pool_is_30_lengths():
    assert PoolLength(50).count_lengths(1500) == 30


def test_1510_meters_in_25_meter_pool_is_60_point_4_lengths():
    assert PoolLength(25).count_lengths(1510) == 60.4


def test_pool_length_cannot_be_changed_after_creation():
    pool = PoolLength(25)
    with pytest.raises(dataclasses.FrozenInstanceError):
        pool.meters = 0
