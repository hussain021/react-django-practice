import React, { Component } from "react";
import Icon from "./Icon";
class NavBar extends Component {
  state = {
    icon: Icon,
  };
  render() {
    return (
      <React.Fragment>
        <div className="navBarBackground">
          <div className="inlineBlock">
            <Icon
              className="position-absolute top-0 end-0"
              width="30px"
              iconPath="./bars-solid.svg"
            />
          </div>

          <div className="navBarIconStyle">
            <Icon
              className="position-absolute top-0 end-0"
              width="30px"
              iconPath="./github-brands.svg"
            />
          </div>
          <div className="navBarIconStyle">
            <Icon
              className="invert_effect position-absolute top-0 end-0"
              width="30px"
              iconPath="./bell-solid.svg"
            />
          </div>
        </div>
      </React.Fragment>
    );
  }
}

export default NavBar;
