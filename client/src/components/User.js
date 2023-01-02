import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Route, useParams } from "react-router-dom";
import { PersonCircle } from "react-bootstrap-icons";

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
        <div className="userbody">
          {typeof data["similar_users"] === "undefined" ||
          typeof data["favorite_movies"] === "undefined" ||
          typeof data["movies_data"] === "undefined" ? (
            <p> </p>
          ) : (
            <>
              <div className="container">
                <h1>{data["name"]}</h1>
                <div className="row">
                  <div className="col-md-6">
                    <ul className="list-unstyled">
                      <li>
                        <span className="emoji">✉️</span> {data["email"]}
                      </li>
                      {/* <li>Age: {data["age"]}</li> */}
                      <li>
                        <span className="emoji">📍</span> {data["location"]}
                      </li>
                    </ul>
                    <h4>Favorite Movies:</h4>

                    <div className="row mt-4">
                      {data["movies_data"].map((movie, i) => (
                        <div className="col-lg-3 col-sm-6" key={i}>
                          <div className="d-flex">
                            <figure className="figure">
                              <img
                                src={movie["url"]}
                                alt=""
                                className="rounded"
                                width="100"
                                height="146.266"
                              ></img>
                              <figcaption className="figure-caption">
                                {movie["movie"]}
                              </figcaption>
                            </figure>
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                  <div className="col-md-5">
                    <h4>Similar Users:</h4>
                    <ul className="list-unstyled">
                      {Object.keys(data["similar_users"]).map((key, index) => {
                        return (
                          <li key={index}>
                            <PersonCircle
                              color="royalblue"
                              className="m-2"
                              size={20}
                            />
                            <a
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
