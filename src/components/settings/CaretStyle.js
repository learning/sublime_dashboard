import React from 'react'

import { Dropdown } from '@fluentui/react/lib/Dropdown'

const defaultValue = 'smooth'

const options = [
  { key: 'smooth', text: 'Smooth' },
  { key: 'phase', text: 'Phase' },
  { key: 'blink', text: 'Blink' },
  { key: 'solid', text: 'Solid' }
]

export default function CaretStyle (props) {
  return <Dropdown
    label="Caret Style"
    options={options}
    selectedKey={ props.value || defaultValue }
    onChange={ (_, { key }) => props.callback(key) }
  />
}
