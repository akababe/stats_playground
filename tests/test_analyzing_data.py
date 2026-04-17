import pytest
import numpy as np
from statslab import analyzing_data

def test_central_tendency():
    data = [1, 2, 2, 3, 4]
    res = analyzing_data.central_tendency(data)
    assert res['mean'] == 2.4
    assert res['median'] == 2.0
    assert res['mode'] == 2

def test_spread_measures():
    data = [1, 2, 3, 4, 5]
    res = analyzing_data.spread_measures(data)
    assert res['range'] == 4
    assert res['variance'] == 2.5 # s^2 = 10 / 4 = 2.5
    assert np.isclose(res['std_dev'], np.sqrt(2.5))
    assert res['iqr'] == 2 # Q1=2, Q3=4

def test_detect_outliers():
    data = [1, 2, 3, 4, 5, 100]
    res = analyzing_data.detect_outliers(data)
    assert 100 in res['outliers']
    assert 5 not in res['outliers']
