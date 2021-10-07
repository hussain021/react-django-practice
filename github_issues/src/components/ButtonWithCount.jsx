import React, { Component } from "react";
import AppButton from "./AppButton";

class ButtonWithCount extends Component {
  state = {
    iconPath: this.props.iconPath,
    width: this.props.width,
    count: this.props.count,
    name: this.props.name,
    onClick: this.props.onClick,
  };
  render() {
    return (
      <React.Fragment>
        <div className="btn-group m-2" role="group">
          <AppButton
            buttonStyle="btn btn-light border-right"
            onClick={() => this.state.onClick(this.state.name)}
            iconPath={this.state.iconPath}
            width={this.state.width}
            text={this.state.name}
          />
          <AppButton
            buttonStyle="btn btn-light border"
            text={this.state.count}
          />
        </div>
      </React.Fragment>
    );
  }
}

export default ButtonWithCount;
