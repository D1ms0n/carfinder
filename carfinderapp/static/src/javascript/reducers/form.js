import { SUBMIT_FORM } from '../constants/Form';

const initialState = {
  result: []
};

export default function form(state = initialState, action) {
  switch (action.type) {
    case SUBMIT_FORM:
      return { ...state, result: action.payload };
    default:
      return state;
  }
}