from statslab import probability_foundations

def test_addition_rule():
    assert probability_foundations.addition_rule(0.5, 0.4, 0.1) == 0.8

def test_bayes():
    # P(B|A) = 0.9, P(A) = 0.01, P(B) = 0.05
    res = probability_foundations.bayes_theorem(0.9, 0.01, 0.05)
    assert abs(res - 0.18) < 1e-7
