class UserProfile:

    def __init__(self, user_id, username, name, email, age, location, favorite_movies=None):
        self.user_id = user_id
        self.username = username
        self.name = name
        self.email = email
        self.age = age
        self.location = location
        self.favorite_movies = favorite_movies or []
