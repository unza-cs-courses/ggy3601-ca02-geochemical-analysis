"""
Pytest configuration for Coding Assignment 2 visible tests.
Loads variant configuration and provides test fixtures.
"""

import json
import pytest
import pandas as pd
from pathlib import Path
import sys

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))


@pytest.fixture(scope="session")
def variant_config():
    """Load student's variant configuration."""
    config_path = Path(__file__).parent.parent.parent / ".variant_config.json"
    if config_path.exists():
        with open(config_path) as f:
            return json.load(f)
    # Default values for testing without variant config
    return {
        "parameters": {
            "primary_element": "Au",
            "secondary_elements": ["Cu", "Ag", "Fe"],
            "quality_filter": "Good",
            "anomaly_threshold_multiplier": 2.5,
            "num_assays": 500
        }
    }


@pytest.fixture(scope="session")
def data_path():
    """Return path to the data directory."""
    return Path(__file__).parent.parent.parent / "data"


@pytest.fixture(scope="session")
def sample_data_path(data_path):
    """Return path to the sample assay data file."""
    return data_path / "geochemical_assays.csv"


@pytest.fixture(scope="session")
def sample_dataframe(sample_data_path):
    """Load and return the sample DataFrame for testing."""
    if sample_data_path.exists():
        return pd.read_csv(sample_data_path)
    # Create a small test DataFrame if file doesn't exist
    return pd.DataFrame({
        'sample_id': [f'TEST-{i:04d}' for i in range(1, 21)],
        'hole_id': ['DH-01'] * 10 + ['DH-02'] * 10,
        'from_depth': list(range(0, 100, 5)) + list(range(0, 100, 5)),
        'to_depth': list(range(5, 105, 5)) + list(range(5, 105, 5)),
        'lithology': ['Granite'] * 8 + ['Basalt'] * 12,
        'Au_ppm': [0.5, 1.2, 0.8, 2.5, None, 0.3, 5.5, 1.1, 0.9, 1.5,
                   0.4, 0.6, 1.8, 0.7, 3.2, None, 0.5, 1.3, 0.8, 2.1],
        'Cu_pct': [0.3, 0.8, 0.5, 1.2, 0.4, None, 2.1, 0.6, 0.7, 0.9,
                   0.2, 0.4, 1.0, 0.3, 1.5, 0.6, None, 0.8, 0.5, 1.1],
        'Ag_ppm': [2.5, 5.0, 3.5, 8.0, 2.0, 1.5, 12.0, 4.0, 3.0, 5.5,
                   1.5, 2.0, 6.0, 2.5, 9.0, 3.5, 2.0, None, 3.5, 7.0],
        'Fe_pct': [5.0, 6.2, 5.5, 7.0, 4.8, 5.3, 8.0, 5.8, 6.0, 6.5,
                   4.5, 5.0, 6.8, 5.2, 7.5, 6.0, 5.5, 6.3, 5.8, 7.2],
        'S_pct': [1.0, 1.5, 1.2, 2.0, 0.8, 1.1, 2.5, 1.3, 1.4, 1.6,
                  0.7, 0.9, 1.8, 1.0, 2.2, 1.4, 1.2, 1.5, 1.3, 1.9],
        'sample_quality': ['Good'] * 12 + ['Fair'] * 5 + ['Rejected'] * 3,
        'assay_date': ['2024-01-15'] * 20
    })


@pytest.fixture
def primary_element(variant_config):
    """Return the primary element for analysis."""
    elem = variant_config["parameters"]["primary_element"]
    # Map to column name
    if elem in ['Au', 'Ag']:
        return f"{elem}_ppm"
    else:
        return f"{elem}_pct"


@pytest.fixture
def secondary_elements(variant_config):
    """Return the secondary elements for analysis."""
    elements = variant_config["parameters"]["secondary_elements"]
    # Map to column names
    result = []
    for elem in elements:
        if elem in ['Au', 'Ag']:
            result.append(f"{elem}_ppm")
        else:
            result.append(f"{elem}_pct")
    return result


@pytest.fixture
def quality_filter(variant_config):
    """Return the quality filter value."""
    return variant_config["parameters"]["quality_filter"]


@pytest.fixture
def anomaly_threshold(variant_config):
    """Return the anomaly threshold multiplier."""
    return variant_config["parameters"]["anomaly_threshold_multiplier"]


@pytest.fixture
def num_assays(variant_config):
    """Return the expected number of assays."""
    return variant_config["parameters"]["num_assays"]


@pytest.fixture
def empty_dataframe():
    """Return an empty DataFrame for edge case testing."""
    return pd.DataFrame()


@pytest.fixture
def dataframe_with_all_missing():
    """Return a DataFrame with all missing values for an element."""
    return pd.DataFrame({
        'sample_id': ['T001', 'T002', 'T003'],
        'Au_ppm': [None, None, None],
        'sample_quality': ['Good', 'Good', 'Fair']
    })
