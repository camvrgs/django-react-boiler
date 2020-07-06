/**
 *  +  {{cookiecutter.project_name}}  +
 *
 *  |  JS Module  |  {{cookiecutter.client_project_name}}  |
 *  {{cookiecutter.client_project_slug}}/.
 *  components/.
 *  ReactSpinner.js
 *
 *  Sample Component. Renders a fontawesome code (needs to be imported at
 *  HTML level) of a react icon which spins. On click, sends action to
 *  a seperate click counter through redux.
 *
 *  ~ {{cookiecutter.author}} ~
 **/

import React, { Component } from 'react'
import PropTypes from 'prop-types'

class ReactSpinner extends Component {
  constructor(props) {
    super(props)
    this.handleEvent = this.handleEvent.bind(this)
  }

  handleEvent() {
    this.props.handleEvent()
  }

  render() {
    return (
      <div className={this.props.style}>
        {this.props.showElement
          ? <a className=''
            onClick={this.handleEvent}
            disabled={this.props.elementDisabled}
          >
            <div><i className="fab fa-react fa-2x fa-spin fa-fw"></i></div>
            <div className='under-icon'><p className='heading'>{this.props.elementText}</p></div>
            {this.props.children}
          </a>
          : ''}
      </div>
    )
  }
}

ReactSpinner.propTypes = {
  elementText: PropTypes.string.isRequired,
  showElement: PropTypes.bool,
  elementDisabled: PropTypes.bool,
  style: PropTypes.string,
  children: PropTypes.oneOfType([
    PropTypes.array,
    PropTypes.element,
    PropTypes.string
  ]),

  // pass down methods
  handleEvent: PropTypes.func
}

ReactSpinner.defaultProps = {
  showElement: true,
  elementDisabled: false,
  style: 'react-spinner',
  handleEvent: () => {}
}

export default ReactSpinner
