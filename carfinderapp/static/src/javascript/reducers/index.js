import {combineReducers} from 'redux';
import form from './form.js';
import loading from './preloader.js';

export default combineReducers({
  form,
  loading
})