import { combineReducers } from 'redux';
import helpers from './helpers';
import errors from './errors'
import messages from './messages'
import auth from './auth'
import institutions from './institutions'

export default combineReducers({
    helpers,
    errors,
    messages,
    institutions,
    auth    
});