import React from 'react'

import request from '@libs/request'

import { Text } from '@fluentui/react/lib/Text'
import { Stack } from '@fluentui/react/lib/Stack'

import defaultSettings from './settings/defaultSettings'
import FontSize from './settings/FontSize'
import DrawWhiteSpace from './settings/DrawWhiteSpace'
import CaretStyle from './settings/CaretStyle'
import DefaultLineEnding from './settings/DefaultLineEnding'
import HighlightLine from './settings/HighlightLine'

export default class Settings extends React.Component {
  constructor (props) {
    super(props)
    this.state = defaultSettings
    this.loadSettings()
  }

  loadSettings () {
    request('/api/sublime/settings').then(res => {
      if (res.error === 0) {
        this.setState(res.data)
      } else {
        alert(res.message)
      }
    })
  }

  changeSetting (key, value) {
    this.setState({ [key]: value })
    request('/api/sublime/settings', {
      [key]: value
    }).then(res => {
      console.group(`changeSetting: ${key}`)
      console.log({ [key]: value })
      console.log(res)
      console.groupEnd(`changeSetting: ${key}`)
    })
  }

  render () {
    return (
      <main>
        <Text variant="xxLarge" nowrap block>Settings</Text>
        <Stack tokens={{ childrenGap: 10 }} styles={{ root: { width: 250, marginTop: 20 }}}>
          <FontSize
            value={ this.state.font_size }
            callback={ value => this.changeSetting('font_size', value) }
          />
          <CaretStyle
            value={ this.state.caret_style }
            callback={ value => this.changeSetting('caret_style', value) }
          />
          <DrawWhiteSpace
            value={ this.state.draw_white_space }
            callback={ value => this.changeSetting('draw_white_space', value) }
          />
          <DefaultLineEnding
            value={ this.state.default_line_ending }
            callback={ value => this.changeSetting('default_line_ending', value) }
          />
          <HighlightLine
            value={ this.state.highlight_line }
            callback={ value => this.changeSetting('highlight_line', value) }
          />
        </Stack>
      </main>
    )
  }
}
