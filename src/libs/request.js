export default function request (url, data) {
  return new Promise((resolve, reject) => {
    if (PRODUCTION) {
      fetch(url, {
        method: 'POST',
        body: data ? JSON.stringify(data) : null
      }).then(
        r => resolve(r.json()),
        err => reject(err)
      )
    } else {
      const mockData = require('../mocks')[url]
      if (mockData) {
        resolve(mockData)
      } else {
        reject(`mock data not found [${url}]`)
      }
    }
  })
}
