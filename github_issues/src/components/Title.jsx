import { Typography } from "@mui/material";
import React, { Component } from "react";

class Title extends Component {
  state = {
    title: this.props.title,
    subTitle: this.props.subTitle,
  };
  render() {
    return (
      <Typography variant="h5">
        <small>{this.state.title} &nbsp;</small>
        /&nbsp;
        {this.state.subTitle}
      </Typography>
    );
  }
}

export default Title;
