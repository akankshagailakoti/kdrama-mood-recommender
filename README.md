# K-Drama Mood Recommender 

This is a simple Python console app that recommends Korean dramas based on your mood.
It uses the TMDB (The Movie Database) API to fetch popular K-dramas by genre.

I built this project as part of my assignment to practice:
- Working with APIs
- Environment variables
- Functions
- File handling in Python

---

## How It Works

1. The user selects a mood (romance, funny, crime, sad, or action)
2. The app calls the TMDB API
3. It shows the top 5 K-dramas for that mood
4. The recommendations are also saved to a text file

---

## Tech Stack

- Python
- TMDB API
- requests
- python-dotenv

---

## Setup Instructions

### 1. Clone the repo

### 2. Install dependencies
``` 
pip install requests python-dotenv
```

### 3. Create a .env file
Create a file called `.env` in the project folder and add:
```
TMDB_API_KEY=your_api_key_here
```
You can get a free API key from TMDB:
https://www.themoviedb.org/settings/api

### 4. Run the App
