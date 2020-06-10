import React from 'react'

import { Dropdown } from '@fluentui/react/lib/Dropdown'

const defaultValue = 'selection'

const options = [
  { key: 'selection', text: 'Selection' },
  { key: 'all', text: 'All' },
  { key: 'none', text: 'None' },
]

export default function DrawWhiteSpace (props) {
  return <Dropdown
    label="Draw White Space"
    options={options}
    selectedKey={ props.value || defaultValue }
    onChange={ (_, { key }) => props.callback(key) }
  />
}
