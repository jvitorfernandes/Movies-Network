import sqlite3
import pandas as pd


def create_movies_table():

    conn = sqlite3.connect("data/movies.db")
    cursor = conn.cursor()

    movies = pd.read_csv('data/imdb_top_1000.csv')
    movies.to_sql("movies_dataset", conn)

    cursor.execute("CREATE TABLE movies AS SELECT * FROM movies_dataset")

    conn.commit()
    conn.close()


def get_movies(movies):

    conn = sqlite3.connect("data/movies.db")
    cursor = conn.cursor()

    movies_list = []
    for movie in movies:
        cursor.execute(
            "SELECT Poster_Link, Series_Title FROM movies WHERE Series_Title = ?", (movie,))
        row = cursor.fetchone()

        movie_dict = {
            "movie": row[1],
            "url": row[0]
        }

        movies_list.append(movie_dict)

    conn.commit()
    conn.close()

    return movies_list


if __name__ == "__main__":
    create_movies_table()
