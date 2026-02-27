# 🎬 Movie Recommender System Web App
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-WebApp-red?logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Recommender-orange?logo=scikitlearn)
![NLP](https://img.shields.io/badge/NLP-ContentBased-green)
![Cosine Similarity](https://img.shields.io/badge/Algorithm-CosineSimilarity-purple)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-yellow)
![TMDB API](https://img.shields.io/badge/API-TMDB-blue)

A smart Machine Learning–based Movie Recommendation Web Application that suggests movies similar to a selected film using Content-Based Filtering techniques.

Built using Python, NLP, Scikit-learn, and Streamlit, and deployed online for real-time movie recommendations with posters.

---

## 🔗 Live Demo

👉 Try the deployed web app here: https://movie-recommender-system-by-saikat-pradhan.streamlit.app/

---

## 🚀 Project Overview

### This project demonstrates how Natural Language Processing (NLP) and Machine Learning similarity techniques can recommend movies based on their content.

### The system analyzes movie metadata such as:

- Genres
- Keywords
- Cast
- Crew
- Overview

### Users simply select a movie, and the system generates personalized recommendations along with movie posters.

---

## 🎯 Application Features

- Movie recommendation based on similarity
- Content-Based Filtering approach
- NLP-based feature engineering
- Cosine Similarity algorithm
- Movie poster fetching using TMDB API
- Interactive Streamlit UI
- Fast real-time recommendations
- Deployed on Streamlit Cloud

---

##🧠 Technologies Used

- Python 🐍
- Streamlit 🌐
- Scikit-learn ⚙️
- Natural Language Processing (NLP) 🧠
- CountVectorizer
- Cosine Similarity
- Pandas 📊
- NumPy 📐
- Pickle 📦

## TMDB API 🎬

### 📊 Dataset

Dataset used from Kaggle: TMDB 5000 Movie Dataset

👉 https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

### Dataset Includes:

- Movie Title
- Genres
- Keywords
- Cast
- Crew
- Overview
- Movie ID

These attributes are combined into textual tags used for similarity learning.

---

## 🏗️ Model Training

Model development performed in:

📓 Movie_Recommender_System.ipynb

- Training Pipeline
- Data Cleaning & Preprocessing
- Feature Extraction
- Tags Creation
- Text Vectorization using CountVectorizer
- Vector Transformation
- Cosine Similarity Calculation
- Model Serialization using Pickle

---

## Saved Files
- movies.pkl              → Processed movie dataset
- CountVectorizer.pkl     → Trained vectorizer

---

## 🧠 How the App Works

- User selects a movie from dropdown.
- Movie metadata is converted into vectors.
- Cosine similarity is calculated between movies.
- Top 5 similar movies are selected.
- Posters are fetched using TMDB API.
- Recommended movies are displayed visually.

---

## 📁 Project Structure
```
Movie-Recommender-System
│
├── app.py
├── movies.pkl
├── CountVectorizer.pkl
├── Movie_Recommender_System.ipynb
├── requirements.txt
└── README.md
```
---

## ⚙️ Setup Guide (Run Locally)
### 1️⃣ Clone Repository
```
git clone https://github.com/Saikat-Pradhan/Movie-Recommender-System.git
cd Movie-Recommender-System
```
### 2️⃣ Install Dependencies
```
pip install -r requirements.txt
```
### 3️⃣ Run Streamlit App
```
streamlit run app.py
```
### Open Browser
```
http://localhost:8501
```

---

## 🎬 Recommendation Output

The application provides:

- Similar Movie Suggestions
- Movie Posters
- Fast Content-Based Recommendations
- Interactive UI Experience

---

## 🌍 Deployment

 Successfully deployed using Streamlit Cloud

### Live App: https://movie-recommender-system-by-saikat-pradhan.streamlit.app/

---

## ⭐ Support

If you like this project, please give it a ⭐ on GitHub.

It motivates me to build more Machine Learning & AI applications 🚀

---

## 👨‍💻 Author

Saikat Pradhan

🔗 GitHub: https://github.com/Saikat-Pradhan

💼 B.Tech CSE | Machine Learning & Data Science Enthusiast
