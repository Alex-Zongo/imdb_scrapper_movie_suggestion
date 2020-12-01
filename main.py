import random
import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top'


def main():
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    movietags = soup.select('td.titleColumn')

    inner_movietags = soup.select('td.titleColumn a')

    movietags_ratings = soup.select('td.posterColumn span[name=ir]')

    def get_year(movie_tag):
        moviesplit = movie_tag.text.split()
        year = moviesplit[-1]
        return year

    years = [get_year(tag) for tag in movietags]

    def get_actors(inner_tag):
        actors = inner_tag['title']
        return actors

    actors = [get_actors(tag) for tag in inner_movietags]

    def get_title(inner_tag):
        title = inner_tag.text
        return title

    titles = [get_title(tag) for tag in inner_movietags]

    def get_rating(tag_rating):
        rating = tag_rating['data-value']
        rating = (float(rating))
        rating = (rating)
        return rating

    ratings = [get_rating(tag) for tag in movietags_ratings]

    n_movies = len(titles)
    print(n_movies)

    while True:
        idx = random.randrange(0, n_movies)

        print(
            f'{titles[idx]} {years[idx]}, rating: {ratings[idx]:.1f}, starring: {actors[idx]}')

        user_input = input('do you want another movie (y/[n])? ')
        if user_input != 'y':
            break


if __name__ == "__main__":
    main()
