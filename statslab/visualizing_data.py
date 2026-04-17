import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

def categorical_summary(data, index=None, columns=None, normalize=False):
    """
    Creates a one-way or two-way contingency table.
    """
    if columns is None:
        # One-way table
        summary = pd.Series(data).value_counts(normalize=normalize).sort_index()
        return summary
    else:
        # Two-way table
        return pd.crosstab(data[index], data[columns], normalize=normalize)

def sturges_bins(data):
    """
    Calculates the number of bins using Sturges' Rule: k = 1 + 3.322 * log10(n)
    """
    n = len(data)
    if n == 0:
        return 1
    k = 1 + 3.322 * math.log10(n)
    return max(1, math.ceil(k))

def plot_histogram(data, title="Histogram", xlabel="Value", ylabel="Frequency", bins=None, kde=False):
    """
    Plots a histogram using Sturges' Rule if bins is None.
    """
    if bins is None:
        bins = sturges_bins(data)
    
    plt.figure(figsize=(10, 6))
    sns.histplot(data, bins=bins, kde=kde)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def plot_stem_and_leaf(data):
    """
    Simple text-based stem-and-leaf plot.
    """
    data = sorted(data)
    stems = {}
    for x in data:
        stem = x // 10
        leaf = x % 10
        if stem not in stems:
            stems[stem] = []
        stems[stem].append(str(leaf))
    
    print("Stem | Leaf")
    print("-----------")
    for stem in sorted(stems.keys()):
        print(f"{stem:4} | {' '.join(stems[stem])}")

def plot_dot_plot(data, title="Dot Plot", xlabel="Value"):
    """
    Plots a simple dot plot.
    """
    unique_values, counts = np.unique(data, return_counts=True)
    
    plt.figure(figsize=(10, 6))
    for val, count in zip(unique_values, counts):
        plt.plot([val] * count, range(count), 'o', color='blue')
    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.yticks([])
    plt.show()

def plot_side_by_side_bar(data, x, hue, title="Side-by-Side Bar Graph"):
    """
    Plots a side-by-side bar chart.
    """
    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x=x, hue=hue)
    plt.title(title)
    plt.show()

def plot_segmented_bar(data, x, hue, title="Segmented Bar Chart"):
    """
    Plots a segmented (stacked) bar chart.
    """
    pivot_df = data.groupby([x, hue]).size().unstack(fill_value=0)
    # Normalize to get percentages for segmented bar chart
    pivot_df_rel = pivot_df.div(pivot_df.sum(axis=1), axis=0)
    
    pivot_df_rel.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.title(title)
    plt.ylabel("Proportion")
    plt.show()

def plot_ogive(data, title="Ogive (Cumulative Frequency Polygon)", xlabel="Value"):
    """
    Plots an Ogive.
    """
    values, base = np.histogram(data, bins=sturges_bins(data))
    cumulative = np.cumsum(values)
    # Add a zero at the beginning
    cumulative = np.insert(cumulative, 0, 0)
    
    plt.figure(figsize=(10, 6))
    plt.plot(base, cumulative, marker='o', linestyle='-')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Cumulative Frequency")
    plt.grid(True)
    plt.show()
