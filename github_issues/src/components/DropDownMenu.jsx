import React, { Component } from "react";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import Select from "@mui/material/Select";
class DropDownMenu extends Component {
  state = {
    title: this.props.title,
    items: this.props.items,
    selected: this.props.title,
  };
  render() {
    return (
      <React.Fragment>
        <InputLabel>{this.state.title}</InputLabel>
        <Select
          autoWidth
          value={this.state.selected}
          onChange={this.handleSearch}
        >
          {this.state.items.map((item, index) => (
            <MenuItem value={item} key={index}>
              {item}
            </MenuItem>
          ))}
        </Select>
      </React.Fragment>
    );
  }
  handleSearch = (event) => {
    this.setState({ selected: event.target.value });
  };
}

export default DropDownMenu;
