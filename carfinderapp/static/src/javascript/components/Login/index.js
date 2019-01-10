import React, {Component} from 'react';
import {withStyles} from '@material-ui/core/styles/index';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogTitle from '@material-ui/core/DialogTitle';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import text from './../../services/texts/index';

const styles = (theme) => ({
  root: {
    flexGrow: 1
  }
});

class Login extends Component {
  constructor(props) {
    super(props);
  }
  render(){
    return (
      <div>
        <DialogTitle id="form-dialog-title">
          Login
        </DialogTitle>
        <DialogContent>
          <TextField
            autoFocus
            margin="dense"
            id="email"
            label="Email Address"
            type="email"
            fullWidth
          />
          <TextField
            margin="dense"
            id="password"
            label="Password"
            type="password"
            fullWidth
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={()=>{this.props.changeState('openLogin')}} color="primary">
            {text.texts.cancel}
          </Button>
          <Button onClick={()=>{this.props.changeState('openLogin')}} color="primary">
            {text.texts.submit}
          </Button>
        </DialogActions>
      </div>
    )
  }
}

export default withStyles(styles)(Login);
