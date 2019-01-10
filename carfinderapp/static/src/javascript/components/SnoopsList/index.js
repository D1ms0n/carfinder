
import React, {Component} from 'react';
import {withStyles} from '@material-ui/core/styles/index';

import text from './../../services/texts/index';
import ApiService from './../../services/api';
import config from './../../configs';

import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemSecondaryAction from '@material-ui/core/ListItemSecondaryAction';
import ListItemText from '@material-ui/core/ListItemText';
import Avatar from '@material-ui/core/Avatar';
import DeleteIcon  from '@material-ui/icons/Delete';
import IconButton from '@material-ui/core/IconButton';
import Divider from '@material-ui/core/Divider';
import Badge from '@material-ui/core/Badge';
import Typography from '@material-ui/core/Typography';

const styles = (theme) => ({
  resultsWrapper: {
    textAlign: 'left',
    margin: 0,
    padding: 0
  },
  noResultsContainer: {
    textAlign: 'center'
  },
  title: {
    paddingLeft: 20,
    paddingTop: 20
  }
});

class SnoopsList extends Component {

  constructor(props) {
    super(props);
    this.config = config();
    this.state = {
      snoops: []
    };
  }

  componentDidMount() {
    const apiService = new ApiService();
    apiService.getRequest(this.config.snoops)
      .then((result)=>{
        console.log(result);
        this.setState({
          snoops: result || []
        })
      }).catch((e)=>{
        console.log(e);
    });
  }

  render() {
    const {classes} = this.props;
    const {snoops} = this.state;
    const noResults = (
      <div className={classes.noResultsContainer}>
        {text.texts.noResultsSnoops}
      </div>
    );
    return (
      <div>
        <Typography className={classes.title} variant="title" gutterBottom>
          {text.texts.snoops}
        </Typography>
        <List>
          { Array.isArray(snoops) && snoops.length > 0
            ? snoops.map(value => (
              <ListItem key={value} dense button className={classes.listItem}>
                <Avatar alt="preview" src="https://material-ui.com/static/images/remy.jpg" />
                <Badge color='secondary' badgeContent={1}>
                  <ListItemText primary={`Line item ${value + 1}`} />
                </Badge>
                <ListItemSecondaryAction>
                  <IconButton aria-label='Delete'>
                    <DeleteIcon />
                  </IconButton>
                </ListItemSecondaryAction>
                <Divider />
              </ListItem>
              ))
            : noResults
          }
        </List>
      </div>
    );
  }
}

export default withStyles(styles)(SnoopsList);
