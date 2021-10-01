import React, { Component } from "react";

class Icon extends Component {
  state = {
    path: this.props.path,
    width: this.props.width,
  };
  render() {
    return <img src={this.state.path} alt="" width={this.state.width} />;
  }
}

export default Icon;
