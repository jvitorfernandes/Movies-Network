# Code Test - Social Network

This application will display user information and suggest similar users based on their common favorite movies.

# Jaccard Index

The application calculates the [Jaccard similarity coefficient](https://en.wikipedia.org/wiki/Jaccard_index) to determine how much users are similar to each other based on their common favorite movies. 

# Performance and Scalability
For the purpose of this application, we are calculating the similarities for a specific user on demand, by comparing the given user to the entire database, giving space-time complexity of O(n). Favorite movies can be volatile and be different at every request (users could update their favorite movies every so often.), but we could also store the results in a cache so that it doesn't need to  be recalculated everytime. 

If the number of user grows considerably, and we'd still want to make calculations on demand, we could select a sample of user from the database instead of querying everything. We could also add additional filters on the queries (e.g. only calculate similarity for users that have at least one movie in common).

If we'd have chosen to calculate the similarity between all pairs of users upfront, the time complexity would increase to O(n^2), and the system may not scale well, unless we add a distributed computing platform like Apache Spark to our approach to perform the calculations in parallel. Since favorite movies can be volatile, we could have these calculations being performed at a set schedule.

# Setup
To get the app up and running, follow these steps:

## Backend
* Navigate to the `server` folder, create a virtual environment, install the requirements and run ```server.py```:

    ```bash
    cd server
    python -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    python server.py
    ```


## Frontend
* Navigate to the ```client``` folder, install the requirements, then start the app:
    ```bash
    cd client
    npm install
    npm start
    ```

## Usage
Open your browser and go to ```http://localhost:3000/user/leslieshields43``` to use the app.

The API should be up and running on ```http://127.0.0.1:5000/```. You can navigate to ```http://127.0.0.1:5000/api/user/jvfernandes``` to see the json response for that request.
