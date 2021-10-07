import React, { Component } from "react";

class DropDownMenu extends Component {
  state = {
    title: this.props.title,
    items: [this.props.item1, this.props.item2, this.props.item3],
    onClick: this.props.onClick,
  };
  render() {
    return (
      <div className="dropdown trigger">
        {this.state.title}
        <div className="sub item">
          {this.state.items.map((item, index) => (
            <div key={index} className="item">
              {item}
            </div>
          ))}
        </div>
      </div>
    );
  }
}

export default DropDownMenu;
