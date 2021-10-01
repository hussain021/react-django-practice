import React, { Component } from "react";

class Title extends Component {
  state = {
    title: this.props.title,
    subTitle: this.props.subTitle,
  };
  render() {
    return (
      <h3 className="m-4 text-primary">
        <small>{this.state.title} &nbsp;</small>
        /&nbsp;
        {this.state.subTitle}
      </h3>
    );
  }
}

export default Title;
