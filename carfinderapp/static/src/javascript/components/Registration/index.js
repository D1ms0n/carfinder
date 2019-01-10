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

class Registration extends Component {
  constructor(props) {
    super(props);
  }
  render(){
    return (
      <div>
        <DialogTitle id="form-dialog-title">
          Registration
        </DialogTitle>
        <DialogContent>
          <TextField
            autoFocus
            margin="dense"
            id="text"
            label="Name"
            type="text"
            fullWidth
          />
          <TextField
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
          <TextField
            margin="dense"
            id="rePassword"
            label="Re-Password"
            type="password"
            fullWidth
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={()=>{this.props.changeState('openRegistration')}} color="primary">
            {text.texts.cancel}
          </Button>
          <Button onClick={()=>{this.props.changeState('openRegistration')}} color="primary">
            {text.texts.submit}
          </Button>
        </DialogActions>
      </div>
    )
  }
}

export default withStyles(styles)(Registration);
