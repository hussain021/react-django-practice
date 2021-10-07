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
        <div className="dropdown">
          <div className="trigger">
            {this.state.title}
            <div className="subAuthor">
              <div className="item" style={{ width: "200px" }}>
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
