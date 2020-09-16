import React from "react";
import PropTypes from "prop-types";

function Home(props) {
  return (
    <div className="home-page">
      <div className="nav">Nav</div>
      <div className="header">Header</div>
      <div className="aside-left">Left Aside</div>
      <div className="main">Main</div>
      <div className="aside-right">Right Aside</div>
    </div>
  );
}

Home.propTypes = {};

export default Home;
