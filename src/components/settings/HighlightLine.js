import React from 'react'

import { Toggle } from '@fluentui/react/lib/Toggle'

const defaultValue = false

export default function HighlightLine (props) {
  return <Toggle
    label="Highlight Line"
    inlineLabel
    onText="On"
    offText="Off"
    checked={ props.value || defaultValue }
    onChange={ (_, checked) => props.callback(checked) }
  />
}
