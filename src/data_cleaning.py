"""
GGY3601 Coding Assignment 2: Data Cleaning Module

This module provides utilities for cleaning and preprocessing geochemical data.

Author: [YOUR NAME]
Student ID: [YOUR ID]
Date: [DATE]
"""

import pandas as pd
import numpy as np


def handle_missing_values(df, strategy='drop', columns=None):
    """
    Handle missing values in the DataFrame.

    This function provides multiple strategies for dealing with missing (NaN)
    values in geochemical data. The appropriate strategy depends on the
    analysis requirements and the nature of the missing data.

    Args:
        df (pandas.DataFrame): DataFrame containing assay data.
        strategy (str): Strategy for handling missing values:
            - 'drop': Remove rows with any missing values
            - 'mean': Replace missing values with column mean
            - 'median': Replace missing values with column median
            - 'zero': Replace missing values with 0
        columns (list, optional): List of columns to apply the strategy to.
            If None, applies to all numeric columns.

    Returns:
        pandas.DataFrame: DataFrame with missing values handled according
            to the specified strategy.

    Example:
        >>> df = load_assay_data('data/geochemical_assays.csv')
        >>> print(f"Before: {df['Au_ppm'].isna().sum()} missing")
        >>> df_clean = handle_missing_values(df, strategy='median')
        >>> print(f"After: {df_clean['Au_ppm'].isna().sum()} missing")
    """
    # TODO: Implement this function
    # Hint:
    # - For 'drop': Use df.dropna()
    # - For 'mean': Use df.fillna(df.mean())
    # - For 'median': Use df.fillna(df.median())
    # - For 'zero': Use df.fillna(0)
    pass


def remove_outliers(df, element, method='iqr', threshold=1.5):
    """
    Remove statistical outliers from the data.

    This function identifies and removes outliers using either the
    Interquartile Range (IQR) method or Z-score method. Outliers in
    geochemical data may represent errors or genuine anomalies - careful
    consideration is needed before removing them.

    Args:
        df (pandas.DataFrame): DataFrame containing assay data.
        element (str): Column name for the element to check for outliers.
        method (str): Method for detecting outliers:
            - 'iqr': Interquartile Range method (Q1 - 1.5*IQR to Q3 + 1.5*IQR)
            - 'zscore': Z-score method (values beyond threshold std from mean)
        threshold (float): Threshold for outlier detection:
            - For 'iqr': IQR multiplier (default 1.5)
            - For 'zscore': Number of standard deviations (default 3.0)

    Returns:
        pandas.DataFrame: DataFrame with outliers removed.

    Example:
        >>> df = load_assay_data('data/geochemical_assays.csv')
        >>> print(f"Before: {len(df)} samples")
        >>> df_clean = remove_outliers(df, 'Au_ppm', method='iqr')
        >>> print(f"After: {len(df_clean)} samples")
    """
    # TODO: Implement this function
    # Hint for IQR method:
    # Q1 = df[element].quantile(0.25)
    # Q3 = df[element].quantile(0.75)
    # IQR = Q3 - Q1
    # lower_bound = Q1 - threshold * IQR
    # upper_bound = Q3 + threshold * IQR
    # Filter: df[(df[element] >= lower_bound) & (df[element] <= upper_bound)]
    pass


def validate_data_quality(df):
    """
    Check for data quality issues in the assay data.

    This function performs comprehensive data quality checks and returns
    a report of any issues found. This is essential for ensuring reliable
    geochemical analysis.

    Args:
        df (pandas.DataFrame): DataFrame containing assay data.

    Returns:
        dict: Data quality report containing:
            - 'total_rows': Total number of samples
            - 'missing_values': Dict of column names to missing value counts
            - 'duplicate_ids': List of duplicate sample IDs
            - 'negative_values': Dict of columns with negative values and counts
            - 'invalid_depths': Count of samples where from_depth >= to_depth
            - 'rejected_samples': Count of samples with 'Rejected' quality
            - 'issues_found': Boolean indicating if any issues were found

    Example:
        >>> df = load_assay_data('data/geochemical_assays.csv')
        >>> report = validate_data_quality(df)
        >>> if report['issues_found']:
        ...     print("Data quality issues detected!")
        ...     for col, count in report['missing_values'].items():
        ...         if count > 0:
        ...             print(f"  {col}: {count} missing values")
    """
    # TODO: Implement this function
    # Hint: Check for various issues and compile into a report dictionary
    pass


