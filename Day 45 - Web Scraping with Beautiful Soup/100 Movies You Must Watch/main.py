import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser')

all_movies = soup.find_all("h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]
#print(movie_titles) #format, first item: '100) Stand By Me'
#the website has ordered the list from 100 to 1, but we wish to reverse the order
movies = movie_titles[::-1] #new first item: '1) The Godfather'
#print(movies)

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")


