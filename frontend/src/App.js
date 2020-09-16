import React from "react";
import PublicPage from "./components/PublicPage";
import Bookmark from "./components/Bookmark";
import AsideTags from "./components/AsideTags";
import Home from "./components/Home";
import HomeContainer from "./containers/HomeContainer";
import logo from "./logo.svg";
import "./App.css";

function App() {
  return (
    <div className="App">
      <HomeContainer />
    </div>
  );
}

export default App;
