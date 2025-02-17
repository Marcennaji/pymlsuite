import pandas as pd
import pytest


@pytest.fixture
def sample_data():
    return pd.read_csv("datasets/sample_dataset.csv")


def test_missing_values(sample_data):
    assert sample_data.isnull().sum().sum() == 0, "Dataset contains missing values!"


def test_column_types(sample_data):
    expected_types = {"age": int, "salary": float, "department": str}
    for col, dtype in expected_types.items():
        assert sample_data[col].dtype == dtype, f"Column {col} has incorrect type!"
