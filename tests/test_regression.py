import numpy as np
from statslab import regression_chi_square

def test_linear_regression():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    res = regression_chi_square.linear_regression(x, y)
    assert res['slope'] == 2.0
    assert abs(res['intercept']) < 1e-7
    assert res['r_value'] == 1.0

def test_chi_square():
    # Observed contingency table
    obs = [[10, 20], [20, 10]]
    res = regression_chi_square.chi_square_independence(obs)
    assert res['chi2_statistic'] > 0
    assert res['p_value'] < 0.05
