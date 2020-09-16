import React from "react";
import Bookmark from "./Bookmark";

export default function BookmarkList({ bookmarkListData }) {
  console.log("BMLDL: ", bookmarkListData);
  return (
    <div className="bookmark-list">
      {bookmarkListData.map((bookmark, index) => {
        console.log("To bookmark: ", bookmark);
        return <Bookmark bookmark={bookmark} />;
      })}
    </div>
  );
}
