import React, { Component } from "react";
import Issue from "./Issue";

class IssueList extends Component {
  state = {
    issueList: this.props.issueList,
  };
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
                    hasMessage={issue.hasMessage}
                    message={issue.message}
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
