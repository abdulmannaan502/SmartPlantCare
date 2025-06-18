# PlantDiseaseDetectPro

🌿 **PlantDiseaseDetectPro** is an AI-powered web app that detects diseases in pepperbell, potato, and tomato plants from leaf images. It provides accurate disease classification along with actionable care advice to help farmers and gardeners keep their crops healthy.

---

## Features

- Upload a plant leaf image (pepperbell, potato, or tomato)
- Fast and accurate disease prediction using TensorFlow Lite model
- Supports 15 disease classes across 3 crops
- Displays disease name, confidence score, and personalized advice
- Simple React frontend with a FastAPI backend

---

## Technology Stack

- Frontend: React, Axios, CSS
- Backend: FastAPI, Python
- Model: TensorFlow Lite (TFLite) image classification
- Image processing: Pillow, NumPy

---

## Setup & Run Locally

### Prerequisites

- Python 3.8+
- Node.js & npm
- Git

### Backend

1. Clone the repo:

   ```bash
   git clone <your-repo-url>
   cd PlantDiseaseDetectPro/backend
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   .\venv\Scripts\activate    # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the FastAPI backend server:

   ```bash
   uvicorn app.main:app --reload
   ```

### Frontend

1. Navigate to the frontend folder:

   ```bash
   cd ../frontend
   ```

2. Install npm dependencies:

   ```bash
   npm install
   ```

3. Run the React app:

   ```bash
   npm start
   ```

4. Open `http://localhost:3000` in your browser.

---

## Usage

1. Upload a clear image of a plant leaf from pepperbell, potato, or tomato.
2. Click *Predict Disease*.
3. View the disease name, confidence percentage, and expert advice for care.

---

## Model & Data

- The TFLite model is trained on 15 disease classes for pepperbell, potato, and tomato.
- Input image size for the model is 128x128 pixels RGB.
- The model file is located in `backend/app/model/model.tflite`.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgments

- Thanks to the open-source community for React, FastAPI, and TensorFlow Lite.
- Dataset inspired by PlantVillage and similar public datasets.

---

- Created by Abdul Mannaan
