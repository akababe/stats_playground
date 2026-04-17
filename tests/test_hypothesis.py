from statslab import hypothesis_testing

def test_t_test_1samp():
    data = [1, 2, 3, 4, 5]
    res = hypothesis_testing.t_test_1samp(data, pop_mean=3)
    assert res['p_value'] > 0.99 # mean is 3, so p-value should be 1
    assert res['decision'] == "Fail to Reject Null Hypothesis"

def test_t_test_2samp():
    data1 = [1, 2, 3]
    data2 = [10, 11, 12]
    res = hypothesis_testing.t_test_2samp(data1, data2)
    assert res['p_value'] < 0.05
    assert res['decision'] == "Reject Null Hypothesis"
