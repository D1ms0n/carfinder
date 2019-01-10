import { SUBMIT_FORM } from '../constants/Form'

export function submitForm(result) {

  return {
    type: SUBMIT_FORM,
    payload: result
  }

}