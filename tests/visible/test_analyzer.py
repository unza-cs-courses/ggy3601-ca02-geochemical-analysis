"""
Visible tests for Coding Assignment 2: Geochemical Data Analysis.

These tests verify the core functionality of the geochemical analyzer module.
Students can run these tests locally to check their implementations.
"""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path
import sys

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from geochemical_analyzer import (
    load_assay_data,
    filter_by_quality,
    calculate_element_statistics,
    detect_anomalies,
    correlate_elements,
    generate_summary_report
)


class TestLoadAssayData:
    """Tests for the load_assay_data function."""

    def test_load_existing_file(self, sample_data_path):
        """Test loading an existing CSV file."""
        if not sample_data_path.exists():
            pytest.skip("Data file not found")

        df = load_assay_data(str(sample_data_path))

        assert df is not None, "Should return a DataFrame for existing file"
        assert isinstance(df, pd.DataFrame), "Return type should be DataFrame"
        assert len(df) > 0, "DataFrame should not be empty"

    def test_load_nonexistent_file(self, tmp_path):
        """Test loading a file that doesn't exist."""
        fake_path = tmp_path / "nonexistent.csv"
        result = load_assay_data(str(fake_path))

        assert result is None, "Should return None for nonexistent file"

    def test_loaded_columns(self, sample_data_path):
        """Test that loaded DataFrame has expected columns."""
        if not sample_data_path.exists():
            pytest.skip("Data file not found")

        df = load_assay_data(str(sample_data_path))

        expected_columns = ['sample_id', 'hole_id', 'from_depth', 'to_depth',
                           'lithology', 'Au_ppm', 'Cu_pct', 'Ag_ppm',
                           'Fe_pct', 'S_pct', 'sample_quality', 'assay_date']

        for col in expected_columns:
            assert col in df.columns, f"Missing expected column: {col}"


class TestFilterByQuality:
    """Tests for the filter_by_quality function."""

    def test_filter_good_quality(self, sample_dataframe):
        """Test filtering for 'Good' quality samples."""
        result = filter_by_quality(sample_dataframe, 'Good')

        assert result is not None, "Should return a DataFrame"
        assert isinstance(result, pd.DataFrame), "Return type should be DataFrame"
        assert len(result) > 0, "Should have some 'Good' quality samples"
        assert all(result['sample_quality'] == 'Good'), \
            "All samples should have 'Good' quality"

    def test_filter_fair_quality(self, sample_dataframe):
        """Test filtering for 'Fair' quality samples."""
        result = filter_by_quality(sample_dataframe, 'Fair')

        assert result is not None, "Should return a DataFrame"
        if len(result) > 0:
            assert all(result['sample_quality'] == 'Fair'), \
                "All samples should have 'Fair' quality"

    def test_filter_nonexistent_quality(self, sample_dataframe):
        """Test filtering for a quality that doesn't exist."""
        result = filter_by_quality(sample_dataframe, 'Excellent')

        assert result is not None, "Should return a DataFrame (possibly empty)"
        assert len(result) == 0, "Should return empty DataFrame for nonexistent quality"

    def test_filter_preserves_columns(self, sample_dataframe):
        """Test that filtering preserves all columns."""
        result = filter_by_quality(sample_dataframe, 'Good')

        assert list(result.columns) == list(sample_dataframe.columns), \
            "Filtered DataFrame should have same columns"


