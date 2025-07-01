# 🎬 Cine - AI Movie Recommendation System

![CineAI Demo](https://github.com/shubhangikatariyar/Cine-AI-Movie-Recommendation-System/blob/main/CineAI.gif)

> A smart and intuitive movie recommender system using **Content-Based Filtering**, built with **Streamlit**, deployed on **Heroku**, and powered by the **TMDB API**.

📽️ **[Watch Full Video Demo](https://www.youtube.com/watch?v=F6STdcI0zDA)**

---

## 🧠 About the Project

**Cine-AI** recommends movies based on user input using **content-based filtering** and **cosine similarity**. It enhances movie metadata with real-time visuals and info from **TMDB (The Movie Database) API**.

---

## 🚀 Features

- 🔍 Content-Based Filtering using metadata (genres, cast, director, etc.)
- 🧮 Cosine Similarity for computing similarity between movies
- 🎞️ Movie posters and details via **TMDB API**
- ⚡ Built with **Streamlit** for a clean interactive UI
- ☁️ Deployed on **Heroku** for easy access and sharing

---

## 🧰 Tech Stack

- Python
- Pandas, Scikit-learn
- Streamlit
- TMDB API
- Heroku

---

## 🔑 TMDB API Setup

This project uses the [TMDB API](https://www.themoviedb.org/documentation/api) to fetch movie posters and metadata.

1. Create an account on TMDB.
2. Generate an API key from your account dashboard.
3. Replace `YOUR_API_KEY` in the code:

```python
response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY")
