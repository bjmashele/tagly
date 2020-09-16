import React from "react";
import AsideTags from "../components/AsideTags";
import Bookmark from "../components/Bookmark";
import BookmarkList from "../components/BookmarkList";

//mock data
import { bookmarkListData } from "../mock-data/mockState";

export default function HomeContainer() {
  console.log("BM List Data: ", JSON.stringify(bookmarkListData));
  return (
    <div className="home-page">
      <div className="nav">Navbar</div>
      <div className="header">Header</div>
      <div className="aside-left">
        <AsideTags />
      </div>
      <div className="main">
        <BookmarkList bookmarkListData={bookmarkListData} />
      </div>
      <div className="aside-right"></div>
      <div className="footer">Footer</div>
    </div>
  );
}
