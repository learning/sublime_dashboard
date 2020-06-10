import React from 'react'

import Sidebar from '@components/Sidebar'
import Settings from '@components/Settings'
import About from '@components/About'

import { initializeIcons } from '@uifabric/icons';

import '@styles/app.css'
import '@styles/main.css'

const pageList = [{
  title: 'Settings',
  component: Settings
}, {
  title: 'About',
  component: About
}]

initializeIcons();

export default class App extends React.Component {
  constructor () {
    super()
    this.state = {
      currentPage: 0
    }
  }

  render () {
    const CurrentComponent = pageList[this.state.currentPage].component
    return (
      <div id="app">
        <Sidebar
          list={pageList}
          update={ currentPage => this.setState({ currentPage })}
          current={ this.state.currentPage }
        />
        <CurrentComponent/>
      </div>
    )
  }
}
