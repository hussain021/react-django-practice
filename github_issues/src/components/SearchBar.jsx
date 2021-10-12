import React, { Component } from "react";
import AppButton from "./AppButton";
import TextField from "@mui/material/TextField";

class SearchBar extends Component {
  state = {
    id: this.props.id,
    onClick: this.props.onClick,
  };
  render() {
    return (
      <React.Fragment>
        <AppButton
          className="searchBarStyle"
          onClick={() =>
            this.state.onClick(document.getElementById(this.state.id).value)
          }
          iconPath="./magnifying-glass-solid.svg"
          width="20px"
        />
        <TextField
          id={this.state.id}
          label={this.state.id}
          variant="outlined"
          placeholder={this.state.id}
          className="searchStyle"
        />
      </React.Fragment>
    );
  }
}

export default SearchBar;
