import React, { Component } from "react";
import "bootstrap/dist/css/bootstrap.css";
import IssueTab from "./IssueTab";
import Tab from "@mui/material/Tab";
import Box from "@mui/material/Box";
import { TabList } from "@material-ui/lab";
import { TabPanel } from "@material-ui/lab";
import { TabContext } from "@material-ui/lab";

class TabBar extends Component {
  state = {
    value: "1",
  };
  handleChange = (event, newValue) => {
    console.log(newValue);
    this.setState({ value: newValue });
  };
  render() {
    return (
      <React.Fragment>
        <Box sx={{ width: "100%", typography: "body1" }}>
          <TabContext value={this.state.value}>
            <Box sx={{ borderBottom: 1, borderColor: "divider" }}>
              <TabList
                onChange={this.handleChange}
                aria-label="lab API tabs example"
              >
                <Tab label="Code" value="1" />
                <Tab label="Issues" value="2" />
                <Tab label="Pull Requests" value="3" />
                <Tab label="Discussions" value="4" />
                <Tab label="Actions" value="5" />
                <Tab label="Projects" value="6" />
              </TabList>
            </Box>
            <TabPanel value="1">Code</TabPanel>
            <TabPanel value="2">
              <IssueTab />
            </TabPanel>
            <TabPanel value="3">Pull Requests</TabPanel>
            <TabPanel value="4">Discussions</TabPanel>
            <TabPanel value="5">Actions</TabPanel>
            <TabPanel value="6">Projects</TabPanel>
          </TabContext>
        </Box>
      </React.Fragment>
    );
  }
}

export default TabBar;
