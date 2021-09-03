import React from 'react';
import logo from './logo.svg';
import './App.css';
import Graph from "./components/Graph/Graph";

function App() {
  return (
    <div className="App">
      <Graph date={new Date()} meteringPointId={"707057500100175148"}/>
    </div>
  );
}

export default App;
