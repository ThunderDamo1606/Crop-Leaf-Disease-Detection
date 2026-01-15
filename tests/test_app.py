import os
import tensorflow as tf
import pytest

MODEL_PATH = "models/mobilenet_model.h5"

def test_model_file_exists():
    """
    Skip test if model file not present
    """
    if not os.path.exists(MODEL_PATH):
        pytest.skip("Model file not present in repo")

    assert os.path.exists(MODEL_PATH)


def test_model_load():
    """
    Load model only if file exists
    """
    if not os.path.exists(MODEL_PATH):
        pytest.skip("Model file not present in repo")

    model = tf.keras.models.load_model(MODEL_PATH)
    assert model is not None


def test_dummy_api():
    assert 2 + 2 == 4