class TestCalculateElementStatistics:
    """Tests for the calculate_element_statistics function."""

    def test_returns_dictionary(self, sample_dataframe):
        """Test that function returns a dictionary."""
        result = calculate_element_statistics(sample_dataframe, 'Au_ppm')

        assert result is not None, "Should return a result"
        assert isinstance(result, dict), "Return type should be dictionary"

    def test_required_keys(self, sample_dataframe):
        """Test that result contains all required keys."""
        result = calculate_element_statistics(sample_dataframe, 'Au_ppm')

        required_keys = ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']
        for key in required_keys:
            assert key in result, f"Missing required key: {key}"

    def test_count_excludes_nan(self, sample_dataframe):
        """Test that count excludes NaN values."""
        result = calculate_element_statistics(sample_dataframe, 'Au_ppm')

        # Count should be less than total rows if there are NaN values
        nan_count = sample_dataframe['Au_ppm'].isna().sum()
        expected_count = len(sample_dataframe) - nan_count

        assert result['count'] == expected_count, \
            f"Count should be {expected_count}, got {result['count']}"

    def test_mean_calculation(self, sample_dataframe):
        """Test that mean is calculated correctly."""
        result = calculate_element_statistics(sample_dataframe, 'Au_ppm')
        expected_mean = sample_dataframe['Au_ppm'].mean()

        assert abs(result['mean'] - expected_mean) < 0.001, \
            f"Mean should be approximately {expected_mean}"

    def test_statistics_for_different_elements(self, sample_dataframe):
        """Test calculating statistics for different elements."""
        elements = ['Au_ppm', 'Cu_pct', 'Fe_pct']

        for element in elements:
            result = calculate_element_statistics(sample_dataframe, element)
            assert result is not None, f"Should return stats for {element}"
            assert 'mean' in result, f"Should have mean for {element}"


class TestDetectAnomalies:
    """Tests for the detect_anomalies function."""

    def test_returns_dataframe(self, sample_dataframe):
        """Test that function returns a DataFrame."""
        result = detect_anomalies(sample_dataframe, 'Au_ppm', 2.0)

        assert result is not None, "Should return a result"
        assert isinstance(result, pd.DataFrame), "Return type should be DataFrame"

    def test_anomalies_exceed_threshold(self, sample_dataframe):
        """Test that all returned samples exceed the threshold."""
        threshold_multiplier = 2.0
        result = detect_anomalies(sample_dataframe, 'Au_ppm', threshold_multiplier)

        if len(result) > 0:
            mean_val = sample_dataframe['Au_ppm'].mean()
            std_val = sample_dataframe['Au_ppm'].std()
            threshold = mean_val + threshold_multiplier * std_val

            assert all(result['Au_ppm'] > threshold), \
                "All anomalies should exceed the threshold"

    def test_higher_threshold_fewer_anomalies(self, sample_dataframe):
        """Test that higher threshold results in fewer anomalies."""
        result_low = detect_anomalies(sample_dataframe, 'Au_ppm', 1.5)
        result_high = detect_anomalies(sample_dataframe, 'Au_ppm', 3.0)

        assert len(result_high) <= len(result_low), \
            "Higher threshold should result in fewer or equal anomalies"

    def test_preserves_columns(self, sample_dataframe):
        """Test that anomaly detection preserves all columns."""
        result = detect_anomalies(sample_dataframe, 'Au_ppm', 2.0)

        if len(result) > 0:
            assert list(result.columns) == list(sample_dataframe.columns), \
                "Anomalies DataFrame should have same columns"


class TestCorrelateElements:
    """Tests for the correlate_elements function."""

    def test_returns_float(self, sample_dataframe):
        """Test that function returns a float."""
        result = correlate_elements(sample_dataframe, 'Au_ppm', 'Cu_pct')

        assert result is not None, "Should return a result"
        assert isinstance(result, (float, np.floating)), "Return type should be float"

    def test_correlation_range(self, sample_dataframe):
        """Test that correlation is between -1 and 1."""
        result = correlate_elements(sample_dataframe, 'Au_ppm', 'Cu_pct')

        assert -1 <= result <= 1, "Correlation should be between -1 and 1"

    def test_self_correlation(self, sample_dataframe):
        """Test that correlation with itself is 1."""
        result = correlate_elements(sample_dataframe, 'Au_ppm', 'Au_ppm')

        assert abs(result - 1.0) < 0.001, "Self-correlation should be 1"

    def test_correlation_symmetry(self, sample_dataframe):
        """Test that correlation is symmetric."""
        result_ab = correlate_elements(sample_dataframe, 'Au_ppm', 'Cu_pct')
        result_ba = correlate_elements(sample_dataframe, 'Cu_pct', 'Au_ppm')

        assert abs(result_ab - result_ba) < 0.001, \
            "Correlation should be symmetric"


