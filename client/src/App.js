import "bootstrap/dist/css/bootstrap.min.css";

import { BrowserRouter as Router, Route } from "react-router-dom";
import User from "./components/User";
// import { useParams } from "react-router-dom";

function App() {
  return (
    <Router>
      <Route path="/user/:username">
        <User />
      </Route>
    </Router>
  );
}

export default App;
