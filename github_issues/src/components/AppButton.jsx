import React, { Component } from "react";
import Icon from "./Icon";

class AppButton extends Component {
  state = {
    text: this.props.text,
    onClick: this.props.onClick,
    design: this.props.design,
    path: this.props.path,
    width: this.props.width,
  };
  render() {
    return (
      <button
        onClick={() => this.state.onClick(this.state.text)}
        className={this.state.design}
      >
        <Icon path={this.state.path} width={this.state.width} />
        &nbsp;{this.state.text}
      </button>
    );
  }
}

export default AppButton;
