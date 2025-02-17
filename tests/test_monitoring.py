from monitoring import check_model_drift


def test_model_drift():
    assert check_model_drift() is None
