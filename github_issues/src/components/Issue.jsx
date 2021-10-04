import React from "react";
import "bootstrap/dist/css/bootstrap.css";
import { withRouter } from "react-router-dom";
import Icon from "./Icon";

const Issue = ({
  title,
  id,
  isOpen,
  createdTime,
  createdBy,
  history,
  hasMessage,
  message,
}) => {
  const handleOnClick = () => {
    history.push(`/${id}`, {
      title,
      id,
      isOpen,
      createdTime,
      createdBy,
      hasMessage,
      message,
    });
  };
  return (
    <div onClick={handleOnClick}>
      <h3>
        {title}
        {title}
      </h3>
      <h5 style={{ color: "grey" }}>
        #{id} {isOpen ? "opened" : "closed"} {createdTime} by {createdBy}
        {hasMessage ? (
          <Icon path="./message-solid.svg" width="20px" />
        ) : (
          <div></div>
        )}
      </h5>
    </div>
  );
};

export default withRouter(Issue);
