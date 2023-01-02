from user_profile import UserProfile
import user_database
from faker import Faker
import pandas as pd
import random


def generate_users(n):

    fake = Faker()

    # https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows
    movies = pd.read_csv('data/imdb_top_1000.csv')
    movies_list = list(movies['Series_Title'])

    profiles = []
    for i in range(n):
        user_id = i + 1
        name = fake.name()
        email = fake.email()
        age = fake.random_int(18, 80)
        username = name.replace(" ", "").replace(".", "").lower() + str(age)
        location = fake.city()
        favorite_movies = random.sample(movies_list, k=8)

        profile = UserProfile(user_id, username, name,
                              email, age, location, favorite_movies)
        profiles.append(profile)

    me = UserProfile(1001, "jvfernandes", "João Vítor Fernandes", "fernandesjvb@gmail.com", 26,
                     "Austin, TX", ["The Worst Person In the World", "Whiplash", "Marcel the Shell with Shoes On", "Gladiator", "Inglourious Basterds", "Interstellar", "The Lion King", "Majo no takkyûbin"])
    profiles.append(me)
    return profiles


if __name__ == "__main__":

    user_database.create_user_table()
    user_database.insert_user_profiles(generate_users(1000))
