import React from 'react'

import '@styles/sidebar.css'

export default function Sidebar (props) {
  return (
    <nav className="sd-sidebar">
      <ul>
        {
          props.list && props.list.map((item, idx) =>
            <li
              className={props.current === idx ? 'active' : ''}
              key={item.title}
              onClick={e => props.update(idx)}
            >
              {item.title}
            </li>
          )
        }
      </ul>
    </nav>
  )
}
