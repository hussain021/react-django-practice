import React, { Component } from "react";
import AppButton from "./AppButton";

class ButtonWithCount extends Component {
  state = {
    path: this.props.path,
    width: this.props.width,
    count: this.props.count,
    name: this.props.name,
    onClick: this.props.onClick,
  };
  render() {
    return (
      <div className="m-2">
        <div className="btn-group" role="group">
          <AppButton
            design="btn btn-light border-right"
            onClick={() => this.state.onClick(this.state.name)}
            path={this.state.path}
            width={this.state.width}
            text={this.state.name}
          />
          <AppButton design="btn btn-light border" text={this.state.count} />
        </div>
      </div>
    );
  }
}

export default ButtonWithCount;
