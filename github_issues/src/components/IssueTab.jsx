import React, { Component } from "react";
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
        <div id="Issues" className="tabcontent">
          <div className="marginLeft3">
            <DropDownWithSearch
              title="Filter"
              onClick={[this.handleSearch("id"), this.handleSearch("title")]}
              items={["id", "title"]}
            />
          </div>
          <div className="marginLeft2">
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
          <div className="marginLeft2">
            <AppButton onClick={this.handleNewIssue} text="New Issue" />
          </div>
          <hr />
          <br />
          <br />
          <br />
          <div className="marginLeft3">
            <DropDownWithSearch
              title="Author"
              onClick={[this.handleSearch("createdBy")]}
              items={["Author"]}
            />
          </div>
          <div className="marginLeft3">
            <DropDownMenu
              title="Labels"
              item1="Item1"
              item2="Item2"
              item3="Item3"
            />
          </div>
          <div className="marginLeft3">
            <DropDownMenu
              title="Projects"
              item1="Item1"
              item2="Item2"
              item3="Item3"
            />
          </div>
          <div className="marginLeft3">
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
        </div>
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
  handleSearch = (searchBy) => (searchString) => {
    console.log(searchBy + searchString);
    //if (searchBy !== "createdBy") searchBy = this.state.filterBy;
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
