import scipy.stats as stats

def hypothesis_test_decision(p_value, alpha=0.05):
    """
    Decides whether to reject or fail to reject the null hypothesis.
    """
    if p_value < alpha:
        return {
            "p_value": p_value,
            "alpha": alpha,
            "decision": "Reject Null Hypothesis",
            "statistically_significant": True
        }
    else:
        return {
            "p_value": p_value,
            "alpha": alpha,
            "decision": "Fail to Reject Null Hypothesis",
            "statistically_significant": False
        }

def t_test_1samp(data, pop_mean, alpha=0.05, alternative='two-sided'):
    """
    Performs a 1-sample t-test.
    """
    t_stat, p_val = stats.ttest_1samp(data, pop_mean, alternative=alternative)
    decision = hypothesis_test_decision(p_val, alpha)
    return {
        "t_statistic": t_stat,
        "p_value": p_val,
        **decision
    }

def t_test_2samp(data1, data2, alpha=0.05, equal_var=False, alternative='two-sided'):
    """
    Performs a 2-sample independent t-test.
    Defaults to Welch's t-test (equal_var=False).
    """
    t_stat, p_val = stats.ttest_ind(data1, data2, equal_var=equal_var, alternative=alternative)
    decision = hypothesis_test_decision(p_val, alpha)
    return {
        "t_statistic": t_stat,
        "p_value": p_val,
        **decision
    }

def t_test_rel(data_pre, data_post, alpha=0.05, alternative='two-sided'):
    """
    Performs a matched-pairs (related) t-test.
    """
    t_stat, p_val = stats.ttest_rel(data_pre, data_post, alternative=alternative)
    decision = hypothesis_test_decision(p_val, alpha)
    return {
        "t_statistic": t_stat,
        "p_value": p_val,
        **decision
    }

def power_analysis_warning(n, effect_size=0.5, alpha=0.05):
    """
    Educational note on power and error types.
    """
    return {
        "type_i_error_alpha": alpha,
        "type_ii_error_beta": "Probability of failing to reject a false null",
        "power": "1 - Beta",
        "n": n,
        "effect_size": effect_size,
        "note": "Higher sample sizes and effect sizes increase statistical power."
    }
