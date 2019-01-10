import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {connect} from 'react-redux';
import {withStyles} from '@material-ui/core/styles/index';
import text from './../../services/texts/index';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import IconButton from '@material-ui/core/IconButton';
import FavoriteIcon from '@material-ui/icons/Favorite';
import ShareIcon from '@material-ui/icons/Share';
import Room from '@material-ui/icons/Room';
import BatteryFull from '@material-ui/icons/BatteryFull';
import DirectionsWalk from '@material-ui/icons/DirectionsWalk';
import DirectionsCar from '@material-ui/icons/DirectionsCar';
import Paper from '@material-ui/core/Paper';

const styles = (theme) => ({
  resultsWrapper: {
    textAlign: 'left',
    margin: 0,
    padding: 0
  },
  listItem: {
    padding: 0,
    marginBottom: 25
  },
  card: {
    borderRadius: 0
  },
  gridContainer: {
    margin: 0,
    width: '100%'
  },
  paperRelative: {
    margin: 0
  },
  content: {
    width: '55%',
    float: 'right'
  },
  cover: {
    width: '45%',
    height: 300,
    float: 'left',
  },
  paper: {
    padding: 15,
    marginTop: 10,
    borderRadius: 0,
    color: theme.palette.text.secondary,
    boxShadow: 'none',
    textAlign: 'center'
  }
});

class Results extends Component {
  render() {
    const {items, classes} = this.props;
    const noResults = text.texts.noResults;
    return (
      <Grid className={classes.grid} item lg={9} md={8} sm={7} xs={11}>
        <Paper className={classes.paper}>
          <List className={classes.resultsWrapper}>
            { items.length === 0 ? noResults : null }
            { items.map( (item,index) => {
              return (
                <ListItem key={index} className={classes.listItem}>
                  <Card className={classes.card}>
                    <CardMedia
                      className={classes.cover}
                      image={item.img}
                      title={item.name}
                    />
                    <div className={classes.details}>
                      <CardContent className={classes.content}>
                        <Typography variant="headline">{item.name}</Typography>
                        <Typography variant="subheading" gutterBottom>
                          {item.price}
                        </Typography>
                        <Grid
                          className={classes.gridContainer}
                          container
                          spacing={24}
                          justify='center'
                          direction='row'
                        >
                          <Grid className={classes.paperRelative} item lg={6} md={6} sm={6} xs={12}>
                            <Typography variant="body2" gutterBottom>
                              <Room /> {item.place}
                            </Typography>
                          </Grid>
                          <Grid className={classes.paperRelative} item lg={6} md={6} sm={6} xs={12}>
                            <Typography variant="body2" gutterBottom>
                              <BatteryFull /> {item.engine}
                            </Typography>
                          </Grid>
                          <Grid className={classes.paperRelative} item lg={6} md={6} sm={6} xs={12}>
                            <Typography variant="body2" gutterBottom>
                              <DirectionsWalk/> {item.millage}
                            </Typography>
                          </Grid>
                          <Grid className={classes.paperRelative} item lg={6} md={6} sm={6} xs={12}>
                            <Typography variant="body2" gutterBottom>
                              <DirectionsCar /> {item.transmission}
                            </Typography>
                          </Grid>
                        </Grid>
                      </CardContent>
                      <Grid
                        className={classes.gridContainer}
                        container
                        spacing={24}
                        justify='center'
                        direction='row'
                      >
                        <Grid className={classes.paperRelative} item lg={12} md={12} sm={12} xs={12}>
                          <Typography variant="body2" gutterBottom>
                            {item.description}
                          </Typography>
                          <Typography variant="caption" gutterBottom align="right">
                            {item.date}
                          </Typography>
                        </Grid>
                      </Grid>
                    </div>
                    <IconButton aria-label="Add to favorites">
                      <FavoriteIcon />
                    </IconButton>
                    <IconButton aria-label="Share">
                      <ShareIcon />
                    </IconButton>
                  </Card>
                </ListItem>
              )})}
          </List>
        </Paper>
      </Grid>
    );
  }
}

Results.propTypes = {
  items: PropTypes.array.isRequired
};

const mapStateToProps = state => {
  return {
    items: state.form.result
  }
};

export default withStyles(styles)(connect(mapStateToProps)(Results));
