import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

def calculate_z_scores(data):
    """
    Returns the standardized (z) scores for a dataset.
    """
    return stats.zscore(data)

def shape_measures(data):
    """
    Returns skewness and kurtosis of the dataset.
    """
    skewness = stats.skew(data)
    kurtosis = stats.kurtosis(data)
    return {
        "skewness": skewness,
        "kurtosis": kurtosis
    }

def chebyshev_bound(k):
    """
    Returns the maximum proportion of data that can be more than k standard
    deviations from the mean, for k > 1.
    P(|X - mu| >= k*sigma) <= 1 / k^2
    """
    if k <= 1:
        return "k must be greater than 1"
    
    proportion = 1 / (k**2)
    return {
        "k": k,
        "max_proportion_outside": proportion,
        "min_proportion_inside": 1 - proportion
    }

def plot_histogram_with_density(data, title="Histogram with Density Curve", xlabel="Value"):
    """
    Plots a histogram with a Kernel Density Estimate (KDE) overlay.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(data, kde=True, stat="density", linewidth=0)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.show()

def is_normal_ish(data, alpha=0.05):
    """
    Performs the Shapiro-Wilk test for normality.
    """
    shapiro_test = stats.shapiro(data)
    is_normal = shapiro_test.pvalue > alpha
    return {
        "shapiro_p_value": shapiro_test.pvalue,
        "is_normal": is_normal
    }
