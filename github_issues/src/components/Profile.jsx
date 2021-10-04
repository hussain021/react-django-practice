import React from "react";
import Icon from "./Icon";

// About Page
const Profile = ({
  location: {
    state: { title, id, isOpen, createdTime, createdBy, hasMessage, message },
  },
}) => (
  <div>
    <h3>Title : {title}</h3>
    <h3>Status : {isOpen ? "opened" : "closed"}</h3>
    <h3>Created Time : {createdTime}</h3>
    <h3>Created By : {createdBy}</h3>
    <h3>
      Comment : {hasMessage ? message : <p>This issue has no comment!</p>}
    </h3>
  </div>
);

export default Profile;
