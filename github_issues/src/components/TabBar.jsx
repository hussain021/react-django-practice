import React, { Component } from "react";
import AppButton from "./AppButton";
import "bootstrap/dist/css/bootstrap.css";
import IssueTab from "./IssueTab";

class TabBar extends Component {
  render() {
    return (
      <div>
        <AppButton
          id="Code"
          onClick={this.handleActivation}
          text="Code"
          design="border p-4"
          width="20px"
          path="code-solid.svg"
        ></AppButton>
        <AppButton
          id="Issues"
          onClick={this.handleActivation}
          text="Issues"
          design="border p-4"
          width="20px"
          path="circle-exclamation-solid.svg"
        ></AppButton>
        <AppButton
          id="PullRequests"
          onClick={this.handleActivation}
          text="PullRequests"
          design="border p-4"
          width="20px"
          path="code-pull-request-solid.svg"
        ></AppButton>
        <AppButton
          id="Discussions"
          onClick={this.handleActivation}
          text="Discussions"
          design="border p-4"
          width="20px"
          path="comments-solid.svg"
        ></AppButton>
        <AppButton
          id="Actions"
          onClick={this.handleActivation}
          text="Actions"
          design="border p-4"
          width="20px"
          path="circle-play-solid.svg"
        ></AppButton>
        <AppButton
          id="Projects"
          onClick={this.handleActivation}
          text="Projects"
          design="border p-4"
          width="20px"
          path="bars-solid.svg"
        ></AppButton>
        <div id="Code" className="tabcontent">
          <h3>Code</h3>
          <p>Code snippet not available!</p>
        </div>

        <IssueTab id="Issues" className="tabcontent" />

        <div id="PullRequests" className="tabcontent">
          <h3>Pull Requests</h3>
          <p>No pull requests</p>
        </div>

        <div id="Discussions" className="tabcontent">
          <h3>Discussions</h3>
          <p>No Discussions</p>
        </div>

        <div id="Actions" className="tabcontent">
          <h3>Actions</h3>
          <p>No Actions</p>
        </div>

        <div id="Projects" className="tabcontent">
          <h3>Projects</h3>
          <p>No Projects</p>
        </div>
      </div>
    );
  }

  handleActivation = (id) => {
    console.log("eeventt" + id);
    var i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(id).style.display = "block";
    document.getElementById(id).className += " active";
  };
}

export default TabBar;
