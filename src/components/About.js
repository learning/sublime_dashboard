import React from 'react'

import { Text } from '@fluentui/react/lib/Text'
import { Link } from '@fluentui/react/lib/Link'

export default function About (props) {
  return (
    <main>
      <Text variant="xxLarge">Sublime Dashboard</Text>
      <p>
        Github: <Link href="https://github.com/learning/sublime_dashboard">https://github.com/learning/sublime_dashboard</Link>
        <br/>
        Author: <Link href="https://github.com/learning">Learning</Link>
      </p>
    </main>
  )
}
