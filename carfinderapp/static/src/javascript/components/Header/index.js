
import React, {Component} from 'react';
import IconButton from '@material-ui/core/IconButton';
import AccountCircle from '@material-ui/icons/AccountCircle';
import Dialog from '@material-ui/core/Dialog';
import Menu from '@material-ui/core/Menu';
import MenuItem from '@material-ui/core/MenuItem';
import Login from './../Login';
import Registration from './../Registration';
import text from './../../services/texts/index';

class AuthActions extends Component {

  constructor(props) {
    super(props);
    this.state = {
      anchorEl: null,
      openLogin: false,
      openRegistration: false
    };
  };

  openMenu = event => {
    this.setState({ anchorEl: event.currentTarget });
  };

  closeMenu = () => {
    this.setState({ anchorEl: null });
  };

  changeState = (stateToChange) => {
    this.setState({
      [stateToChange]: !this.state[stateToChange]
    });
    this.closeMenu();
  };

  render() {
    const {anchorEl} = this.state;
    return (
      <div>
        <IconButton
          color='inherit'
          aria-owns={anchorEl ? 'simple-menu' : null}
          aria-haspopup="true"
          onClick={this.openMenu}
        >
          <AccountCircle />
        </IconButton>
        <Menu
          id="simple-menu"
          anchorEl={anchorEl}
          open={Boolean(anchorEl)}
          onClose={this.closeMenu}
        >
          <MenuItem onClick={()=>{this.changeState('openLogin')}}>{text.texts.login}</MenuItem>
          <MenuItem onClick={()=>{this.changeState('openRegistration')}}>{text.texts.registration}</MenuItem>
        </Menu>

        <Dialog
          open={this.state.openLogin}
          onClose={()=>{this.changeState('openLogin')}}
          aria-labelledby="form-dialog-title"
        >
          <Login
            changeState={this.changeState}
          />
        </Dialog>
        <Dialog
          open={this.state.openRegistration}
          onClose={()=>{this.changeState('openRegistration')}}
          aria-labelledby="form-dialog-title"
        >
          <Registration
            changeState={this.changeState}
          />
        </Dialog>
      </div>
    );
  }
}


export default AuthActions;
