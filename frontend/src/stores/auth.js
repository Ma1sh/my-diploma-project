import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import api from '@/services/api'

export const useAuthStore = defineStore('auth', () => {
  const user = ref(null)
  const accessToken = ref(localStorage.getItem('access_token'))
  const refreshToken = ref(localStorage.getItem('refresh_token'))

  const isAuthenticated = computed(() => !!accessToken.value)

  const login = async (credentials) => {
    try {
      const response = await api.post('/auth/jwt/create/', credentials)
      accessToken.value = response.data.access
      refreshToken.value = response.data.refresh
      
      localStorage.setItem('access_token', response.data.access)
      localStorage.setItem('refresh_token', response.data.refresh)
      
      await fetchUser()
      return true
    } catch (error) {
      console.error('Login error:', error)
      throw error
    }
  }

  const register = async (userData) => {
    try {
      await api.post('/auth/users/', userData)
      return true
    } catch (error) {
      console.error('Registration error:', error)
      throw error
    }
  }

  const logout = () => {
    user.value = null
    accessToken.value = null
    refreshToken.value = null
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
  }

  const fetchUser = async () => {
    try {
      const response = await api.get('/auth/users/me/')
      user.value = response.data
    } catch (error) {
      console.error('Fetch user error:', error)
      logout()
    }
  }

  const checkAuth = async () => {
    if (accessToken.value) {
      await fetchUser()
    }
  }

  const updateProfile = async (userData) => {
    try {
      const response = await api.patch('/auth/users/me/', userData)
      user.value = response.data
      return true
    } catch (error) {
      console.error('Update profile error:', error)
      throw error
    }
  }

  return {
    user,
    isAuthenticated,
    login,
    register,
    logout,
    fetchUser,
    checkAuth,
    updateProfile
  }
})