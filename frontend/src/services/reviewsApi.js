import api from './api'

export default {
  getReviews(params = {}) {
    return api.get('/reviews/', { params })
  },

  getFeaturedReviews() {
    return api.get('/reviews/featured/')
  },

  createReview(data) {
    return api.post('/reviews/', data)
  }
}