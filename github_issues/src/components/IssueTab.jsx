import React, { Component } from "react";
import IssueList from "./IssueList";
import DropDownMenu from "./DropDownMenu";
import SearchBar from "./SearchBar";
import AppButton from "./AppButton";
import DropDownWithSearch from "./DropDownWithSearch";

class IssueTab extends Component {
  state = {
    issueList: [],
    searchedList: [],
  };
  constructor() {
    super();
    console.log("constructor called");
  }

  async componentDidMount() {
    // Simple POST request with a JSON body using fetch
    await this.fetchIssues();
  }
  componentDidUpdate(prevProps) {
    console.log("updated");
    if (
      this.state.issueList !== "undefined" &&
      this.props.issueList !== prevProps.issueList
    ) {
      this.setState({ issueList: this.props.issueList });
    }
    console.log(this.state.issueList.length);
  }
  render() {
    return (
      <div id="Issues" className="tabcontent">
        <div style={{ marginLeft: "3%", display: "inline-block" }}>
          <DropDownMenu title="Filter" />
        </div>
        <div style={{ marginLeft: "2%", display: "inline-block" }}>
          <SearchBar id="mainSearch" onClick={this.handleSearch("title")} />
        </div>
        <div style={{ marginLeft: "2%", display: "inline-block" }}>
          <AppButton
            onClick={this.showAlert}
            text="Labels"
            path="./tag-solid.svg"
            width="30px"
          />
        </div>
        <div style={{ display: "inline-block" }}>
          <AppButton
            onClick={this.showAlert}
            text="MileStones"
            path="./arrow-right-solid.svg"
            width="30px"
          />
        </div>
        <div
          style={{ marginLeft: "2%", display: "inline-block", color: "green" }}
        >
          <AppButton onClick={this.handleNewIssue} text="New Issue" />
        </div>
        <hr />
        <div style={{ marginLeft: "3%", display: "inline-block" }}>
          <DropDownWithSearch
            onClick={this.handleSearch("createdBy")}
            title="Author"
          />
        </div>
        <div style={{ marginLeft: "3%", display: "inline-block" }}>
          <DropDownMenu title="Labels" />
        </div>
        <div style={{ marginLeft: "3%", display: "inline-block" }}>
          <DropDownMenu title="Projects" />
        </div>
        <div style={{ marginLeft: "3%", display: "inline-block" }}>
          <DropDownMenu title="Milestones" />
        </div>

        <IssueList issueList={this.state.searchedList} />
      </div>
    );
  }

  showAlert = () => {
    alert("Button not implemented");
  };

  handleSearch = (searchBy) => (searchString) => {
    console.log("search:" + searchBy);
    if (this.state.issueList) {
      var searchedList = [];
      for (var issue in this.state.issueList) {
        if (
          this.state.issueList[issue][searchBy]
            .toLowerCase()
            .includes(searchString.toLowerCase())
        )
          searchedList.push(this.state.issueList[issue]);
      }
      this.setState({ searchedList: searchedList });
    }
    if (searchString === "") {
      this.setState({ searchedList: this.state.issueList });
    }
  };

  fetchIssues = async () => {
    console.log("running post request");
    const requestOptions = {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    };
    const response = await fetch(
      "https://615448672473940017efad57.mockapi.io/issues",
      requestOptions
    ).then((response) => response.json());
    console.log(response);
    var newIssueList = [];
    response.forEach(function (issue) {
      newIssueList.push(issue);
    });
    this.setState({ issueList: newIssueList, searchedList: newIssueList });
    console.log(this.state.issueList.length);
  };
  handleNewIssue = async () => {
    console.log("running post request");
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
    };
    await fetch(
      "https://615448672473940017efad57.mockapi.io/issues",
      requestOptions
    ).then((response) => response.json());
    alert("New random issue created");
    await this.fetchIssues();
  };
}

export default IssueTab;
