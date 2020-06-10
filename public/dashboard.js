const menu = document.getElementById('menu')
const layout = document.getElementById('layout')
const menuLink = document.getElementById('menuLink')
const button = document.getElementById('button')

function toggleMenu(e) {
  [menu, layout, menuLink].forEach(element => {
    element.classList.toggle('active')
  })
  e.preventDefault()
}

document.addEventListener('click', e => {
  if (e.target.id === menuLink.id) {
    return toggleMenu(e)
  }

  if (~menu.classList.contains('active')) {
    toggleMenu(e)
  }

  switch (e.target.id) {
    case button.id:
      fetch('/api/sublime/settings', {
        method: 'POST',
        body: JSON.stringify({
          foo: 'bar',
          c: 1,
          b: false,
          a: {
            list: [1, 2, 3]
          }
        })
      })
      break
  }
})
