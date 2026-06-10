from fastapi import FastAPI
from dotenv import load_dotenv # type: ignore
from pathlib import Path
import os
import pickle
import requests

# =====================================
# Paths and Environment Variables
# =====================================

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

API_KEY = os.getenv("TMDB_API_KEY")

# =====================================
# FastAPI App
# =====================================

app = FastAPI()

# =====================================
# Load Artifacts
# =====================================

movies = pickle.load(
    open(BASE_DIR / "artifacts" / "movies.pkl", "rb")
)

similarity = pickle.load(
    open(BASE_DIR / "artifacts" / "similarity.pkl", "rb")
)

# =====================================
# TMDB Helper Function
# =====================================

def fetch_poster(movie_id):

    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"

        response = requests.get(url)

        if response.status_code != 200:
            return None

        data = response.json()

        poster_path = data.get("poster_path")

        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"

        return None

    except Exception:
        return None


# =====================================
# Recommendation Function
# =====================================

def recommend(movie):

    movie_matches = movies[
        movies["title"] == movie
    ]

    if movie_matches.empty:
        return None

    movie_index = movie_matches.index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movies_list:

        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(
            {
                "title": movies.iloc[i[0]].title,
                "poster": fetch_poster(movie_id)
            }
        )

    return recommended_movies


# =====================================
# Routes
# =====================================

@app.get("/")
def home():

    return {
        "message": "Movie Recommendation API Running"
    }


@app.get("/check-api")
def check_api():

    return {
        "tmdb_api_loaded": API_KEY is not None
    }


@app.get("/columns")
def columns():

    return movies.columns.tolist()


@app.get("/recommend/{movie_name}")
def get_recommendations(movie_name):

    recommendations = recommend(movie_name)

    if recommendations is None:

        return {
            "error": f"Movie '{movie_name}' not found"
        }

    return {
        "movie": movie_name,
        "recommendations": recommendations
    }