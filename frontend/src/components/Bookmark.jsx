import React from "react";
import PropTypes from "prop-types";

//dev
const bookmarkData = {
  image: "",
  title: "Local Development with AWS on LocalStack",
  about: "Developing a Spring Boot App against AWS Services with LocalStack",
  tags: ["DevOps", "AWS", "JAVA", "Spring Boot"],
  createdOn: "Sep 12,20",
  url: "freecodecamp.org",
};

function Bookmark(props) {
  const { title, image, about, tags, createdOn, url } = bookmarkData;
  return (
    <div className="bookmark" style={{ width: "40vw" }}>
      <div className="bookmark-image">Image</div>
      <div className="bookmark-main">
        <h3 className="text">{title}</h3>
        <div className="bookmark-about ">"{about}"</div>
      </div>
      <div className="bookmark-footer">
        <div className="bookmark-footer-content">
          <div className="created-on">{createdOn}</div>
          <div className="url text">{url}</div>
        </div>
      </div>
    </div>
  );
}

Bookmark.propTypes = {};

export default Bookmark;
