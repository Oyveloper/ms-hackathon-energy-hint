import React from 'react';
import './App.css';
import Graph from "./components/Graph/Graph";

function App() {
  return (
    <div className="App">
      <Graph date={new Date()} meteringPointId={"707057500100175148"} height={700} width={700}/>
    </div>
  );
}

export default App;
