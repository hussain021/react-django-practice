import "./App.css";
import React, { Component } from "react";
import "bootstrap/dist/css/bootstrap.css";
import Details from "./components/Details";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import Home from "./components/Home";
import NewIssue from "./components/NewIssue";

class App extends Component {
  render() {
    return (
      <div>
        <BrowserRouter>
          <Switch>
            <Route exact path="/" component={Home} />
            <Route exact path="/newIssue" component={NewIssue} />
            <Route path="/:id" component={Details} />
          </Switch>
        </BrowserRouter>
      </div>
    );
  }
}

export default App;
