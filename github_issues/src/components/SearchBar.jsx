import React, { Component } from "react";

class SearchBar extends Component {
  state = {
    id: this.props.id,
    onClick: this.props.onClick,
  };
  render() {
    return (
      <div>
        <link
          rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
        />

        <button
          style={{ width: "40px", height: "30px" }}
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
      </div>
    );
  }
}

export default SearchBar;
