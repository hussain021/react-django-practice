import React, { Component } from "react";

class Icon extends Component {
  state = {
    iconPath: this.props.iconPath,
    width: this.props.width,
  };
  render() {
    return <img src={this.state.iconPath} alt="" width={this.state.width} />;
  }
}

export default Icon;
