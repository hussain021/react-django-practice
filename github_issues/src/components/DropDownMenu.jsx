import React, { Component } from "react";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import Select from "@mui/material/Select";
class DropDownMenu extends Component {
  state = {
    title: this.props.title,
    items: this.props.items,
    onClick: this.props.onClick,
  };
  render() {
    return (
      <React.Fragment>
        <InputLabel id="demo-simple-select-label">
          {this.state.title}
        </InputLabel>
        <Select
          labelId="demo-simple-select-label"
          id="demo-simple-select"
          className="menuStyle"
        >
          {this.state.items.map((item, index) => (
            <MenuItem key={index}>{item}</MenuItem>
          ))}
        </Select>
      </React.Fragment>
    );
  }
}

export default DropDownMenu;
