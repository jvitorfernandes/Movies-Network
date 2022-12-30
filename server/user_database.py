import sqlite3


def create_user_table():

    conn = sqlite3.connect("data/user_profiles.db")
    cursor = conn.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS profiles (username text, name text, age integer, location text, favorite_movies text)")

    conn.commit()
    conn.close()


def insert_user_profiles(profiles):

    conn = sqlite3.connect("data/user_profiles.db")
    cursor = conn.cursor()

    for profile in profiles:
        cursor.execute("INSERT INTO profiles VALUES (?, ?, ?, ?, ?)",
                       (profile.username, profile.name, profile.age, profile.location, ",".join(profile.favorite_movies)))

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

    user = {
        "username": row[0],
        "name": row[1],
        "age": row[2],
        "location": row[3],
        "favorite_movies": row[4].split(",")
    }

    return user


def get_users(limit):
    conn = sqlite3.connect("data/user_profiles.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM profiles LIMIT ?", (limit,))
    users = cursor.fetchall()

    conn.commit()
    conn.close()

    return users


user = get_user('michaelmiller31')
print(type(user))

users = get_users(10)
print(type(users))
