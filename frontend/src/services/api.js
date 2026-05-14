import axios from 'axios'
import { useToast } from 'vue-toastification'

const toast = useToast()

const api = axios.create({
  baseURL: '/api',
  headers: {
    'Content-Type': 'application/json'
  }
})

// Request interceptor
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('access_token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// Response interceptor
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config

    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true

      try {
        const refreshToken = localStorage.getItem('refresh_token')
        const response = await axios.post('/api/auth/jwt/refresh/', {
          refresh: refreshToken
        })

        const { access } = response.data
        localStorage.setItem('access_token', access)

        originalRequest.headers.Authorization = `Bearer ${access}`
        return api(originalRequest)
      } catch (error) {
        localStorage.removeItem('access_token')
        localStorage.removeItem('refresh_token')
        window.location.href = '/login'
        return Promise.reject(error)
      }
    }

    // Show error toast
    if (error.response?.data?.detail) {
      toast.error(error.response.data.detail)
    } else if (error.response?.data) {
      const errors = Object.values(error.response.data).flat()
      errors.forEach(err => toast.error(err))
    } else {
      toast.error('Произошла ошибка. Попробуйте позже.')
    }

    return Promise.reject(error)
  }
)

export default api