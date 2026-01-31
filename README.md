# GGY3601 Coding Assignment 2: Geochemical Data Analysis

**Weight:** 15% of final grade
**Due:** Week 10
**Estimated Time:** 8-12 hours

## Purpose

This assignment develops your skills in using pandas for real-world geochemical data analysis. You will work with assay data to perform statistical analysis, handle missing values, detect anomalies, and create meaningful visualizations.

## Learning Outcomes

By completing this assignment, you will be able to:
- LO5.1: Use pandas to load and explore geochemical datasets
- LO5.2: Handle missing values and data quality issues appropriately
- LO5.3: Perform statistical analysis and groupby operations
- LO5.4: Detect geochemical anomalies using statistical methods
- LO5.5: Create meaningful visualizations for geochemical data
- LO5.6: Calculate element correlations and interpret results

## Your Personalized Assignment

**See `ASSIGNMENT.md` for your unique parameters and test values.**

The ASSIGNMENT.md file contains your student-specific values including:
- Primary element to analyze
- Secondary elements for correlation analysis
- Quality filter level
- Anomaly detection threshold multiplier
- Number of assay records

## Repository Structure

```
.
├── src/
│   ├── geochemical_analyzer.py  # Main analysis module (COMPLETE THIS)
│   ├── data_cleaning.py         # Data cleaning utilities (COMPLETE THIS)
│   ├── visualization.py         # Plotting functions (COMPLETE THIS)
│   └── main.py                  # Main program
├── tests/
│   └── visible/                 # Automated tests (visible to you)
├── data/
│   └── geochemical_assays.csv   # Assay data to analyze
├── ASSIGNMENT.md                # Your unique assignment parameters
└── README.md                    # This file
```

## Dataset Description

The `geochemical_assays.csv` file contains drill core assay data with the following columns:

| Column | Description | Units |
|--------|-------------|-------|
| sample_id | Unique sample identifier | - |
| hole_id | Drill hole identifier | - |
| from_depth | Sample interval start | meters |
| to_depth | Sample interval end | meters |
| lithology | Rock type | - |
| Au_ppm | Gold concentration | parts per million |
| Cu_pct | Copper concentration | percent |
| Ag_ppm | Silver concentration | parts per million |
| Fe_pct | Iron concentration | percent |
| S_pct | Sulfur concentration | percent |
| sample_quality | QA/QC classification | Good/Fair/Rejected |
| assay_date | Date of analysis | YYYY-MM-DD |

Note: The dataset contains missing values and quality control issues that you must handle appropriately.

## Tasks Overview

### Task 1: Data Loading and Exploration (15 marks)
Implement `load_assay_data()` function that:
- Loads the CSV file using pandas
- Returns a DataFrame
- Handles the case where file doesn't exist

### Task 2: Quality Filtering (15 marks)
Implement `filter_by_quality()` function that:
- Filters DataFrame by sample_quality column
- Returns only rows matching the specified quality level
- Handles empty results gracefully

### Task 3: Element Statistics (20 marks)
Implement `calculate_element_statistics()` function that:
- Calculates descriptive statistics for a specified element
- Uses pandas describe() method
- Handles missing values appropriately
- Returns a dictionary with count, mean, std, min, 25%, 50%, 75%, max

### Task 4: Anomaly Detection (20 marks)
Implement `detect_anomalies()` function that:
- Identifies samples where element value exceeds mean + (threshold_multiplier * std)
- Returns a DataFrame of anomalous samples
- Works with missing values in the element column

### Task 5: Element Correlation (15 marks)
Implement `correlate_elements()` function that:
- Calculates Pearson correlation between two elements
- Returns the correlation coefficient
- Handles missing values appropriately

### Task 6: Summary Report (15 marks)
Implement `generate_summary_report()` function that:
- Creates a comprehensive summary for multiple elements
- Includes statistics, missing value counts, and anomaly counts
- Returns a formatted dictionary or DataFrame

## Getting Started

1. Clone this repository to your local machine
2. Read `ASSIGNMENT.md` for your unique values
3. Explore the data file: `data/geochemical_assays.csv`
4. Complete each function in `src/geochemical_analyzer.py`
5. Implement data cleaning utilities in `src/data_cleaning.py`
6. Create visualization functions in `src/visualization.py`
7. Run tests locally: `pytest tests/visible/ -v`
8. Push your code to see automated test results

## Key Pandas Operations to Use

- `pd.read_csv()` - Loading data
- `df.describe()` - Summary statistics
- `df.groupby()` - Grouped analysis
- `df.isna()` / `df.dropna()` / `df.fillna()` - Missing value handling
- `df.corr()` - Correlation matrix
- `df[condition]` - Boolean filtering
- `df['column'].mean()`, `.std()` - Statistical calculations

## Example Code Snippets

```python
import pandas as pd

# Loading data
df = pd.read_csv('data/geochemical_assays.csv')

# Basic exploration
print(df.head())
print(df.info())
print(df.describe())

# Filtering by quality
good_samples = df[df['sample_quality'] == 'Good']

# Calculating statistics
au_mean = df['Au_ppm'].mean()
au_std = df['Au_ppm'].std()

# Detecting anomalies (values > mean + 2*std)
threshold = au_mean + 2 * au_std
anomalies = df[df['Au_ppm'] > threshold]

# Correlation between elements
correlation = df['Au_ppm'].corr(df['Cu_pct'])
```

## Submission Requirements

1. All functions in `src/geochemical_analyzer.py` must be implemented
2. All visible tests must pass
3. Code must be well-documented with comments
4. Push your final code before the deadline

## Grading

| Component | Weight |
|-----------|--------|
| Visible Tests | 70% |
| Hidden Tests | 20% |
| Code Quality | 10% |

## Academic Integrity

- **ALLOWED:** Lecture notes, official pandas documentation, asking tutors
- **NOT ALLOWED:** Copying code, AI tools, sharing solutions

All submissions are checked with plagiarism detection software. Your variant parameters are unique to you, making copied solutions easy to detect.
