from user_database import get_users, get_user
import json


def jaccard_similarity(set_a, set_b):
    """
    Calculates the Jaccard similarity between two sets
    """
    intersection = set_a.intersection(set_b)
    intersection_size = len(intersection)
    union_size = (len(set_a) + len(set_b)) - intersection_size
    s_index = float(intersection_size) / union_size

    return s_index


def get_similar_users(username):
    """
    Returns a dictionary of the 5 users with the highest Jaccard similarity relative to the given user.
    """
    profile = get_user(username)
    profile_favorite_movies = set(profile["favorite_movies"])
    rows = get_users(1001)

    # Create a list to store the similar users
    similar_users = []
    similar_users_dict = {}

    # Loop through the retrieved users
    for row in rows:
        if row[1] == username:
            continue

        user = {
            "username": row[1],
            "name": row[2],
            "favorite_movies": row[6].split(",")
        }

        profile_movies_set = set(profile["favorite_movies"])
        user_movies_set = set(row[6].split(","))

        user["similar_movies"] = list(profile_movies_set.intersection(user_movies_set))
        user["similarity"] = jaccard_similarity(profile_movies_set, user_movies_set)

        similar_users.append(user)

        five_similar = sorted(
            similar_users, key=lambda x: x['similarity'], reverse=True)[:5]

        for i, user in enumerate(five_similar):
            similar_users_dict[i] = user

    return similar_users_dict


# print(get_similar_users("jvfernandes"))
