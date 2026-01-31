# Your Assignment Parameters

These are your unique values for Coding Assignment 2. Use these exact values in your code.

## Your Configuration

| Parameter | Your Value |
|-----------|------------|
| Primary Element | {primary_element} |
| Secondary Elements | {secondary_elements} |
| Quality Filter | {quality_filter} |
| Anomaly Threshold Multiplier | {anomaly_threshold_multiplier} |
| Number of Assays | {num_assays} |

## Task 1: Data Loading and Exploration (15 marks)

Implement the `load_assay_data()` function in `src/geochemical_analyzer.py`:

```python
def load_assay_data(filename):
    """
    Load geochemical assay data from a CSV file.

    Args:
        filename: Path to the CSV file

    Returns:
        pandas DataFrame containing the assay data
        None if the file doesn't exist
    """
    # YOUR CODE HERE
    pass
```

**Requirements:**
- Use pandas `read_csv()` to load the data
- Handle FileNotFoundError gracefully (return None)
- The loaded DataFrame should have {num_assays} records

## Task 2: Quality Filtering (15 marks)

Implement the `filter_by_quality()` function:

```python
def filter_by_quality(df, quality_level):
    """
    Filter assay data by sample quality.

    Args:
        df: pandas DataFrame with assay data
        quality_level: Quality level to filter by (e.g., '{quality_filter}')

    Returns:
        Filtered DataFrame containing only rows matching the quality level
    """
    # YOUR CODE HERE
    pass
```

**Requirements:**
- Filter the DataFrame where `sample_quality` equals `quality_level`
- Your primary quality filter is: **{quality_filter}**
- Return the filtered DataFrame

## Task 3: Element Statistics (20 marks)

Implement the `calculate_element_statistics()` function:

```python
def calculate_element_statistics(df, element):
    """
    Calculate descriptive statistics for a specific element.

    Args:
        df: pandas DataFrame with assay data
        element: Column name for the element (e.g., '{primary_element}_ppm' or '{primary_element}_pct')

    Returns:
        Dictionary with keys: 'count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'
    """
    # YOUR CODE HERE
    pass
```

**Requirements:**
- Your primary element is: **{primary_element}**
- Use pandas `describe()` method
- Handle missing values (they should be excluded from statistics)
- Return a dictionary with the statistics

**Example for {primary_element}:**
```python
stats = calculate_element_statistics(df, '{primary_element}_ppm')
# or for Cu, Fe, S which are in percent:
# stats = calculate_element_statistics(df, 'Cu_pct')
```

## Task 4: Anomaly Detection (20 marks)

Implement the `detect_anomalies()` function:

```python
def detect_anomalies(df, element, threshold_multiplier):
    """
    Detect geochemical anomalies using statistical threshold.

    An anomaly is defined as: value > mean + (threshold_multiplier * std)

    Args:
        df: pandas DataFrame with assay data
        element: Column name for the element
        threshold_multiplier: Number of standard deviations above mean

    Returns:
        DataFrame containing only anomalous samples
    """
    # YOUR CODE HERE
    pass
```

**Requirements:**
- Your anomaly threshold multiplier is: **{anomaly_threshold_multiplier}**
- Calculate mean and standard deviation (excluding NaN values)
- Threshold = mean + ({anomaly_threshold_multiplier} * std)
- Return DataFrame with samples exceeding the threshold

**Example:**
```python
anomalies = detect_anomalies(df, '{primary_element}_ppm', {anomaly_threshold_multiplier})
```

## Task 5: Element Correlation (15 marks)

Implement the `correlate_elements()` function:

```python
def correlate_elements(df, element1, element2):
    """
    Calculate Pearson correlation coefficient between two elements.

    Args:
        df: pandas DataFrame with assay data
        element1: First element column name
        element2: Second element column name

    Returns:
        Float: Pearson correlation coefficient (-1 to 1)
    """
    # YOUR CODE HERE
    pass
```

**Requirements:**
- Your secondary elements for correlation are: **{secondary_elements}**
- Use pandas `corr()` method
- Handle missing values appropriately
- Return a single float value

**Example:**
```python
# Analyze correlation between your primary and secondary elements
correlation = correlate_elements(df, '{primary_element}_ppm', 'Cu_pct')
```

## Task 6: Summary Report (15 marks)

Implement the `generate_summary_report()` function:

```python
def generate_summary_report(df, elements):
    """
    Generate a comprehensive summary report for multiple elements.

    Args:
        df: pandas DataFrame with assay data
        elements: List of element column names

    Returns:
        Dictionary with element names as keys and summary statistics as values
    """
    # YOUR CODE HERE
    pass
```

**Requirements:**
- Include statistics for each element
- Include count of missing values for each element
- Include count of anomalies (using your threshold: {anomaly_threshold_multiplier})
- Return a nested dictionary structure

**Example:**
```python
elements = ['{primary_element}_ppm', 'Cu_pct', 'Ag_ppm']
report = generate_summary_report(df, elements)
```

## Data Cleaning Module

In `src/data_cleaning.py`, implement the following helper functions:

### `handle_missing_values(df, strategy='drop')`
- Handle missing values in the DataFrame
- Support strategies: 'drop', 'mean', 'median', 'zero'

### `remove_outliers(df, element, method='iqr')`
- Remove statistical outliers from the data
- Support methods: 'iqr' (Interquartile Range), 'zscore'

### `validate_data_quality(df)`
- Check for data quality issues
- Return a report of issues found

## Visualization Module

In `src/visualization.py`, implement plotting functions:

### `plot_element_histogram(df, element, bins=30)`
- Create a histogram of element values

### `plot_element_boxplot(df, elements)`
- Create box plots for multiple elements

### `plot_correlation_matrix(df, elements)`
- Create a correlation heatmap

### `plot_scatter_with_regression(df, element1, element2)`
- Create a scatter plot with regression line

## Testing Your Code

Run the automated tests locally:

```bash
# Run all visible tests
pytest tests/visible/ -v

# Run specific test file
pytest tests/visible/test_analyzer.py -v

# Run with coverage
pytest tests/visible/ -v --cov=src
```

## Tips for Success

1. **Start with data exploration:**
   ```python
   df = pd.read_csv('data/geochemical_assays.csv')
   print(df.head())
   print(df.info())
   print(df.isna().sum())
   ```

2. **Understand the element column naming:**
   - Gold (Au): `Au_ppm` (parts per million)
   - Copper (Cu): `Cu_pct` (percent)
   - Silver (Ag): `Ag_ppm`
   - Iron (Fe): `Fe_pct`
   - Sulfur (S): `S_pct`

3. **Handle missing values consistently:**
   ```python
   # Check for missing values
   df['Au_ppm'].isna().sum()

   # Calculate statistics excluding NaN
   df['Au_ppm'].mean()  # pandas excludes NaN by default
   ```

4. **Use your unique parameters:**
   - Primary element: {primary_element}
   - Threshold multiplier: {anomaly_threshold_multiplier}
   - Quality filter: {quality_filter}

## Submission Checklist

- [ ] `load_assay_data()` implemented and tested
- [ ] `filter_by_quality()` implemented and tested
- [ ] `calculate_element_statistics()` implemented and tested
- [ ] `detect_anomalies()` implemented and tested
- [ ] `correlate_elements()` implemented and tested
- [ ] `generate_summary_report()` implemented and tested
- [ ] Data cleaning functions implemented
- [ ] Visualization functions implemented
- [ ] All visible tests pass
- [ ] Code is well-documented with comments
- [ ] Pushed to GitHub before deadline
