import React, { Component } from "react";

class SearchBar extends Component {
  state = {
    id: this.props.id,
    onClick: this.props.onClick,
  };
  render() {
    return (
      <React.Fragment>
        <link
          rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
        />

        <button
          className="width30Height40"
          onClick={() =>
            this.state.onClick(document.getElementById(this.state.id).value)
          }
        >
          <i className="fa fa-search"></i>
        </button>
        <input
          id={this.state.id}
          type="text"
          placeholder="Search.."
          name="search"
        />
      </React.Fragment>
    );
  }
}

export default SearchBar;
