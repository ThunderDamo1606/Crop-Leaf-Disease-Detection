import os
import tensorflow as tf

def test_model_file_exists():
    """
    Check if trained model file exists
    """
    assert os.path.exists("models/mobilenet_model.h5")


def test_model_load():
    """
    Check if model loads without error
    """
    model = tf.keras.models.load_model("models/mobilenet_model.h5")
    assert model is not None


def test_dummy_api():
    """
    Dummy test to verify pytest working
    """
    assert 2 + 2 == 4
