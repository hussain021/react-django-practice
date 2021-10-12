import { Typography } from "@mui/material";
import React from "react";

const Details = ({
  location: {
    state: { title, id, isOpen, createdTime, createdBy, hasMessage, message },
  },
}) => (
  <React.Fragment>
    <Typography variant="h5">Title : {title}</Typography>
    <Typography variant="h5">
      Status : {isOpen ? "opened" : "closed"}
    </Typography>
    <Typography variant="h5">Created Time : {createdTime}</Typography>
    <Typography variant="h5">Created By : {createdBy}</Typography>
    <Typography variant="h5">
      Comment : {hasMessage ? message : <p>This issue has no comment!</p>}
    </Typography>
  </React.Fragment>
);

export default Details;
