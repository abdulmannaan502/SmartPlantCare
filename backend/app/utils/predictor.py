# backend/app/utils/predictor.py

import numpy as np
import tensorflow as tf
from PIL import Image
import io

# Load TFLite model and allocate tensors
interpreter = tf.lite.Interpreter(model_path="app/model/model.tflite")
interpreter.allocate_tensors()

# Get input and output tensor details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Class names (15 classes)
class_names = [
    # Pepperbell diseases
    "Pepperbell Bacterial Spot",
    "Pepperbell Early Blight",
    "Pepperbell Late Blight",
    "Pepperbell Healthy",
    "Pepperbell Mosaic Virus",
    
    # Potato diseases
    "Potato Early Blight",
    "Potato Late Blight",
    "Potato Healthy",
    "Potato Common Scab",
    "Potato Blackleg",
    
    # Tomato diseases
    "Tomato Bacterial Spot",
    "Tomato Early Blight",
    "Tomato Late Blight",
    "Tomato Healthy",
    "Tomato Yellow Leaf Curl Virus"
]

# Advice dictionary corresponding to each class
advice_dict = {
    # Pepperbell advice
    "Pepperbell Bacterial Spot": "Apply copper-based fungicide.",
    "Pepperbell Early Blight": "Use fungicide and remove infected leaves.",
    "Pepperbell Late Blight": "Improve airflow and apply fungicides.",
    "Pepperbell Healthy": "Plant is healthy. Keep monitoring.",
    "Pepperbell Mosaic Virus": "Remove infected plants to stop spread.",
    
    # Potato advice
    "Potato Early Blight": "Apply fungicides early and rotate crops.",
    "Potato Late Blight": "Remove infected plants, use resistant varieties.",
    "Potato Healthy": "Plant is healthy. Maintain care.",
    "Potato Common Scab": "Maintain proper soil moisture; avoid high pH.",
    "Potato Blackleg": "Improve drainage and avoid injury during planting.",
    
    # Tomato advice
    "Tomato Bacterial Spot": "Use bactericides and avoid overhead watering.",
    "Tomato Early Blight": "Apply fungicide and remove infected leaves.",
    "Tomato Late Blight": "Use resistant varieties and fungicides.",
    "Tomato Healthy": "Plant is healthy. Keep monitoring.",
    "Tomato Yellow Leaf Curl Virus": "Control whiteflies and remove infected plants."
}

def preprocess_image(image_bytes):
    # Open image, convert to RGB, resize to expected input size
    img = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    img = img.resize((128, 128))  # Model input size
    img_array = np.array(img, dtype=np.float32) / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

def predict_image(image_bytes):
    img_array = preprocess_image(image_bytes)

    # Set model input
    interpreter.set_tensor(input_details[0]['index'], img_array)
    interpreter.invoke()

    # Get model output and find predicted class and confidence
    output_data = interpreter.get_tensor(output_details[0]['index'])[0]
    predicted_index = int(np.argmax(output_data))
    confidence = float(output_data[predicted_index])

    predicted_class = class_names[predicted_index]
    advice = advice_dict.get(predicted_class, "No advice available")

    return {
        "class": predicted_class,
        "confidence": confidence,
        "advice": advice
    }
