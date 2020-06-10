import React from 'react'

import { Dropdown } from '@fluentui/react/lib/Dropdown'

const defaultValue = 'system'

const options = [
  { key: 'system', text: 'System' },
  { key: 'windows', text: 'Windows (CRLF)' },
  { key: 'unix', text: 'Unix (LF)' }
]

export default function DefaultLineEnding (props) {
  return <Dropdown
    label="Default Line Ending"
    description="Determines what character(s) are used to terminate each line in new files."
    options={options}
    selectedKey={ props.value || defaultValue }
    onChange={ (_, { key }) => props.callback(key) }
  />
}
