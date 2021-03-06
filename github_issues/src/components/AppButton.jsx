import React, { Component } from "react";
import Icon from "./Icon";
import { Button } from "react-bootstrap";

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
      <Button
        onClick={() => this.state.onClick(this.state.text)}
        variant="success"
      >
        <Icon iconPath={this.state.iconPath} width={this.state.width} />
        &nbsp;{this.state.text}
      </Button>
    );
  }
}

export default AppButton;
