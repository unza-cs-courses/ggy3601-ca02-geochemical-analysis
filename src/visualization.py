"""
GGY3601 Coding Assignment 2: Visualization Module

This module provides functions for creating geochemical data visualizations.

Author: [YOUR NAME]
Student ID: [YOUR ID]
Date: [DATE]
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def plot_element_histogram(df, element, bins=30, title=None, save_path=None):
    """
    Create a histogram of element concentration values.

    This function creates a histogram showing the distribution of element
    concentrations, which is useful for understanding data distribution
    and identifying potential anomalies.

    Args:
        df (pandas.DataFrame): DataFrame containing assay data.
        element (str): Column name for the element to plot.
        bins (int): Number of histogram bins (default 30).
        title (str, optional): Plot title. If None, auto-generated.
        save_path (str, optional): Path to save the figure. If None,
            displays the plot.

    Returns:
        matplotlib.figure.Figure: The created figure object.

    Example:
        >>> df = load_assay_data('data/geochemical_assays.csv')
        >>> fig = plot_element_histogram(df, 'Au_ppm', bins=50)
        >>> plt.show()
    """
    # TODO: Implement this function
    # Hint:
    # fig, ax = plt.subplots(figsize=(10, 6))
    # ax.hist(df[element].dropna(), bins=bins, edgecolor='black', alpha=0.7)
    # ax.set_xlabel(element)
    # ax.set_ylabel('Frequency')
    # ax.set_title(title or f'Distribution of {element}')
    pass


def plot_element_boxplot(df, elements, title=None, save_path=None):
    """
    Create box plots for multiple elements.

    Box plots are useful for comparing distributions across multiple
    elements and identifying outliers.

    Args:
        df (pandas.DataFrame): DataFrame containing assay data.
        elements (list): List of element column names to plot.
        title (str, optional): Plot title. If None, auto-generated.
        save_path (str, optional): Path to save the figure.

    Returns:
        matplotlib.figure.Figure: The created figure object.

    Example:
        >>> df = load_assay_data('data/geochemical_assays.csv')
        >>> fig = plot_element_boxplot(df, ['Au_ppm', 'Ag_ppm', 'Cu_pct'])
        >>> plt.show()
    """
    # TODO: Implement this function
    # Hint:
    # fig, ax = plt.subplots(figsize=(12, 6))
    # df[elements].boxplot(ax=ax)
    # ax.set_ylabel('Concentration')
    # ax.set_title(title or 'Element Distributions')
    pass


def plot_correlation_matrix(df, elements, title=None, save_path=None):
    """
    Create a correlation heatmap for multiple elements.

    Correlation matrices help identify geochemical associations between
    elements, which can indicate mineralization processes.

    Args:
        df (pandas.DataFrame): DataFrame containing assay data.
        elements (list): List of element column names to include.
        title (str, optional): Plot title. If None, auto-generated.
        save_path (str, optional): Path to save the figure.

    Returns:
        matplotlib.figure.Figure: The created figure object.

    Example:
        >>> df = load_assay_data('data/geochemical_assays.csv')
        >>> elements = ['Au_ppm', 'Cu_pct', 'Ag_ppm', 'Fe_pct', 'S_pct']
        >>> fig = plot_correlation_matrix(df, elements)
        >>> plt.show()
    """
    # TODO: Implement this function
    # Hint:
    # corr_matrix = df[elements].corr()
    # fig, ax = plt.subplots(figsize=(10, 8))
    # im = ax.imshow(corr_matrix, cmap='RdYlBu_r', vmin=-1, vmax=1)
    # plt.colorbar(im)
    # ax.set_xticks(range(len(elements)))
    # ax.set_yticks(range(len(elements)))
    # ax.set_xticklabels(elements, rotation=45)
    # ax.set_yticklabels(elements)
    pass


def plot_scatter_with_regression(df, element1, element2, title=None, save_path=None):
    """
    Create a scatter plot with regression line.

    Scatter plots with regression help visualize relationships between
    two elements and quantify the strength of correlation.

    Args:
        df (pandas.DataFrame): DataFrame containing assay data.
        element1 (str): Column name for x-axis element.
        element2 (str): Column name for y-axis element.
        title (str, optional): Plot title. If None, auto-generated.
        save_path (str, optional): Path to save the figure.

    Returns:
        matplotlib.figure.Figure: The created figure object.

    Example:
        >>> df = load_assay_data('data/geochemical_assays.csv')
        >>> fig = plot_scatter_with_regression(df, 'Au_ppm', 'Cu_pct')
        >>> plt.show()
    """
    # TODO: Implement this function
    # Hint:
    # fig, ax = plt.subplots(figsize=(10, 8))
    # clean_df = df[[element1, element2]].dropna()
    # ax.scatter(clean_df[element1], clean_df[element2], alpha=0.5)
    # # Add regression line using np.polyfit
    # z = np.polyfit(clean_df[element1], clean_df[element2], 1)
    # p = np.poly1d(z)
    # ax.plot(clean_df[element1].sort_values(), p(clean_df[element1].sort_values()), 'r-')
    pass


def plot_depth_profile(df, element, hole_id=None, title=None, save_path=None):
    """
    Create a depth profile plot for an element.

    Depth profiles show how element concentration varies with depth,
    which is essential for understanding ore body geometry.

    Args:
        df (pandas.DataFrame): DataFrame containing assay data.
        element (str): Column name for the element to plot.
        hole_id (str, optional): Specific drill hole to plot. If None,
            plots all holes.
        title (str, optional): Plot title. If None, auto-generated.
        save_path (str, optional): Path to save the figure.

    Returns:
        matplotlib.figure.Figure: The created figure object.

    Example:
        >>> df = load_assay_data('data/geochemical_assays.csv')
        >>> fig = plot_depth_profile(df, 'Au_ppm', hole_id='DH-01')
        >>> plt.show()
    """
    # TODO: Implement this function
    # Hint:
    # Plot element values against midpoint depth
    # midpoint = (df['from_depth'] + df['to_depth']) / 2
    # ax.scatter(df[element], midpoint)
    # ax.invert_yaxis()  # Depth increases downward
    pass


def plot_lithology_comparison(df, element, title=None, save_path=None):
    """
    Create a comparison plot of element values by lithology.

    This visualization helps identify which rock types have higher
    element concentrations.

    Args:
        df (pandas.DataFrame): DataFrame containing assay data.
        element (str): Column name for the element to plot.
        title (str, optional): Plot title. If None, auto-generated.
        save_path (str, optional): Path to save the figure.

    Returns:
        matplotlib.figure.Figure: The created figure object.

    Example:
        >>> df = load_assay_data('data/geochemical_assays.csv')
        >>> fig = plot_lithology_comparison(df, 'Au_ppm')
        >>> plt.show()
    """
    # TODO: Implement this function
    # Hint:
    # fig, ax = plt.subplots(figsize=(12, 6))
    # df.boxplot(column=element, by='lithology', ax=ax)
    pass


def plot_anomaly_highlight(df, element, threshold_multiplier, title=None, save_path=None):
    """
    Create a plot highlighting anomalous samples.

    This visualization shows the distribution of element values with
    anomalous samples highlighted, making it easy to identify high-grade
    zones.

    Args:
        df (pandas.DataFrame): DataFrame containing assay data.
        element (str): Column name for the element to plot.
        threshold_multiplier (float): Number of std above mean for anomaly.
        title (str, optional): Plot title. If None, auto-generated.
        save_path (str, optional): Path to save the figure.

    Returns:
        matplotlib.figure.Figure: The created figure object.

    Example:
        >>> df = load_assay_data('data/geochemical_assays.csv')
        >>> fig = plot_anomaly_highlight(df, 'Au_ppm', 2.5)
        >>> plt.show()
    """
    # TODO: Implement this function
    # Hint:
    # Calculate threshold
    # mean_val = df[element].mean()
    # std_val = df[element].std()
    # threshold = mean_val + threshold_multiplier * std_val
    # Plot all points in one color, anomalies in another
    pass


def create_summary_dashboard(df, elements, save_path=None):
    """
    Create a multi-panel summary dashboard.

    This function creates a comprehensive visualization dashboard with
    multiple plots showing different aspects of the geochemical data.

    Args:
        df (pandas.DataFrame): DataFrame containing assay data.
        elements (list): List of element column names to include.
        save_path (str, optional): Path to save the figure.

    Returns:
        matplotlib.figure.Figure: The created figure object.

    Example:
        >>> df = load_assay_data('data/geochemical_assays.csv')
        >>> fig = create_summary_dashboard(df, ['Au_ppm', 'Cu_pct', 'Ag_ppm'])
        >>> plt.show()
    """
    # TODO: Implement this function (optional/advanced)
    # Hint: Use plt.subplots(2, 2) to create a 2x2 grid
    # Include: histogram, boxplot, correlation matrix, scatter
    pass
