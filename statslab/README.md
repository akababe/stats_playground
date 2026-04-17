# Python StatsLab Playground (`statslab`)

A comprehensive Python-based environment for experimenting with statistical concepts.

## Modules

### 1. Visualizing Data (`visualizing_data`)
*   **Categorical Summaries:** One-way and two-way contingency tables.
*   **Distribution Shapes:** Histograms (using Sturges' Rule), Stem-and-leaf plots, Dot plots.
*   **Comparison Visuals:** Side-by-side and Segmented bar graphs.
*   **Cumulative Data:** Ogives.

### 2. Analyzing Data (`analyzing_data`)
*   **Central Tendency:** Mean, Median, and Mode.
*   **Spread:** Range, Variance, Standard Deviation, and IQR ($Q_3 - Q_1$).
*   **Outlier Detection:** $1.5 \times \text{IQR}$ rule.
*   **Visual Aid:** Box-and-whisker plots.

### 3. Data Distributions (`data_distributions`)
*   **Standardization:** Z-scores ($z = \frac{x - \mu}{\sigma}$).
*   **Shape:** Skewness and Kurtosis.
*   **Chebyshev's Theorem:** Bounds for non-normal distributions.
*   **Density Curves:** KDE overlays for histograms.

### 4. Probability Foundations (`probability_foundations`)
*   **Rules:** Addition and Multiplication rules.
*   **Conditional Probability:** $P(A | B)$.
*   **Bayes' Theorem:** Updating probabilities with new evidence.

### 5. Discrete Random Variables (`discrete_random_variables`)
*   **Distributions:** Binomial, Poisson, Geometric, and Bernoulli.
*   **Combinatorics:** Permutations and Combinations.

### 6. Sampling & Inference (`sampling_inference`)
*   **CLT Simulator:** Visual demonstration of the Central Limit Theorem.
*   **Confidence Intervals:** For means (t-dist) and proportions (z-dist).
*   **Sample Size:** Calculations for desired margin of error.

### 7. Hypothesis Testing (`hypothesis_testing`)
*   **T-Tests:** 1-sample, 2-sample (Welch's), and Matched-pairs.
*   **Decision Logic:** P-value vs. Significance level ($\alpha$).

### 8. Regression & Chi-Square (`regression_chi_square`)
*   **Linear Regression:** Least squares line, residuals, and $R^2$.
*   **Correlation:** Pearson's $r$.
*   **Chi-Square:** Independence and Goodness-of-Fit tests.

## Installation

```bash
pip install -r requirements.txt
```

## Example Usage

```python
from statslab import analyzing_data, visualizing_data

data = [10, 12, 12, 13, 12, 11, 14, 13, 15, 10, 10, 10, 100]

# Get statistical summary
summary = analyzing_data.full_univariate_summary(data)
print(f"Mean: {summary['mean']}")
print(f"Outliers: {summary['outliers']}")

# Plot a box plot
analyzing_data.plot_box_plot(data, title="Sample Box Plot")
```
