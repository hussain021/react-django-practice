import React, { Component } from "react";

class DropDownMenu extends Component {
  state = {
    title: this.props.title,
  };
  render() {
    return (
      <div className="dropdown">
        <div className="trigger">
          {this.state.title}
          <div className="sub">
            <div className="item">Item 1</div>
            <div className="item">Item 2</div>
            <div className="item">Item 3</div>
          </div>
        </div>
      </div>
    );
  }
}

export default DropDownMenu;
