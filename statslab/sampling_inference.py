import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def simulate_clt(population_data, sample_size=30, num_samples=1000):
    """
    Demonstrates the Central Limit Theorem by drawing multiple samples
    from a population and plotting the distribution of their means.
    """
    sample_means = []
    for _ in range(num_samples):
        sample = np.random.choice(population_data, size=sample_size, replace=True)
        sample_means.append(np.mean(sample))
    
    plt.figure(figsize=(10, 6))
    plt.hist(sample_means, bins=30, edgecolor='black', alpha=0.7)
    plt.title(f"CLT: Distribution of {num_samples} Sample Means (n={sample_size})")
    plt.xlabel("Sample Mean")
    plt.ylabel("Frequency")
    plt.show()
    
    return sample_means

def mean_confidence_interval(data, confidence=0.95):
    """
    Calculates a confidence interval for the population mean.
    Uses t-distribution if sample size is small/sigma unknown.
    """
    n = len(data)
    m = np.mean(data)
    se = stats.sem(data)
    # df = n - 1
    h = se * stats.t.ppf((1 + confidence) / 2., n-1)
    return {
        "mean": m,
        "margin_of_error": h,
        "lower_bound": m - h,
        "upper_bound": m + h,
        "confidence_level": confidence
    }

def proportion_confidence_interval(count, n, confidence=0.95):
    """
    Calculates a confidence interval for a population proportion.
    Uses normal approximation (z-distribution).
    """
    p_hat = count / n
    z_star = stats.norm.ppf((1 + confidence) / 2.)
    se = np.sqrt((p_hat * (1 - p_hat)) / n)
    h = z_star * se
    return {
        "proportion": p_hat,
        "margin_of_error": h,
        "lower_bound": p_hat - h,
        "upper_bound": p_hat + h,
        "confidence_level": confidence
    }

def required_sample_size_mean(margin_of_error, std_dev, confidence=0.95):
    """
    Returns required sample size to achieve a certain margin of error for the mean.
    n = (z* sigma / ME)^2
    """
    z_star = stats.norm.ppf((1 + confidence) / 2.)
    n = ((z_star * std_dev) / margin_of_error)**2
    return np.ceil(n)
