import React, { Component } from "react";
import IssueList from "./IssueList";
import DropDownMenu from "./DropDownMenu";
import SearchBar from "./SearchBar";
import AppButton from "./AppButton";
import DropDownWithSearch from "./DropDownWithSearch";
import { withRouter } from "react-router";
import Pagination from "./Pagination";
import Issue from "./Issue";
class IssueTab extends Component {
  state = {
    issueList: [],
    searchedList: [],
    filterBy: "title",
    emptyList: false,
  };
  constructor() {
    super();
  }

  async componentDidMount() {
    // Simple POST request with a JSON body using fetch
    await this.fetchIssues();
  }
  componentDidUpdate(prevProps) {
    if (
      this.state.issueList !== "undefined" &&
      this.props.issueList !== prevProps.issueList
    ) {
      this.setState({ issueList: this.props.issueList });
    }
  }
  render() {
    return (
      <div id="Issues" className="tabcontent">
        <div style={{ marginLeft: "3%", display: "inline-block" }}>
          <DropDownMenu
            title="Filter"
            onClick={this.handleFilter}
            item1="id"
            item2="title"
          />
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
          <DropDownMenu
            title="Labels"
            item1="Item1"
            item2="Item2"
            item3="Item3"
          />
        </div>
        <div style={{ marginLeft: "3%", display: "inline-block" }}>
          <DropDownMenu
            title="Projects"
            item1="Item1"
            item2="Item2"
            item3="Item3"
          />
        </div>
        <div style={{ marginLeft: "3%", display: "inline-block" }}>
          <DropDownMenu
            title="Milestones"
            item1="Item1"
            item2="Item2"
            item3="Item3"
          />
        </div>
        {this.state.emptyList ? (
          <h3>No issue available</h3>
        ) : (
          <Pagination
            data={this.state.searchedList}
            RenderComponent={Issue}
            title="Issues"
            pageLimit={1}
            dataLimit={10}
          />
        )}
      </div>
    );
  }

  handleFilter = (filterBy) => {
    this.setState({ filterBy: filterBy });
  };

  showAlert = () => {
    alert("Button not implemented");
  };

  handleSearch = (searchBy) => (searchString) => {
    if (searchBy !== "createdBy") searchBy = this.state.filterBy;
    if (this.state.issueList) {
      var searchedList = [];
      for (var issue in this.state.issueList) {
        if (searchBy === "id") {
          if (this.state.issueList[issue][searchBy] === searchString) {
            searchedList.push(this.state.issueList[issue]);
          }
        } else {
          if (
            this.state.issueList[issue][searchBy]
              .toLowerCase()
              .includes(searchString.toLowerCase())
          )
            searchedList.push(this.state.issueList[issue]);
        }
      }
      if (searchedList.length === 0) this.setState({ emptyList: true });
      else {
        this.setState({ emptyList: false });
        this.setState({ searchedList: searchedList });
      }
    }
    if (searchString === "") {
      this.setState({ searchedList: this.state.issueList });
    }
  };

  fetchIssues = async () => {
    const requestOptions = {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    };
    const response = await fetch(
      "https://615448672473940017efad57.mockapi.io/issues",
      requestOptions
    ).then((response) => response.json());
    var newIssueList = [];
    response.forEach(function (issue) {
      newIssueList.push(issue);
    });
    newIssueList.sort((a, b) =>
      a.createdTime > b.createdTime ? 1 : b.createdTime > a.createdTime ? -1 : 0
    );
    this.setState({ issueList: newIssueList, searchedList: newIssueList });
  };
  handleNewIssue = async () => {
    this.props.history.push(`/newIssue`, {});
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

export default withRouter(IssueTab);
