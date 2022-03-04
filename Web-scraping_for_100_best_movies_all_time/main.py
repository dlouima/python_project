from pprint import pprint

from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

html_text = requests.get(url=URL).text


soup = BeautifulSoup(html_text, 'html.parser')


data = soup.find_all('h3', class_="title")
movie_list = [movie.get_text() for movie in data]
movie_list.reverse()

with open("100_greatest_movies.txt", 'w') as file:
    for text in movie_list:
        file.write(text + "\n")
