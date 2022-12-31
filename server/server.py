from flask import Flask, jsonify
from user_database import get_user
from similar_users import get_similar_users

api = Flask(__name__)


@api.route("/api/user/<string:username>")
def user(username):
    user = get_user(username)
    user["similar_users"] = get_similar_users(username)
    return jsonify(user)


if __name__ == "__main__":
    api.run(debug=True)
