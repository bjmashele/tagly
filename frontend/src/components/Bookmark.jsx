import React from "react";
import PropTypes from "prop-types";
import { BsPencil, BsTrash } from "react-icons/bs";
import devops from "../assets/devops.png";
import tagly from "../assets/tagly-icon.svg";
//dev
const bookmarkData = {
  image: "",
  title: "Local Development with AWS on LocalStack",
  about: "Developing a Spring Boot App against AWS Services with LocalStack",
  tags: ["DevOps", "AWS", "JAVA", "Spring Boot"],
  createdOn: "Sep 12,20",
  url: "reflectoring.io",
};

const BookmarkTags = ({ tags }) =>
  tags.map((tag, index) => (
    <div className="bookmark-tag-item" key={index}>
      {tag}
    </div>
  ));
function Bookmark(props) {
  const { title, image, about, tags, createdOn, url } = props.bookmark;

  console.log("Tags: ", JSON.stringify(tags));
  const imageSrc = image ? image : tagly;
  return (
    <div className="bookmark" style={{ width: "40vw" }}>
      <div className="bookmark-image">
        <img src={imageSrc} alt="IMAGE" height="140px" />
      </div>
      <div className="bookmark-main">
        <h3 className="text">{title}</h3>
        <div className="bookmark-about ">"{about}"</div>
      </div>
      <section className="bookmark-tags">
        {/* <BookmarkTags tags={tags} /> */}
      </section>
      <div className="bookmark-footer">
        <div className="bookmark-footer-start">
          <div className="created-on">{createdOn}</div>
          <div className="bookmark-url text">{url}</div>
        </div>
        <div className="bookmark-footer-end">
          <BsPencil color="blue" style={{ paddingRight: "3em" }} />{" "}
          <BsTrash color="red" />
        </div>
      </div>
    </div>
  );
}

Bookmark.propTypes = {};

export default Bookmark;
