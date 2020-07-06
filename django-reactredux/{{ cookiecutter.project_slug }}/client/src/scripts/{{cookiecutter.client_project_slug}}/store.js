/**
 *  +  {{cookiecutter.project_name}}  +
 *
 *  |  JS Module  |  {{cookiecutter.client_project_name}}  |
 *  {{cookiecutter.client_project_slug}}/.
 *  store.js
 *
 *  generates a Redux store in a seperate file to be passed down to whichever
 *  containers need it
 *  also makes integration testing easier if using live Redux stores
 *
 *  ~ {{cookiecutter.author}} ~
 **/

import { createStore, applyMiddleware } from 'redux'
import thunk from 'redux-thunk'
// import logger from 'redux-logger'
import rootReducer from './reducers'

const createStoreWithMiddleware = applyMiddleware(thunk)(createStore)
const store = createStoreWithMiddleware(rootReducer)

export default store
