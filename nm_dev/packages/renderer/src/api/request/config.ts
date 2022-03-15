let BASE_URL = ''
const TIME_OUT = 10000

if (process.env.NODE_ENV === 'development') {
  BASE_URL = 'http://127.0.0.1:17173'
} else if (process.env.NODE_ENV === 'production') {
  BASE_URL = 'http://127.0.0.1:17173'
} else {
  BASE_URL = 'http://127.0.0.1:17173'
}

export { BASE_URL, TIME_OUT }