class TestGenerateSummaryReport:
    """Tests for the generate_summary_report function."""

    def test_returns_dictionary(self, sample_dataframe):
        """Test that function returns a dictionary."""
        elements = ['Au_ppm', 'Cu_pct']
        result = generate_summary_report(sample_dataframe, elements)

        assert result is not None, "Should return a result"
        assert isinstance(result, dict), "Return type should be dictionary"

    def test_contains_all_elements(self, sample_dataframe):
        """Test that report contains all requested elements."""
        elements = ['Au_ppm', 'Cu_pct', 'Ag_ppm']
        result = generate_summary_report(sample_dataframe, elements)

        for elem in elements:
            assert elem in result, f"Report should contain {elem}"

    def test_element_report_structure(self, sample_dataframe):
        """Test that each element report has expected structure."""
        elements = ['Au_ppm']
        result = generate_summary_report(sample_dataframe, elements)

        element_report = result['Au_ppm']

        # Should have basic statistics
        assert 'mean' in element_report, "Should have mean"
        assert 'std' in element_report, "Should have std"
        assert 'min' in element_report, "Should have min"
        assert 'max' in element_report, "Should have max"

    def test_missing_value_count(self, sample_dataframe):
        """Test that report includes missing value count."""
        elements = ['Au_ppm']
        result = generate_summary_report(sample_dataframe, elements)

        element_report = result['Au_ppm']

        # Should have missing value count
        assert 'missing' in element_report or 'count' in element_report, \
            "Should include missing value information"


class TestDataIntegrity:
    """Tests for data integrity and edge cases."""

    def test_handles_empty_dataframe(self, empty_dataframe):
        """Test that functions handle empty DataFrame gracefully."""
        # These should not raise exceptions
        try:
            filter_by_quality(empty_dataframe, 'Good')
        except Exception as e:
            # It's okay if it returns None or empty, but shouldn't crash badly
            pass

    def test_handles_missing_column(self, sample_dataframe):
        """Test behavior when element column doesn't exist."""
        # This test checks if the function handles missing columns
        # Implementation may vary - could return None or raise specific error
        try:
            result = calculate_element_statistics(sample_dataframe, 'Nonexistent_ppm')
            # If it returns something, should be None or indicate error
        except KeyError:
            # KeyError is acceptable behavior
            pass
        except Exception as e:
            pytest.fail(f"Unexpected exception: {e}")


class TestVariantParameters:
    """Tests using variant-specific parameters."""

    def test_primary_element_stats(self, sample_dataframe, primary_element):
        """Test statistics calculation with variant's primary element."""
        result = calculate_element_statistics(sample_dataframe, primary_element)

        assert result is not None, \
            f"Should calculate stats for primary element {primary_element}"
        assert 'mean' in result, "Should have mean in statistics"

    def test_quality_filter_with_variant(self, sample_dataframe, quality_filter):
        """Test quality filter with variant's parameter."""
        result = filter_by_quality(sample_dataframe, quality_filter)

        assert result is not None, \
            f"Should filter by quality level '{quality_filter}'"

    def test_anomaly_detection_with_variant(self, sample_dataframe,
                                            primary_element, anomaly_threshold):
        """Test anomaly detection with variant's parameters."""
        result = detect_anomalies(sample_dataframe, primary_element, anomaly_threshold)

        assert result is not None, \
            f"Should detect anomalies with threshold {anomaly_threshold}"
        assert isinstance(result, pd.DataFrame), "Should return DataFrame"
