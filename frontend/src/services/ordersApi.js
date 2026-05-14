import api from './api'

export default {
  getOrders(params = {}) {
    return api.get('/orders/', { params })
  },

  getOrder(id) {
    return api.get(`/orders/${id}/`)
  },

  createOrder(data) {
    return api.post('/orders/', data)
  },

  updateOrder(id, data) {
    return api.patch(`/orders/${id}/`, data)
  },

  deleteOrder(id) {
    return api.delete(`/orders/${id}/`)
  }
}