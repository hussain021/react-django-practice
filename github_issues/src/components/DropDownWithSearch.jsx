import React, { Component } from "react";
import SearchBar from "./SearchBar";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import Select from "@mui/material/Select";

class DropDownWithSearch extends Component {
  state = {
    title: this.props.title,
    items: this.props.items,
    onClick: this.props.onClick,
    selected: this.props.selected,
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
    this.state.onClick(event.target.value);
  };
}

export default DropDownWithSearch;
