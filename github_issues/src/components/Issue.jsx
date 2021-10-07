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
    <React.Fragment>
      <div onClick={handleOnClick}>
        <h3>
          {title}
          {title}
        </h3>
        <div className="width90">
          <h5>
            #{id} {isOpen ? "opened" : "closed"} {createdTime} by {createdBy}
            {hasMessage ? (
              <div style={{ display: "inline-block", paddingLeft: "55%" }}>
                <Icon iconPath="./message-solid.svg" width="20px" />
              </div>
            ) : (
              <div></div>
            )}
          </h5>
        </div>
      </div>
    </React.Fragment>
  );
};

export default withRouter(Issue);
