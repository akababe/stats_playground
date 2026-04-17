import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

def central_tendency(data):
    """
    Returns mean, median, and mode(s).
    """
    mean = np.mean(data)
    median = np.median(data)
    mode_res = stats.mode(data, keepdims=True)
    mode = mode_res.mode[0] if mode_res.count[0] > 0 else None
    return {
        "mean": mean,
        "median": median,
        "mode": mode
    }

def spread_measures(data):
    """
    Returns range, variance, standard deviation, and IQR.
    Uses sample variance/std (n-1 degrees of freedom).
    """
    data_range = np.ptp(data)
    variance = np.var(data, ddof=1)
    std_dev = np.std(data, ddof=1)
    q1, q3 = np.percentile(data, [25, 75])
    iqr = q3 - q1
    return {
        "range": data_range,
        "variance": variance,
        "std_dev": std_dev,
        "q1": q1,
        "q3": q3,
        "iqr": iqr
    }

def detect_outliers(data):
    """
    Identifies outliers using the 1.5 * IQR rule.
    """
    q1, q3 = np.percentile(data, [25, 75])
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    outliers = [x for x in data if x < lower_bound or x > upper_bound]
    return {
        "outliers": outliers,
        "lower_bound": lower_bound,
        "upper_bound": upper_bound
    }

def plot_box_plot(data, title="Box and Whisker Plot", xlabel="Value", horizontal=True):
    """
    Plots a box-and-whisker plot.
    """
    plt.figure(figsize=(10, 6))
    if horizontal:
        sns.boxplot(x=data)
    else:
        sns.boxplot(y=data)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.show()

def full_univariate_summary(data):
    """
    Returns a comprehensive statistical summary of the dataset.
    """
    ct = central_tendency(data)
    sm = spread_measures(data)
    od = detect_outliers(data)
    
    summary = {**ct, **sm, **od}
    return summary
