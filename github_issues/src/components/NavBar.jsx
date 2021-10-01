import React, { Component } from "react";
import Icon from "./Icon";
class NavBar extends Component {
  state = {
    icon: Icon,
  };
  render() {
    return (
      <React.Fragment>
        <div style={{ background: "black", height: "70px" }}>
          <div style={{ display: "inline-block" }}>
            <Icon
              className="position-absolute top-0 end-0"
              width="30px"
              path="./bars-solid.svg"
            />
          </div>

          <div style={{ marginLeft: "45%", display: "inline-block" }}>
            <Icon
              className="position-absolute top-0 end-0"
              width="30px"
              path="./github-brands.svg"
            />
          </div>
          <div style={{ marginLeft: "48%", display: "inline-block" }}>
            <Icon
              className="invert_effect position-absolute top-0 end-0"
              width="30px"
              path="./bell-solid.svg"
            />
          </div>
        </div>
      </React.Fragment>
    );
  }
}

export default NavBar;
