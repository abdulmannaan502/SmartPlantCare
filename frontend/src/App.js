import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [previewUrl, setPreviewUrl] = useState(null);
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [errorMsg, setErrorMsg] = useState(null);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
    setPrediction(null);
    setErrorMsg(null);

    if (file) {
      setPreviewUrl(URL.createObjectURL(file));
    } else {
      setPreviewUrl(null);
    }
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      setErrorMsg("Please select an image file first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      setLoading(true);
      setErrorMsg(null);
      const response = await axios.post("http://127.0.0.1:8000/predict", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      setPrediction(response.data.prediction);
    } catch (error) {
      setErrorMsg(
        error.response?.data?.detail || error.message || "Something went wrong"
      );
      setPrediction(null);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>🌿 Plant Disease Detector</h1>
      <input type="file" onChange={handleFileChange} accept="image/*" />
      {previewUrl && (
        <div className="preview">
          <img src={previewUrl} alt="Selected Plant Leaf" />
        </div>
      )}
      <button onClick={handleUpload} disabled={loading}>
        {loading ? "Predicting..." : "Predict Disease"}
      </button>

      {errorMsg && <p className="error">{errorMsg}</p>}

      {prediction && (
        <div className="result">
          <h2>🔍 Prediction</h2>
          <p>
            <strong>Disease:</strong> {prediction.class}
          </p>
          <p>
            <strong>Confidence:</strong> {Math.round(prediction.confidence * 100)}%
          </p>
          {prediction.advice && (
            <p>
              <strong>Advice:</strong> {prediction.advice}
            </p>
          )}
        </div>
      )}
    </div>
  );
}

export default App;
