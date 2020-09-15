import React from "react";
import PropTypes from "prop-types";

const TagList = function ({ tagsMeta }) {
  return (
    <ul>
      {tagsMeta.map((item, index) => (
        <li key={index} className="aside-tag-item">
          <div className="aside-tag-item-name">{item.name}</div>
          <div className="aside-tag-item-count">{item.count}</div>
        </li>
      ))}
    </ul>
  );
};

{
  /* <li className="aside-tag-item" key={index}>
      <div className="aside-tag-item-name">{item.name}</div>
      <div className="aside-tag-item-count">{item.count}</div>
    </li> */
}

function AsideTags(props) {
  let tagsMeta = [
    { name: "DevOps", count: 4 },
    { name: "AWS", count: 2 },
    { name: "JAVA", count: 3 },
    { name: "Spring Boot", count: 1 },
  ];

  return (
    <div>
      <div className="tag-status">
        <div className="title">STATUS</div>
        <hr className="line" />
      </div>
      <div className="tag-list">
        <div className="title">TAGS</div>
        <hr className="line" />

        <TagList tagsMeta={tagsMeta} />
      </div>
      <div className="tag-visibility">
        <div className="title">VISIBILITY</div> <hr className="line" />
      </div>
    </div>
  );
}

AsideTags.propTypes = {};

export default AsideTags;
