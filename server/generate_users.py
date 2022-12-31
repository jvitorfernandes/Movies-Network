from user_profile import UserProfile
import user_database
from faker import Faker
import pandas as pd
import random


def generate_users(n):

    fake = Faker()

    # https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows
    movies = pd.read_csv('data/imdb_top_1000.csv')
    movies_list = list(movies[:10]['Series_Title'])

    profiles = []
    for i in range(n):
        user_id = i + 1
        name = fake.name()
        email = fake.email()
        age = fake.random_int(18, 80)
        location = fake.city()
        favorite_movies = list(
            set(random.choices(movies_list, k=random.randint(3, 5))))

        profile = UserProfile(user_id, name, email, age,
                              location, favorite_movies)
        profiles.append(profile)

    return profiles


if __name__ == "__main__":

    user_database.create_user_table()
    user_database.insert_user_profiles(generate_users(10))
