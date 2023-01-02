import sqlite3
from movies_database import get_movies


def create_user_table():

    conn = sqlite3.connect("data/user_profiles.db")
    cursor = conn.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS profiles (id text, username text, name text, email text, age integer, location text, favorite_movies text)")

    conn.commit()
    conn.close()


def insert_user_profiles(profiles):

    conn = sqlite3.connect("data/user_profiles.db")
    cursor = conn.cursor()

    for profile in profiles:
        cursor.execute("INSERT INTO profiles VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (profile.user_id, profile.username, profile.name, profile.email, profile.age, profile.location, ",".join(profile.favorite_movies)))

    conn.commit()
    conn.close()


def get_user(username):
    conn = sqlite3.connect("data/user_profiles.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM profiles WHERE username=?", (username,))
    row = cursor.fetchone()

    conn.commit()
    conn.close()

    movies_data = get_movies(row[6].split(","))
    # Will send a list of movies to the movies database and get a list of dicts: movie name and url
    user = {
        "user_id": row[0],
        "username": row[1],
        "name": row[2],
        "email": row[3],
        "age": row[4],
        "location": row[5],
        "favorite_movies": row[6].split(","),
        "movies_data": movies_data
    }

    return user


# print(get_user("judithstokes42"))


def get_users(limit):
    conn = sqlite3.connect("data/user_profiles.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM profiles LIMIT ?", (limit,))
    users = cursor.fetchall()

    conn.commit()
    conn.close()

    return users


# user = get_user('michaelmiller31')
# print(type(user))

# users = get_users(10)
# print(type(users))
