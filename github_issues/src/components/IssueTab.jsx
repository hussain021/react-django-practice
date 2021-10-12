import React, { Component } from "react";
import DropDownMenu from "./DropDownMenu";
import AppButton from "./AppButton";
import DropDownWithSearch from "./DropDownWithSearch";
import { withRouter } from "react-router";
import Pagination from "./Pagination";
import Issue from "./Issue";
import SearchBar from "./SearchBar";
import { Typography } from "@mui/material";

class IssueTab extends Component {
  state = {
    issueList: [],
    searchedList: [],
    filterBy: "title",
    emptyList: false,
    currentPage: 1,
  };

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
      <React.Fragment>
        <br />
        <br />

        <div className="dropDownMenu">
          <DropDownWithSearch
            title="Filter"
            onClick={this.handleFilter}
            items={["id", "title", "author"]}
            selected="title"
          />
        </div>
        <SearchBar id="mainSearch" onClick={this.handleSearch("title")} />
        <div className="issueTabMargin">
          <AppButton
            onClick={this.showAlert}
            text="Labels"
            iconPath="./tag-solid.svg"
            width="30px"
          />
        </div>
        <div className="inlineBlock">
          <AppButton
            onClick={this.showAlert}
            text="MileStones"
            iconPath="./arrow-right-solid.svg"
            width="30px"
          />
        </div>
        <div className="issueTabMargin">
          <AppButton onClick={this.handleNewIssue} text="New Issue" />
        </div>
        <hr />
        <br />
        <br />
        <br />
        <div className="dropDownMenu">
          <DropDownMenu
            title="Labels"
            selected="Select"
            items={["Item1", "Item2", "Item3"]}
          />
        </div>
        <div className="dropDownMenu">
          <DropDownMenu
            title="Projects"
            selected="Select"
            items={["Item1", "Item2", "Item3"]}
          />
        </div>
        <div className="dropDownMenu">
          <DropDownMenu
            title="Milestones"
            items={["Item1", "Item2", "Item3"]}
            selected="Select"
          />
        </div>
        {this.state.emptyList ? (
          <Typography variant="h5">No issue available</Typography>
        ) : (
          <React.Fragment>
            <h1>Issues</h1>

            <div className="dataContainer">
              {this.getPaginatedData().map((d, idx) => (
                <Issue
                  key={idx}
                  title={d.title}
                  id={d.id}
                  isOpen={d.isOpen}
                  createdTime={d.createdTime}
                  createdBy={d.createdBy}
                  hasMessage={d.hasMessage}
                  message={d.message}
                />
              ))}
            </div>
            <Pagination
              data={this.state.searchedList}
              title="Issues"
              pageLimit={1}
              dataLimit={10}
              onClick={this.handlePagination}
            />
          </React.Fragment>
        )}
      </React.Fragment>
    );
  }

  handleFilter = (filterBy) => {
    this.setState({ filterBy: filterBy });
  };

  showAlert = () => {
    alert("Button not implemented");
  };
  handlePagination = (currentPage) => {
    this.setState({ currentPage: currentPage });
  };
  getPaginationGroup = () => {
    let start = Math.floor((this.state.currentPage - 1) / 1) * 1;
    return new Array(1).fill().map((_, idx) => start + idx + 1);
  };
  getPaginatedData = () => {
    const startIndex = this.state.currentPage * 10 - 10;
    const endIndex = startIndex + 10;
    return this.state.searchedList.slice(startIndex, endIndex);
  };
  handleFilter = (filterBy) => {
    this.setState({ filterBy: filterBy });
  };

  handleSearch = (searchBy) => (searchString) => {
    console.log(searchBy + searchString);
    if (searchBy !== "createdBy") searchBy = this.state.filterBy;
    if (searchBy === "author") searchBy = "createdBy";
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