def standardize_lithology_names(df):
    """
    Standardize lithology names to consistent format.

    Geochemical data often contains inconsistent naming (e.g., 'granite',
    'Granite', 'GRANITE'). This function standardizes all lithology names
    to title case.

    Args:
        df (pandas.DataFrame): DataFrame containing assay data with
            'lithology' column.

    Returns:
        pandas.DataFrame: DataFrame with standardized lithology names.

    Example:
        >>> df = load_assay_data('data/geochemical_assays.csv')
        >>> df_clean = standardize_lithology_names(df)
        >>> print(df_clean['lithology'].unique())
    """
    # TODO: Implement this function
    # Hint: Use df['lithology'].str.title()
    pass


def filter_by_depth_range(df, min_depth=None, max_depth=None):
    """
    Filter samples by depth range.

    This function filters the DataFrame to include only samples within
    the specified depth range. Useful for focusing analysis on specific
    geological intervals.

    Args:
        df (pandas.DataFrame): DataFrame containing assay data.
        min_depth (float, optional): Minimum depth to include.
            If None, no minimum filter is applied.
        max_depth (float, optional): Maximum depth to include.
            If None, no maximum filter is applied.

    Returns:
        pandas.DataFrame: Filtered DataFrame containing samples within
            the specified depth range.

    Example:
        >>> df = load_assay_data('data/geochemical_assays.csv')
        >>> shallow = filter_by_depth_range(df, max_depth=100)
        >>> deep = filter_by_depth_range(df, min_depth=300)
    """
    # TODO: Implement this function
    # Hint: Apply conditional filtering based on from_depth and to_depth
    pass


def calculate_sample_interval(df):
    """
    Calculate sample interval length for each sample.

    Adds a new column 'interval_length' representing the length of each
    sample interval (to_depth - from_depth). This is useful for weighted
    average calculations.

    Args:
        df (pandas.DataFrame): DataFrame containing assay data with
            'from_depth' and 'to_depth' columns.

    Returns:
        pandas.DataFrame: DataFrame with added 'interval_length' column.

    Example:
        >>> df = load_assay_data('data/geochemical_assays.csv')
        >>> df = calculate_sample_interval(df)
        >>> print(f"Average interval: {df['interval_length'].mean():.2f} m")
    """
    # TODO: Implement this function
    # Hint: df['interval_length'] = df['to_depth'] - df['from_depth']
    pass


def merge_adjacent_samples(df, element, max_gap=0.5):
    """
    Identify adjacent samples that could be composited.

    This function identifies samples that are adjacent (no gap between
    to_depth of one and from_depth of next) within the same drill hole.
    These could potentially be composited for grade calculations.

    Args:
        df (pandas.DataFrame): DataFrame containing assay data.
        element (str): Element column for composite calculation.
        max_gap (float): Maximum gap between samples to consider adjacent.

    Returns:
        pandas.DataFrame: DataFrame with composite information added.

    Example:
        >>> df = load_assay_data('data/geochemical_assays.csv')
        >>> composites = merge_adjacent_samples(df, 'Au_ppm')
    """
    # TODO: Implement this function (optional/advanced)
    # This is an advanced function - implement if you have time
    pass


def export_clean_data(df, filename, format='csv'):
    """
    Export cleaned data to a file.

    Args:
        df (pandas.DataFrame): DataFrame to export.
        filename (str): Output filename.
        format (str): Output format ('csv' or 'excel').

    Returns:
        bool: True if export successful, False otherwise.

    Example:
        >>> df = load_assay_data('data/geochemical_assays.csv')
        >>> df_clean = handle_missing_values(df, strategy='drop')
        >>> export_clean_data(df_clean, 'data/cleaned_assays.csv')
    """
    # TODO: Implement this function
    # Hint:
    # - For 'csv': Use df.to_csv(filename, index=False)
    # - For 'excel': Use df.to_excel(filename, index=False)
    pass
