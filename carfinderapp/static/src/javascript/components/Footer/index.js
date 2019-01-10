import React, { Component } from 'react';
import IconButton from '@material-ui/core/IconButton';
import ExpandLess from '@material-ui/icons/ExpandLess';
import { withStyles } from '@material-ui/core/styles/index';
const scroll = require('window-scroll');

const styles = theme => ({
  iconWrap: {
    width: 58,
    height: 58
  },
  icon: {
    margin: theme.spacing.unit,
    fontSize: 50,
    marginTop: 4
  },
  '@global': {
    '.scrollToTop': {
      position: 'fixed',
      transition: 'all .2s ease-in-out',
      right: -150,
      bottom: 15
    },
    '.scrollToTop.active': {
      right: 15,
    }
  }
});

class Index extends Component {
  constructor(props) {
    super(props);
    this.state = {
      scrollToTopIsShown: false,
      scrollPositionToShowScroll: 250
    };
    this.showScrollToTop = this.showScrollToTop.bind(this);
    this.scrollToTop = this.scrollToTop.bind(this);
  }
  componentDidMount() {
    window.addEventListener('scroll', this.showScrollToTop);
  }
  componentWillUnmount() {
    window.removeEventListener('scroll', this.showScrollToTop);
  }
  showScrollToTop(){
    if ( scroll.getScrollY() > this.state.scrollPositionToShowScroll ){
      this.setState({
        scrollToTopIsShown: true
      });
    } else {
      this.setState({
        scrollToTopIsShown: false
      });
    }
  }
  scrollToTop(){
    (function smoothscroll(){
      const currentScroll = document.documentElement.scrollTop || document.body.scrollTop;
      if (currentScroll > 0) {
        window.requestAnimationFrame(smoothscroll);
        window.scrollTo(0,currentScroll - (currentScroll/5));
      }
    })();
  }
  render() {
    const {classes} = this.props;
    return (
      <div>
        <footer className="shop_footer">
          <div className={'scrollToTop ' + (this.state.scrollToTopIsShown === true ? 'active' : '')}
            onClick={this.scrollToTop}>
            <IconButton aria-label="Share" className={classes.iconWrap} >
              <ExpandLess className={classes.icon} />
            </IconButton>
          </div>
        </footer>
      </div>
    );
  }
}

export default withStyles(styles)(Index);