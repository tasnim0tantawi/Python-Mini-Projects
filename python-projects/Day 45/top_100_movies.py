import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.imdb.com/list/ls068718974/")
soup = BeautifulSoup(response.text, "html.parser")
movies = [movie.getText() for movie in soup.select(".lister-item-header a")]
with open("top_100_movies.txt", "w") as f:
    count = 1
    for movie in movies:
        f.write(str(count)+") "+ movie + "\n")
        count += 1