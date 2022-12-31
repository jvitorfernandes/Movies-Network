import React, { useState, useEffect } from "react";

function App() {
  const [data, setData] = useState([{}]);

  useEffect(() => {
    fetch("/user/jasonmcdaniel47")
      .then((res) => res.json())
      .then((data) => {
        setData(data);
        console.log(data);
      });
  }, []);

  return (
    <div>
      {typeof data === "undefined" ? (
        <p>Loading...</p>
      ) : (
        <>
          <h1>{data["name"]}</h1>
          <p>{data["age"]}</p>
          <p>{data["location"]}</p>

          {data["favorite_movies"].map((movie, i) => (
            <p>{movie}</p>
          ))}

          {Object.keys(data["similar_users"]).map((key, index) => {
            return (
              <ul>
                <li>
                  <a href={"/user/" + data["similar_users"][key]["username"]}>
                    {data["similar_users"][key]["username"]}
                  </a>
                </li>
              </ul>
            );
          })}
        </>

        // <p>{data["favorite_movies"]}</p>
      )}
    </div>
  );
}

export default App;
