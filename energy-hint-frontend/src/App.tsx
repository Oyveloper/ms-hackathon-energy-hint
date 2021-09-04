import React from "react";
import "./App.css";
import AdvicePage from "./components/Advice/AdvicePage";
import Graph from "./components/Graph/Graph";
import MobileContainer from "./components/Mobile/Mobile";

function App() {
  /*
  <Graph
          date={new Date()}
          meteringPointId={"707057500100175148"}
          height={350}
          width={350}
        />
        */
  return (
    <div className="App">
      <MobileContainer>
        <AdvicePage />
      </MobileContainer>
    </div>
  );
}

export default App;
