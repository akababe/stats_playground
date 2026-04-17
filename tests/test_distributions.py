from statslab import data_distributions

def test_z_scores():
    data = [1, 2, 3]
    z = data_distributions.calculate_z_scores(data)
    assert abs(z[1]) < 1e-7 # 2 is the mean, so z should be 0

def test_chebyshev():
    res = data_distributions.chebyshev_bound(2)
    assert res['max_proportion_outside'] == 0.25
    assert res['min_proportion_inside'] == 0.75
