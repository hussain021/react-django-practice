import React, { Component } from "react";
import { Img } from "react-image";

class Icon extends Component {
  state = {
    iconPath: this.props.iconPath,
    width: this.props.width,
  };
  render() {
    return <Img src={this.state.iconPath} alt="" width={this.state.width} />;
  }
}

export default Icon;
