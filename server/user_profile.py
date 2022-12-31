class UserProfile:

    def __init__(self, user_id, name, email, age, location, favorite_movies=None):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.age = age
        self.location = location
        self.favorite_movies = favorite_movies or []
        self.username = name.replace(" ", "").replace(
            ".", "").lower() + str(age)
