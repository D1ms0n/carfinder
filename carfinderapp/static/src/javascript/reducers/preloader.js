
import { TOOGLE_PRELOADER } from '../constants/Preloader';

const initialState = {
  result: false
};

export default function loading(state = initialState, action) {
  switch (action.type) {
    case TOOGLE_PRELOADER:
      return { ...state, result: action.payload };
    default:
      return state;
  }
}