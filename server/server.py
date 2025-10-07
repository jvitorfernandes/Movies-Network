from flask import Flask, jsonify, redirect, send_from_directory
import os
from user_database import get_user
from similar_users import get_similar_users

api = Flask(__name__)


@api.route("/api/user/<string:username>")
def user(username):
    user = get_user(username)
    user["similar_users"] = get_similar_users(username)
    return jsonify(user)


# If a React build exists in server/client_build, serve it (single-container deployments)
CLIENT_BUILD_DIR = os.path.join(os.path.dirname(__file__), "client_build")
if os.path.isdir(CLIENT_BUILD_DIR):
    @api.route('/', defaults={'path': ''})
    @api.route('/<path:path>')
    def serve_client(path):
        # Serve static files when they exist, otherwise serve index.html
        if path != "" and os.path.exists(os.path.join(CLIENT_BUILD_DIR, path)):
            return send_from_directory(CLIENT_BUILD_DIR, path)
        return send_from_directory(CLIENT_BUILD_DIR, 'index.html')


if __name__ == "__main__":
    api.run(debug=True)
