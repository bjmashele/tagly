import React from "react";
import AsideTags from "../components/AsideTags";
import Bookmark from "../components/Bookmark";

export default function HomeContainer() {
  return (
    <div className="home-page text">
      <div className="nav">Navbar</div>
      <div className="header">Header</div>
      <div className="aside-left">
        <AsideTags />
      </div>
      <div className="main">
        <Bookmark />
      </div>
      <div className="aside-right"></div>
      <div className="footer">Footer</div>
    </div>
  );
}
