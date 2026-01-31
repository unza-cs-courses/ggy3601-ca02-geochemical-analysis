"""
GGY3601 Coding Assignment 2: Main Program

This is the main entry point for the geochemical data analysis.
Run this script to perform the complete analysis workflow.

Author: [YOUR NAME]
Student ID: [YOUR ID]
Date: [DATE]
"""

import sys
from pathlib import Path

# Add src directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

# Import analysis modules
from geochemical_analyzer import (
    load_assay_data,
    filter_by_quality,
    calculate_element_statistics,
    detect_anomalies,
    correlate_elements,
    generate_summary_report
)
from data_cleaning import (
    handle_missing_values,
    validate_data_quality
)
from visualization import (
    plot_element_histogram,
    plot_correlation_matrix
)


def main():
    """
    Main analysis workflow for geochemical data.

    This function demonstrates the complete workflow for analyzing
    geochemical assay data, including:
    1. Loading and exploring data
    2. Quality filtering
    3. Statistical analysis
    4. Anomaly detection
    5. Correlation analysis
    6. Generating summary reports
    """
    print("=" * 60)
    print("GGY3601 Coding Assignment 2: Geochemical Data Analysis")
    print("=" * 60)

    # =========================================================================
    # Step 1: Load the data
    # =========================================================================
    print("\n--- Step 1: Loading Data ---")

    data_path = Path(__file__).parent.parent / "data" / "geochemical_assays.csv"
    df = load_assay_data(str(data_path))

    if df is None:
        print(f"ERROR: Could not load data from {data_path}")
        return

    print(f"Loaded {len(df)} assay records")
    print(f"Columns: {list(df.columns)}")

    # =========================================================================
    # Step 2: Explore the data
    # =========================================================================
    print("\n--- Step 2: Data Exploration ---")

    # TODO: Add your data exploration code here
    # Examples:
    # print(df.head())
    # print(df.info())
    # print(df.describe())

    # =========================================================================
    # Step 3: Validate data quality
    # =========================================================================
    print("\n--- Step 3: Data Quality Check ---")

    quality_report = validate_data_quality(df)
    if quality_report:
        # TODO: Print quality report findings
        pass

    # =========================================================================
    # Step 4: Filter by quality
    # =========================================================================
    print("\n--- Step 4: Quality Filtering ---")

    # TODO: Use YOUR quality_filter parameter from ASSIGNMENT.md
    quality_filter = "Good"  # Replace with your parameter
    good_samples = filter_by_quality(df, quality_filter)

    if good_samples is not None:
        print(f"Filtered to {len(good_samples)} '{quality_filter}' quality samples")

    # =========================================================================
    # Step 5: Calculate element statistics
    # =========================================================================
    print("\n--- Step 5: Element Statistics ---")

    # TODO: Use YOUR primary_element parameter from ASSIGNMENT.md
    primary_element = "Au_ppm"  # Replace with your parameter

    stats = calculate_element_statistics(df, primary_element)
    if stats:
        print(f"\nStatistics for {primary_element}:")
        for key, value in stats.items():
            if isinstance(value, float):
                print(f"  {key}: {value:.4f}")
            else:
                print(f"  {key}: {value}")

    # =========================================================================
    # Step 6: Detect anomalies
    # =========================================================================
    print("\n--- Step 6: Anomaly Detection ---")

    # TODO: Use YOUR anomaly_threshold_multiplier from ASSIGNMENT.md
    threshold_multiplier = 2.5  # Replace with your parameter

    anomalies = detect_anomalies(df, primary_element, threshold_multiplier)
    if anomalies is not None:
        print(f"Found {len(anomalies)} anomalous samples")
        if len(anomalies) > 0:
            print("\nTop anomalies:")
            # TODO: Display top anomalies

    # =========================================================================
    # Step 7: Calculate correlations
    # =========================================================================
    print("\n--- Step 7: Element Correlations ---")

    elements = ["Au_ppm", "Cu_pct", "Ag_ppm", "Fe_pct", "S_pct"]

    print("\nCorrelation matrix:")
    for i, elem1 in enumerate(elements):
        for elem2 in elements[i+1:]:
            corr = correlate_elements(df, elem1, elem2)
            if corr is not None:
                print(f"  {elem1} vs {elem2}: {corr:.3f}")

    # =========================================================================
    # Step 8: Generate summary report
    # =========================================================================
    print("\n--- Step 8: Summary Report ---")

    report = generate_summary_report(df, elements)
    if report:
        print("\nSummary Report:")
        for elem, elem_report in report.items():
            print(f"\n{elem}:")
            for key, value in elem_report.items():
                if isinstance(value, float):
                    print(f"    {key}: {value:.4f}")
                else:
                    print(f"    {key}: {value}")

    # =========================================================================
    # Step 9: Create visualizations (optional)
    # =========================================================================
    print("\n--- Step 9: Visualizations ---")

    # TODO: Create visualizations using functions from visualization.py
    # Note: Uncomment and modify these lines when you implement the functions

    # plot_element_histogram(df, primary_element)
    # plot_correlation_matrix(df, elements)

    print("Visualization functions available but not displayed in this run.")
    print("Uncomment visualization code to generate plots.")

    # =========================================================================
    # Analysis complete
    # =========================================================================
    print("\n" + "=" * 60)
    print("Analysis Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
