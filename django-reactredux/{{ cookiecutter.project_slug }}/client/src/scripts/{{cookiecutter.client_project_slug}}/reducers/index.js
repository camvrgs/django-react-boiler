/**
 *  +  {{cookiecutter.project_name}}  +
 *
 *  |  JS Module  |  {{cookiecutter.client_project_name}}  |
 *  {{cookiecutter.client_project_slug}}/.
 *  reducers/.
 *  index.js
 *
 *  combines and exports all redux reducers for the app into a rootreducer
 *  to initialize the redux store
 *  https://redux.js.org/basics/reducers
 *
 *  ~ {{cookiecutter.author}} ~
 **/

import { combineReducers } from 'redux'

// * * Import reducers here * * //
import clickCounterReducer from './clickCounter'
// * * End import * * //

const rootReducer = combineReducers({
  // store_variable: importedReducer,
  clicks: clickCounterReducer
})

export default rootReducer
