# 📊 Python StatsLab Playground

Welcome to the **Python StatsLab Playground**, a comprehensive, educationally-focused environment for experimenting with statistical concepts. This project provides both a robust functional library (`statslab`) and an interactive web-based interface (via Gradio) to explore data from visualization to complex inferential testing.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- [Optional] Virtual environment (recommended)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/akababe/stats_playground.git
   cd stats_playground
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🎮 Interactive Playground (Gradio)

The easiest way to explore statistical concepts visually is through our interactive Gradio dashboard.

To launch the dashboard:
```bash
python app.py
```
This will open an interface in your browser where you can:
- **Analyze Data**: Input numeric lists to see instant descriptive statistics, histograms, and box plots.
- **Explore Distributions**: Check for skewness, kurtosis, and normality (Shapiro-Wilk test).
- **Simulate CLT**: Watch the Central Limit Theorem in action by drawing samples from different population distributions.
- **Run Regressions**: Perform linear regression analysis and visualize the line of best fit and residuals.

---

## 📚 The `statslab` Library

The core of this project is a stateless, functional library organized into modules corresponding to key statistical domains.

### Available Modules
1.  **`visualizing_data`**: Categorical summaries, histograms (Sturges' Rule), dot plots, and ogives.
2.  **`analyzing_data`**: Central tendency (mean/median/mode), spread (variance/std dev/IQR), and outlier detection ($1.5 \times \text{IQR}$).
3.  **`data_distributions`**: Z-score standardization, skewness, kurtosis, and Chebyshev's Theorem.
4.  **`probability_foundations`**: Addition/multiplication rules, conditional probability, and Bayes' Theorem.
5.  **`discrete_random_variables`**: PMFs/CDFs for Binomial, Poisson, and Geometric distributions.
6.  **`sampling_inference`**: CLT simulation and confidence intervals for means and proportions.
7.  **`hypothesis_testing`**: 1-sample, 2-sample, and matched-pairs t-tests.
8.  **`regression_chi_square`**: Linear regression, Pearson's $r$, and Chi-Square tests.

### Library Usage Example
```python
from statslab import analyzing_data, visualizing_data

# Your dataset
data = [10, 12, 12, 13, 12, 11, 14, 13, 15, 10, 10, 10, 25]

# Get a full statistical summary
summary = analyzing_data.full_univariate_summary(data)
print(f"Mean: {summary['mean']:.2f}")
print(f"Detected Outliers: {summary['outliers']}")

# Plot results
visualizing_data.plot_histogram(data, title="Age Distribution")
```

---

## 🧪 Testing & Validation

We maintain a suite of unit tests to ensure mathematical correctness across all modules.

To run the tests:
```bash
pytest
```

---

## 📜 Educational Purpose
This project is designed for students, educators, and data enthusiasts to gain intuition about statistics through code. Every function is documented with its mathematical intent, making it a "live" textbook for learning Python-based data science.
