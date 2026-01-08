#This console will suggest a K-Drama based on your mood.
# Create a .env file with TMDB_API_KEY=your_api_key_here
#Link to TMDB API key: https://www.themoviedb.org/settings/api


import requests
from pprint import pprint
from dotenv import load_dotenv  #to load the API key from the .env file. To install it: pip install python-dotenv
import os

#to load the .env file 
load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")

#GET requests to check API
response = requests.get(f"https://api.themoviedb.org/3/discover/tv?api_key={API_KEY}&with_original_language=ko&with_genres=18&sort_by=popularity.desc")

if response.status_code == 200:
    data = response.json()
    pprint(data["results"][:5])  #because it was showing WinError 10054. It may be cause the data is huge.
else:
    print("request failed:", response.status_code)

#POST requests

#function to get data by genre
def get_drama_by_genre(genre_code):
    url = f"https://api.themoviedb.org/3/discover/tv?api_key={API_KEY}&with_original_language=ko&with_genres={genre_code}&sort_by=popularity.desc"
    response = requests.get(url)
    data = response.json()
    return data.get("results", [])[:5] #to get only top 5 dramas because it was showing error 10054.

#function to print drama
def print_kdrama(dramas):
    for kdrama in dramas:
        kdrama_name = kdrama["name"]
        description = kdrama["overview"][:100]+"..."
        print(kdrama_name)
        print(description)

#kdrama genre (from TMDB website) dictionary 
genre = {
    "romance": 10749,
    "funny": 35,
    "crime": 80,
    "sad": 18,
    "action": 10759}

#function to save dramas to a file
def save_kdrama_to_file(mood, dramas):
    with open("kdrama_recommendations.txt", "w", encoding="utf-8") as f: 
        f.write(f"Here are some {mood} kdrama for you:\n\n")
        for kdrama in dramas:
            kdrama_name = kdrama["name"]
            description = kdrama["overview"][:500] + "..."
            f.write(kdrama_name + "\n")
            f.write(description + "\n\n")
        print("recommendations saved to the file")

print("Welcome!Get K-drama recommendations based on your mood.")
print("Available moods:", ", ".join(genre.keys()))
mood = input("Which K-drama genre would you like to watch?")

if mood not in genre:
    print("Sorry! I don't have a genre for your mood.")

else:
    genre_code = genre[mood]
    kdrama_recommendation = get_drama_by_genre(genre_code)

print(f"Here are some {mood} kdrama for you:")
print_kdrama(kdrama_recommendation)

save_kdrama_to_file(mood, kdrama_recommendation)
