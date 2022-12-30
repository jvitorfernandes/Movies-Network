from user_database import get_users, get_user
import json


def get_similar_users(username):
    # Connect to the database
    profile = get_user(username)
    profile_favorite_movies = set(profile["favorite_movies"])
    rows = get_users(10)

    # Create a list to store the similar users
    similar_users = []
    similar_users_dict = {}

    # Loop through the retrieved users
    for row in rows:
        if row[0] == username:
            continue

        user = {
            "username": row[0],
            "favorite_movies": set(row[4].split(","))
        }

        similar_movies = profile_favorite_movies.intersection(
            user["favorite_movies"])
        intersection = len(similar_movies)
        union = (len(profile_favorite_movies) +
                 len(user["favorite_movies"])) - intersection
        s_index = float(intersection) / union

        user["similar_movies"] = list(similar_movies)
        user["favorite_movies"] = list(user["favorite_movies"])
        user["similarity"] = s_index

        similar_users.append(user)

        five_similar = sorted(
            similar_users, key=lambda x: x['similarity'], reverse=True)[:5]

        for i, user in enumerate(five_similar):
            similar_users_dict[i] = user

    return similar_users_dict


print(get_similar_users("jasonmcdaniel47"))
