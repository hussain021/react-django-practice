import "./App.css";
import React, { Component } from "react";
import NavBar from "./components/NavBar";
import Title from "./components/Title";
import ButtonWithCount from "./components/ButtonWithCount";
import "bootstrap/dist/css/bootstrap.css";
import TabBar from "./components/TabBar";

class App extends Component {
  constructor() {
    super();
    this.state = {
      watch: { value: true, count: 100 },
      fork: { value: true, count: 100 },
      star: { value: true, count: 100 },
    };
  }

  render() {
    return (
      <div>
        <NavBar />
        <div style={{ marginLeft: "5%", display: "inline-block" }}>
          <Title title="facebook" subTitle="create-react-app" />
        </div>
        <div style={{ marginLeft: "30%", display: "inline-block" }}>
          <ButtonWithCount
            key={this.state.watch["value"] ? "Watch" : "Unwatch"}
            onClick={this.handleToggle("watch")}
            name={this.state.watch["value"] ? "Watch" : "Unwatch"}
            count={this.state.watch["count"]}
            path="./eye-solid.svg"
            width="20px"
          />
        </div>
        <div style={{ marginLeft: "5%", display: "inline-block" }}>
          <ButtonWithCount
            key={this.state.star["value"] ? "Star" : "Unstar"}
            onClick={this.handleToggle("star")}
            name={this.state.star["value"] ? "Star" : "Unstar"}
            count={this.state.star["count"]}
            path="./star-solid.svg"
            width="20px"
          />
        </div>
        <div style={{ marginLeft: "5%", display: "inline-block" }}>
          <ButtonWithCount
            key={this.state.fork["value"] ? "Fork" : "Unfork"}
            onClick={this.handleToggle("fork")}
            name={this.state.fork["value"] ? "Fork" : "Unfork"}
            count={this.state.fork["count"]}
            path="./code-fork-solid.svg"
            width="20px"
          />
        </div>
        <TabBar />
      </div>
    );
  }
  handleToggle = (tag) => (abc) => {
    console.log("tag is" + tag + this.state[tag]["value"]);
    var value = !this.state[tag]["value"];
    var count = this.state[tag]["count"];
    if (value === true) count--;
    else count++;
    this.setState({ [tag]: { value: value, count: count } });
  };
}

export default App;
