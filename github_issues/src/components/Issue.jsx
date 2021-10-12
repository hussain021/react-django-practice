import React from "react";
import "bootstrap/dist/css/bootstrap.css";
import { withRouter } from "react-router-dom";
import Icon from "./Icon";
import Typography from "@mui/material/Typography";
import { Box } from "@mui/system";

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
        <Box>
          <Typography variant="h5">
            {title}
            {title}
          </Typography>
          <div className="issueStyle">
            <Typography variant="h8">
              #{id} {isOpen ? "opened" : "closed"} {createdTime} by {createdBy}
              {hasMessage ? (
                <div className="issueMessageStyle">
                  <Icon p={5} iconPath="./message-solid.svg" width="20px" />
                </div>
              ) : (
                <div></div>
              )}
            </Typography>
          </div>
        </Box>
      </div>
    </React.Fragment>
  );
};

export default withRouter(Issue);
