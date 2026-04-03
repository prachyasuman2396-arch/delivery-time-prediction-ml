#  Food Delivery Time Prediction System

An end-to-end Machine Learning system that predicts food delivery time based on real-world operational factors such as distance, traffic, weather, and courier experience.

This project demonstrates a **production-grade ML pipeline**, deployed as a REST API and integrated with an interactive frontend.

---

### Live API

- Swagger Docs:  
  https://delivery-time-prediction-ml-1.onrender.com/docs

- Predict Endpoint:  
  https://delivery-time-prediction-ml-1.onrender.com/docs#/default/predict_predict_post

___

##  Problem Statement

Accurately estimating delivery time is critical for logistics platforms like Swiggy, Zomato, and Uber Eats.

This project aims to:
- Predict delivery time using structured data
- Incorporate real-world feature interactions
- Serve predictions via a scalable API
- Provide a user-friendly interface for inference

---

##  ML System Design

The system is designed with a modular and production-oriented architecture:

### 1. Feature Engineering

Custom features are engineered to capture real-world delivery dynamics:

- Distance-to-experience ratio  
- Distance + preparation interaction  
- Peak hour indicator  
- Vehicle speed normalization  
- Distance adjusted by vehicle type  

These transformations are applied using a dedicated feature engineering module.

---

### 2. Pipeline Architecture

A complete Scikit-learn pipeline is used to ensure consistency between training and inference:

- Numerical preprocessing:
  - Median imputation
  - Standard scaling

- Categorical preprocessing:
  - Mode imputation
  - One-hot encoding

- Model:
  - Linear Regression (baseline, interpretable)

This ensures:
- No data leakage
- Reproducibility
- Clean separation of concerns

---

### 3. Training Workflow

- Train-test split (80/20)
- Evaluation metrics:
  - R² Score
  - Mean Absolute Error (MAE)
- Model persistence using `joblib`

---

##  Model Performance

| Metric | Value |
|--------|------|
| R² Score | ~0.85+ |
| MAE | Low error range |

The model effectively captures both linear relationships and engineered interactions.

---

## ⚙️ API Deployment

The trained model is deployed using FastAPI and hosted on Render.


### Features

- Input validation using Pydantic
- Structured JSON responses
- Custom error handling
- Scalable deployment

---

## 💻 Frontend (Streamlit)

An interactive frontend is built using Streamlit for real-time predictions.

### Features

- Clean and intuitive UI
- Dropdown-based categorical inputs
- API integration using HTTP requests
- Real-time prediction display

---

## 🔄 End-to-End Flow

User Input (Streamlit)  
→ API Request (FastAPI)  
→ Input Validation (Pydantic)  
→ Feature Engineering  
→ Preprocessing Pipeline  
→ Model Prediction  
→ JSON Response  
→ UI Display  

---

## 📁 Project Structure
