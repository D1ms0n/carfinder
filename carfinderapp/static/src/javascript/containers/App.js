
import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {bindActionCreators} from 'redux';
import {connect} from 'react-redux';
import * as FormActions from '../actions/FormActions';
import text from './../services/texts/index';

import {withStyles} from "@material-ui/core/styles/index";
import CssBaseline from '@material-ui/core/CssBaseline';
import classNames from 'classnames';
import Footer from './../components/Footer/';
import Form from './../components/Form/';
import Results from './../components/Results';
import SnoopsList from './../components/SnoopsList';
import AuthActions from './../components/Header/';
import Badge from '@material-ui/core/Badge';
import Grid from '@material-ui/core/Grid';
import Drawer from '@material-ui/core/Drawer';
import IconButton from '@material-ui/core/IconButton';
import ChevronLeftIcon from '@material-ui/icons/ChevronLeft';
import Divider from '@material-ui/core/Divider';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import AppBar from '@material-ui/core/AppBar';
import MenuIcon from '@material-ui/icons/Menu';

const drawerWidth = 240;
const styles = theme => ({
  root: {
    flexGrow: 1,
  },
  appFrame: {
    zIndex: 1,
    overflow: 'hidden',
    position: 'relative',
    display: 'flex',
    width: '100%',
  },
  appBar: {
    position: 'absolute',
    transition: theme.transitions.create(['margin', 'width'], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    }),
  },
  appBarShift: {
    width: `calc(100% - ${drawerWidth}px)`,
    transition: theme.transitions.create(['margin', 'width'], {
      easing: theme.transitions.easing.easeOut,
      duration: theme.transitions.duration.enteringScreen,
    }),
  },
  'appBarShift-left': {
    marginLeft: drawerWidth,
  },
  menuButton: {
    marginLeft: 12,
    marginRight: 20,
  },
  hide: {
    display: 'none',
  },
  drawerPaper: {
    position: 'relative',
    width: drawerWidth,
  },
  drawerHeader: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'flex-end',
    padding: '0 8px',
    ...theme.mixins.toolbar,
  },
  content: {
    flexGrow: 1,
    backgroundColor: theme.palette.background.default,
    padding: theme.spacing.unit * 3,
    transition: theme.transitions.create('margin', {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    }),
  },
  'content-left': {
    marginLeft: -drawerWidth,
  },
  contentShift: {
    transition: theme.transitions.create('margin', {
      easing: theme.transitions.easing.easeOut,
      duration: theme.transitions.duration.enteringScreen,
    }),
  },
  'contentShift-left': {
    marginLeft: 0,
  },
  loaderWrapper: {
    textAlign: 'center',
    position: 'fixed',
    top: 0,
    left: 0,
    width: '100%!important',
    height: '100%!important',
    backgroundColor: 'rgba(227, 242, 253, .4)',
    zIndex: 10000,
    display:'flex',
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center'
  },
  loader: {
    textAlign: 'center'
  }
});

class App extends Component {

  constructor(props){
    super(props);
    this.state = {
      drawerOpen: false
    };
    this.handleDrawerToggle = this.handleDrawerToggle.bind(this);
  };

  handleDrawerToggle() {
    this.setState({
      drawerOpen: !this.state.drawerOpen
    })
  };

  render() {
    const {submitForm} = this.props.FormActions;
    const { classes } = this.props;
    const { drawerOpen } = this.state;
    const drawer = (
      <Drawer
        variant="persistent"
        anchor='left'
        open={drawerOpen}
        classes={{
          paper: classes.drawerPaper,
        }}
      >
        <div className={classes.drawerHeader}>
          <IconButton onClick={this.handleDrawerToggle}>
            <ChevronLeftIcon />
          </IconButton>
        </div>
        <Divider />
        <SnoopsList />
        <Divider />
      </Drawer>
    );
    return (
      <React.Fragment>
        <CssBaseline />
        <Grid
          container
          spacing={24}
          justify='center'
        >
          <Grid item lg={10} md={10} sm={10} xs={12}>
            <div className={classes.root}>
              <div className={classes.appFrame}>
                <AppBar
                  className={classNames(classes.appBar, {
                    [classes.appBarShift]: drawerOpen,
                    [classes['appBarShift-left']]: drawerOpen,
                  })}
                >
                  <Toolbar disableGutters={!drawerOpen}>
                    <IconButton
                      color='inherit'
                      aria-label='Open drawer'
                      onClick={this.handleDrawerToggle}
                      className={classNames(classes.menuButton, drawerOpen && classes.hide)}
                    >
                      <Badge color='secondary' badgeContent={4}>
                        <MenuIcon/>
                      </Badge>
                    </IconButton>
                    <Typography
                      variant='title'
                      color='inherit'
                      noWrap>
                      {text.texts.headerTitle}
                    </Typography>
                    <AuthActions />
                  </Toolbar>
                </AppBar>
                {drawer}
                <main
                  className={classNames(classes.content, classes['content-left'], {
                    [classes.contentShift]: drawerOpen,
                    [classes['contentShift-left']]: drawerOpen,
                  })}
                >
                  <div className={classes.drawerHeader} />
                  <Grid
                    container
                    spacing={24}
                    justify='center'
                  >
                    <Form
                      submitForm={submitForm}
                    />
                    <Results />
                  </Grid>
                </main>
              </div>
            </div>
          </Grid>
        </Grid>
        <Footer />
      </React.Fragment>
    );
  }
}

App.propTypes = {
  classes: PropTypes.object.isRequired
};

const mapStateToProps = state => {
  return {
    items: state.form.result,
    loading: state.loading.result,
  }
};

const mapDispatchToProps = dispatch => {
  return {
    FormActions: bindActionCreators(FormActions, dispatch),
  }
};

export default withStyles(styles)(connect(mapStateToProps, mapDispatchToProps)(App));
