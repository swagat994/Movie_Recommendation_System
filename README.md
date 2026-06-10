# Movie Recommendation System

A content-based movie recommendation system that suggests movies similar to a user's selection by analyzing movie metadata. The recommendation engine uses natural language processing techniques and cosine similarity to identify movies with comparable characteristics. The application integrates with the TMDB API to enrich recommendations with movie posters and metadata.

## Live Demo

**Application:** 

## Overview

This project demonstrates the development of a machine learning-powered web application that combines recommendation algorithms with modern web technologies. Users can select a movie and receive a list of similar movies along with their corresponding posters fetched from TMDB.

## Features

* Content-based movie recommendation engine
* Cosine similarity-based movie matching
* TMDB API integration for movie posters
* FastAPI-powered REST API
* Interactive Streamlit user interface
* Real-time recommendation generation
* Robust handling of invalid movie inputs

## Technology Stack

* Python
* FastAPI
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* Requests
* TMDB API

## How It Works

Movie metadata is processed and transformed into meaningful textual features such as genres, keywords, cast members, and crew information. These features are vectorized and used to compute similarity scores between movies. When a user selects a movie, the system retrieves the most relevant recommendations from a precomputed similarity matrix and augments the results with poster data obtained through the TMDB API.

## Sample Output

```json
{
  "movie": "Avatar",
  "recommendations": [
    {
      "title": "Titan A.E.",
      "poster": "https://image.tmdb.org/..."
    }
  ]
}
```

## License

This project was developed for educational purposes.
