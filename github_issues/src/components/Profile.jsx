import React from "react";

// About Page
const Profile = ({
  location: {
    state: { title, id, isOpen, createdTime, createdBy, hasMessage, message },
  },
}) => (
  <React.Fragment>
    <h3>Title : {title}</h3>
    <h3>Status : {isOpen ? "opened" : "closed"}</h3>
    <h3>Created Time : {createdTime}</h3>
    <h3>Created By : {createdBy}</h3>
    <h3>
      Comment : {hasMessage ? message : <p>This issue has no comment!</p>}
    </h3>
  </React.Fragment>
);

export default Profile;
