import "./App.css";
import AdvicePage from "./components/Advice/AdvicePage";

import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import PieChartPage from "./components/PieChart/PieChartPage";

function App() {
  return (
    <div className="App">
      <Router>
        <Switch>
          <Route exact path="/">
            <AdvicePage />
          </Route>

          <Route exact path="/distrobution">
            <PieChartPage />
          </Route>

          <Route path="*">
            <div>404 not found</div>
          </Route>
        </Switch>
      </Router>
    </div>
  );
}

export default App;
