from flask import Flask, render_template, request
from utils import preprocess_image
import tensorflow as tf
import numpy as np
import os

# Initialize Flask app
app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

# Ensure static folder exists
if not os.path.exists("static"):
    os.makedirs("static")

# Load trained model
model = tf.keras.models.load_model("models/mobilenet_model.h5")

# Load class names from dataset folder
DATA_DIR = "data/processed"
class_names = sorted(os.listdir(DATA_DIR))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    file = request.files["file"]

    # Check file selected
    if file.filename == "":
        return render_template("index.html", error="No file selected")

    # Save uploaded image
    img_path = "static/uploaded.jpg"
    file.save(img_path)

    # Preprocess image (from utils.py)
    img = preprocess_image(img_path)

    # Prediction
    preds = model.predict(img)
    confidence = np.max(preds) * 100
    predicted_class = class_names[np.argmax(preds)]

    warning = None

    # Smart warning (not crop specific)
    if confidence < 40:
        warning = "Low confidence prediction. Please upload a clear leaf image."

    return render_template(
        "index.html",
        prediction=predicted_class,
        confidence=round(confidence, 2),
        img_path=img_path,
        warning=warning,
        note="Prediction is based on visual disease patterns only."
    )


if __name__ == "__main__":
    app.run(debug=True)
