import React, { Component } from "react";
import NavBar from "./NavBar";
import Title from "./Title";
import ButtonWithCount from "./ButtonWithCount";
import "bootstrap/dist/css/bootstrap.css";
import TabBar from "./TabBar";
import { watch, unwatch, fork, unfork, star, unstar } from "../constants.js";

class Home extends Component {
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
      <React.Fragment>
        <NavBar />
        <div className="buttonCountMargin">
          <Title title="facebook" subTitle="create-react-app" />
        </div>
        <div className="firstButtonCount">
          <ButtonWithCount
            key={this.state.watch["value"] ? watch : unwatch}
            onClick={this.handleToggle("watch")}
            name={this.state.watch["value"] ? watch : unwatch}
            count={this.state.watch["count"]}
            iconPath="./eye-solid.svg"
            width="20px"
          />
        </div>
        <div className="buttonCountMargin">
          <ButtonWithCount
            key={this.state.star["value"] ? star : unstar}
            onClick={this.handleToggle("star")}
            name={this.state.star["value"] ? star : unstar}
            count={this.state.star["count"]}
            iconPath="./star-solid.svg"
            width="20px"
          />
        </div>
        <div className="buttonCountMargin">
          <ButtonWithCount
            key={this.state.fork["value"] ? fork : unfork}
            onClick={this.handleToggle("fork")}
            name={this.state.fork["value"] ? fork : unfork}
            count={this.state.fork["count"]}
            iconPath="./code-fork-solid.svg"
            width="20px"
          />
        </div>
        <br />

        <TabBar />
      </React.Fragment>
    );
  }

  handleToggle = (tag) => async (abc) => {
    var value = !this.state[tag]["value"];
    var count = this.state[tag]["count"];
    if (value === true) count--;
    else count++;
    this.setState({ [tag]: { value: value, count: count } });
  };
}

export default Home;
