import api from './api'

export default {
  getCategories() {
    return api.get('/categories/')
  },

  getServices(params = {}) {
    return api.get('/services/', { params })
  },

  getService(id) {
    return api.get(`/services/${id}/`)
  },

  getPopularServices() {
    return api.get('/services/', { params: { is_popular: true } })
  }
}