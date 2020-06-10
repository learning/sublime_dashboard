import React from 'react'

import { Slider } from '@fluentui/react/lib/Slider'

const defaultValue = 10

const max = 48
const min = 8

export default function FontSize (props) {
  let value = props.value
  if (value !== 0 && !value) {
    value = defaultValue
  }

  return <Slider
    label="Font Size"
    value={value}
    min={min}
    max={max}
    step={1}
    onChange={ value => props.callback(value) }
  />
}
