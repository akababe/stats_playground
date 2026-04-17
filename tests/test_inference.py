import numpy as np
from statslab import sampling_inference

def test_mean_ci():
    data = [1, 2, 3, 4, 5] # mean = 3, se = sem([1,2,3,4,5]) = 1.5811 / sqrt(5) = 0.7071
    res = sampling_inference.mean_confidence_interval(data, confidence=0.95)
    assert res['mean'] == 3.0
    assert res['lower_bound'] < 3.0
    assert res['upper_bound'] > 3.0

def test_prop_ci():
    res = sampling_inference.proportion_confidence_interval(50, 100, confidence=0.95)
    assert res['proportion'] == 0.5
    assert np.isclose(res['margin_of_error'], 1.96 * np.sqrt(0.5 * 0.5 / 100), atol=1e-3)
