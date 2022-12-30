class UserProfile:

    def __init__(self, name, age, location, favorite_movies=None):
        self.name = name
        self.age = age
        self.location = location
        self.favorite_movies = favorite_movies or []
        self.username = name.replace(" ", "").replace(
            ".", "").lower() + str(age)
