import React, { Component } from "react";
import "bootstrap/dist/css/bootstrap.css";

class Issue extends Component {
  state = {
    title: this.props.title,
    id: this.props.id,
    isOpen: this.props.isOpen,
    createdBy: this.props.createdBy,
    createdTime: this.props.createdTime,
    isBugReported: this.props.isBugReported,
    needsTriage: this.props.needsTriage,
  };
  componentDidMount() {
    console.log("issue creatged");
  }
  render() {
    return (
      <div>
        <h3>
          {this.state.title}
          {this.state.title}
        </h3>
        <h5 style={{ color: "grey" }}>
          #{this.state.id} {this.state.isOpen ? "opened" : "closed"}{" "}
          {this.state.createdTime} by {this.state.createdBy}
        </h5>
      </div>
    );
  }
}

export default Issue;
