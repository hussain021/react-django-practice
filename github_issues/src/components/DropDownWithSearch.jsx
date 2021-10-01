import React, { Component } from "react";
import SearchBar from "./SearchBar";

class DropDownWithSearch extends Component {
  state = {
    title: this.props.title,
    onClick: this.props.onClick,
  };
  render() {
    return (
      <div className="dropdown">
        <div className="trigger">
          {this.state.title}
          <div className="subAuthor">
            <div className="item" style={{ width: "200px" }}>
              {" "}
              <div style={{ marginLeft: "2%", display: "inline-block" }}>
                <SearchBar id="author" onClick={this.handleSearch} />
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
  handleSearch = (searchString) => {
    console.log("search:" + searchString);
    this.state.onClick(searchString);
  };
}

export default DropDownWithSearch;
