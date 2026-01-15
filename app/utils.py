import cv2
import numpy as np

def preprocess_image(image_path):
    """
    Preprocess uploaded image before prediction.

    Steps:
    1. Read image from given path
    2. Resize image to 224x224 (MobileNet input size)
    3. Convert BGR to RGB
    4. Normalize pixel values (0-1)
    5. Expand dimensions to match model input shape

    Returns:
        Preprocessed image ready for model prediction
    """

    # Read image
    img = cv2.imread(image_path)

    if img is None:
        raise ValueError("Invalid image file")

    # Resize
    img = cv2.resize(img, (224, 224))

    # Convert BGR to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Normalize
    img = img / 255.0

    # Expand dims (1,224,224,3)
    img = np.expand_dims(img, axis=0)

    return img
