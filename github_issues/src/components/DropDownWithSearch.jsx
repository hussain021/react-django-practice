import React, { Component } from "react";
import SearchBar from "./SearchBar";

class DropDownWithSearch extends Component {
  state = {
    title: this.props.title,
    items: this.props.items,
    onClick: this.props.onClick,
  };
  render() {
    return (
      <React.Fragment>
        <div className="dropdown trigger">
          {this.state.title}
          <div className="item subAuthor" style={{ width: "200px" }}>
            {" "}
            {this.state.items.map((item, index) => (
              <div key={index} className="searchBarSpacing">
                <SearchBar
                  id={item}
                  onClick={this.handleSearch(this.state.onClick[index])}
                />
              </div>
            ))}
          </div>
        </div>
      </React.Fragment>
    );
  }
  handleSearch = (onClick) => (searchString) => {
    onClick(searchString);
  };
}

export default DropDownWithSearch;
