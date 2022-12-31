import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Route, useParams } from "react-router-dom";
import { EnvelopeAt } from "react-bootstrap-icons";

export default function User() {
  const [data, setData] = useState([{}]);
  const { username } = useParams();

  useEffect(() => {
    fetch("/api/user/" + username)
      .then((res) => res.json())
      .then((data) => {
        setData(data);
        console.log(data);
      });
  }, []);

  return (
    <Router>
      <Route path="/user/:username">
        <div>
          {typeof data["similar_users"] === "undefined" ||
          typeof data["favorite_movies"] === "undefined" ? (
            <p> </p>
          ) : (
            <>
              <div className="container">
                <div className="row">
                  <div className="col-md-9">
                    <h2>{data["name"]}</h2>
                    <ul>
                      <li>{data["email"]}</li>
                      <li>Age: {data["age"]}</li>
                      <li>Location: {data["location"]}</li>
                    </ul>
                    <h4>Favorite Movies:</h4>
                    <ul>
                      {data["favorite_movies"].map((movie, i) => (
                        <li key={i}>{movie}</li>
                      ))}
                    </ul>
                  </div>
                  <div className="col-md-3">
                    <h4>Similar Users:</h4>
                    <ul>
                      {Object.keys(data["similar_users"]).map((key, index) => {
                        return (
                          <li>
                            <a
                              key={index}
                              href={
                                "/user/" +
                                data["similar_users"][key]["username"]
                              }
                            >
                              {data["similar_users"][key]["name"]}
                            </a>
                          </li>
                        );
                      })}
                    </ul>
                  </div>
                </div>
              </div>
            </>
          )}
        </div>
      </Route>
    </Router>
  );
}
