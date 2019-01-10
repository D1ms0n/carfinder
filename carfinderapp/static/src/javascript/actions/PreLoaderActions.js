import { TOOGLE_PRELOADER } from '../constants/Preloader'

export function togglePreLoader(result) {

  return {
    type: TOOGLE_PRELOADER,
    payload: result
  }

}