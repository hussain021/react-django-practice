import React, { Component } from "react";
import Issue from "./Issue";

class IssueList extends Component {
  state = {
    issueList: this.props.issueList,
  };
  componentDidMount() {
    console.log("createddddd");
    //this.setState({issueList:this.props.issueList})
    console.log(this.state.issueList.length);
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
      <div>
        <table className="table table-hover table-bordered">
          <tbody>
            {this.state.issueList.map((issue) => (
              <tr key={issue.id}>
                <td>
                  <Issue
                    title={issue.title}
                    id={issue.id}
                    isOpen={issue.isOpen}
                    createdBy={issue.createdBy}
                    createdTime={issue.createdTime}
                    isBugReported={issue.isBugReported}
                    needsTriage={issue.needsTriage}
                  />
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  }
}

export default IssueList;
