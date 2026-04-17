import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def linear_regression(x, y):
    """
    Performs simple linear regression: y = b0 + b1*x.
    """
    res = stats.linregress(x, y)
    
    # Calculate residuals
    y_pred = res.intercept + res.slope * np.array(x)
    residuals = np.array(y) - y_pred
    
    return {
        "slope": res.slope,
        "intercept": res.intercept,
        "r_value": res.rvalue,
        "r_squared": res.rvalue**2,
        "p_value": res.pvalue,
        "stderr": res.stderr,
        "intercept_stderr": res.intercept_stderr,
        "residuals": residuals,
        "y_pred": y_pred
    }

def plot_regression_line(x, y, title="Linear Regression"):
    """
    Plots a scatter plot with the regression line and residuals.
    """
    reg = linear_regression(x, y)
    
    plt.figure(figsize=(10, 6))
    sns.regplot(x=x, y=y)
    plt.title(f"{title} (R^2 = {reg['r_squared']:.4f})")
    plt.show()

def plot_residuals(x, residuals, title="Residual Plot"):
    """
    Plots the residuals against x.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(x, residuals)
    plt.axhline(0, color='red', linestyle='--')
    plt.title(title)
    plt.xlabel("Independent Variable (x)")
    plt.ylabel("Residuals (y - y_hat)")
    plt.show()

def chi_square_independence(observed_data, alpha=0.05):
    """
    Performs Chi-Square test for independence on a contingency table.
    """
    chi2, p, dof, expected = stats.chi2_contingency(observed_data)
    
    significant = p < alpha
    
    return {
        "chi2_statistic": chi2,
        "p_value": p,
        "degrees_of_freedom": dof,
        "expected_frequencies": expected,
        "significant": significant,
        "decision": "Reject Null" if significant else "Fail to Reject Null"
    }

def chi_square_goodness_of_fit(observed_freq, expected_freq=None, alpha=0.05):
    """
    Performs Chi-Square goodness-of-fit test.
    If expected_freq is None, assumes uniform distribution.
    """
    res = stats.chisquare(observed_freq, f_exp=expected_freq)
    significant = res.pvalue < alpha
    
    return {
        "chi2_statistic": res.statistic,
        "p_value": res.pvalue,
        "significant": significant,
        "decision": "Reject Null" if significant else "Fail to Reject Null"
    }

def correlation_coefficient(x, y):
    """
    Returns Pearson's r correlation coefficient.
    """
    r, p = stats.pearsonr(x, y)
    return {
        "r": r,
        "p_value": p
    }
