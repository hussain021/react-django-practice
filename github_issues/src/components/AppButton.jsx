import React, { Component } from "react";
import Icon from "./Icon";

class AppButton extends Component {
  state = {
    text: this.props.text,
    onClick: this.props.onClick,
    buttonStyle: this.props.buttonStyle,
    iconPath: this.props.iconPath,
    width: this.props.width,
  };
  render() {
    return (
      <button
        onClick={() => this.state.onClick(this.state.text)}
        className={this.state.buttonStyle}
      >
        <Icon iconPath={this.state.iconPath} width={this.state.width} />
        &nbsp;{this.state.text}
      </button>
    );
  }
}

export default AppButton;
