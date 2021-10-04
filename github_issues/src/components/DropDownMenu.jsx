import React, { Component } from "react";

class DropDownMenu extends Component {
  state = {
    title: this.props.title,
    item1: this.props.item1,
    item2: this.props.item2,
    item3: this.props.item3,
    onClick: this.props.onClick,
  };
  render() {
    return (
      <div className="dropdown">
        <div className="trigger">
          {this.state.title}
          <div className="sub">
            <div className="item">
              <button onClick={() => this.state.onClick(this.state.item1)}>
                {this.state.item1}
              </button>
            </div>
            <div className="item">
              <button onClick={() => this.state.onClick(this.state.item2)}>
                {this.state.item2}
              </button>
            </div>
            <div className="item">
              <button onClick={() => this.state.onClick(this.state.item3)}>
                {this.state.item3}
              </button>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default DropDownMenu;
