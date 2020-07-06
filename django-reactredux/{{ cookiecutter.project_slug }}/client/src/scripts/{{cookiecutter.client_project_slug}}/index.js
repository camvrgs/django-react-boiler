/**
 *  +  {{cookiecutter.project_name}}  +
 *
 *  |  JS Module  |  {{cookiecutter.client_project_name}}  |
 *  {{cookiecutter.client_project_slug}}/.
 *  index.js
 *
 *  React project entry, renders main React component and
 *  attaches the Redux Store to it
 *
 *  ~ {{cookiecutter.author}} ~
 **/

import React from 'react'
import ReactDOM from 'react-dom'
import { Provider } from 'react-redux'

import App from './containers/App'

import store from './store'

ReactDOM.render(
  <Provider store={store}>
    <div className='{{cookiecutter.client_project_slug}}-app'>
      <App />
    </div>
  </Provider>
  , document.querySelector('.mount')
)
