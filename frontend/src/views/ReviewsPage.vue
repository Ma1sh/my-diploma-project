<template>
  <div class="reviews-page">
    <div class="page-header">
      <div class="container">
        <h1 class="page-title">Отзывы клиентов</h1>
        <p class="page-description">Мнения наших клиентов о качестве работы</p>
      </div>
    </div>

    <div class="container">
      <div class="reviews-stats">
        <div class="stat-card">
          <div class="stat-number">{{ totalReviews }}</div>
          <div class="stat-label">Всего отзывов</div>
        </div>
        <div class="stat-card">
          <div class="stat-number">{{ averageRating.toFixed(1) }}</div>
          <div class="stat-label">Средняя оценка</div>
          <div class="rating-stars">
            <span v-for="star in 5" :key="star" class="star">
              {{ star <= Math.round(averageRating) ? '★' : '☆' }}
            </span>
          </div>
        </div>
        <div class="stat-card">
          <div class="stat-number">98%</div>
          <div class="stat-label">Довольных клиентов</div>
        </div>
      </div>

      <div class="reviews-actions">
        <button 
          v-if="authStore.isAuthenticated"
          @click="showReviewModal = true"
          class="btn btn-primary"
        >
          + Оставить отзыв
        </button>
        <router-link 
          v-else
          to="/login"
          class="btn btn-primary"
        >
          Войдите, чтобы оставить отзыв
        </router-link>
      </div>

      <div class="filter-bar">
        <button 
          v-for="rating in [0, 5, 4, 3]" 
          :key="rating"
          class="filter-btn"
          :class="{ active: filters.rating === rating }"
          @click="filterByRating(rating)"
        >
          <template v-if="rating === 0">Все отзывы</template>
          <template v-else>{{ rating }} ★</template>
        </button>
      </div>

      <div v-if="loading" class="loading">
        <div class="spinner"></div>
        <p>Загрузка отзывов...</p>
      </div>

      <div v-else-if="reviews.length" class="reviews-grid">
        <div 
          v-for="review in reviews" 
          :key="review.id"
          class="review-card"
        >
          <div class="review-header">
            <div class="review-author-info">
              <div class="author-avatar">
                {{ getInitials(review.user_name) }}
              </div>
              <div class="author-details">
                <h3 class="author-name">{{ review.user_name }}</h3>
                <div class="review-rating">
                  <span v-for="star in 5" :key="star" class="star">
                    {{ star <= review.rating ? '★' : '☆' }}
                  </span>
                </div>
              </div>
            </div>
            <span class="review-date">{{ formatDate(review.created_at) }}</span>
          </div>
          
          <p class="review-text">{{ review.text }}</p>
          
          <div v-if="review.is_featured" class="featured-badge">
            ⭐ Рекомендуемый отзыв
          </div>
        </div>
      </div>

      <div v-else class="no-reviews">
        <div class="no-reviews-icon">💬</div>
        <h3>Отзывов пока нет</h3>
        <p>Станьте первым, кто оставит отзыв!</p>
      </div>
    </div>

    <!-- Review Modal -->
    <div v-if="showReviewModal" class="modal-overlay" @click="closeModal">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <h2>Оставить отзыв</h2>
          <button class="modal-close" @click="closeModal">✕</button>
        </div>
        
        <form @submit.prevent="handleSubmitReview" class="review-form">
          <div class="form-group">
            <label class="form-label">Оценка *</label>
            <div class="rating-input">
              <button 
                v-for="star in 5" 
                :key="star"
                type="button"
                class="star-btn"
                :class="{ active: star <= reviewForm.rating }"
                @click="reviewForm.rating = star"
              >
                {{ star <= reviewForm.rating ? '★' : '☆' }}
              </button>
            </div>
          </div>

          <div class="form-group">
            <label class="form-label">Ваш отзыв *</label>
            <textarea 
              v-model="reviewForm.text"
              class="form-control"
              rows="6"
              placeholder="Расскажите о вашем опыте работы с нами..."
              required
            ></textarea>
          </div>

          <div class="modal-actions">
            <button 
              type="submit" 
              class="btn btn-primary"
              :disabled="submitting || reviewForm.rating === 0"
            >
              <span v-if="submitting">Отправка...</span>
              <span v-else>Отправить отзыв</span>
            </button>
            <button type="button" class="btn btn-outline" @click="closeModal">
              Отмена
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useAuthStore } from '@/stores/auth'
import reviewsApi from '@/services/reviewsApi'
import { useToast } from 'vue-toastification'

const authStore = useAuthStore()
const toast = useToast()

const reviews = ref([])
const loading = ref(false)
const showReviewModal = ref(false)
const submitting = ref(false)

const filters = ref({
  rating: 0
})

const reviewForm = ref({
  rating: 0,
  text: ''
})

const totalReviews = computed(() => reviews.value.length)
const averageRating = computed(() => {
  if (reviews.value.length === 0) return 0
  const sum = reviews.value.reduce((acc, review) => acc + review.rating, 0)
  return sum / reviews.value.length
})

const loadReviews = async () => {
  loading.value = true
  try {
    const params = {}
    if (filters.value.rating > 0) {
      params.rating = filters.value.rating
    }
    
    const response = await reviewsApi.getReviews(params)
    reviews.value = response.data.results
  } catch (error) {
    console.error('Error loading reviews:', error)
  } finally {
    loading.value = false
  }
}

const filterByRating = (rating) => {
  filters.value.rating = rating
  loadReviews()
}

const handleSubmitReview = async () => {
  submitting.value = true
  try {
    await reviewsApi.createReview(reviewForm.value)
    toast.success('Спасибо за отзыв! Он появится после модерации.')
    closeModal()
    reviewForm.value = { rating: 0, text: '' }
    loadReviews()
  } catch (error) {
    console.error('Error submitting review:', error)
    toast.error('Ошибка отправки отзыва')
  } finally {
    submitting.value = false
  }
}

const closeModal = () => {
  showReviewModal.value = false
}

const getInitials = (name) => {
  return name
    .split(' ')
    .map(word => word[0])
    .join('')
    .toUpperCase()
    .slice(0, 2)
}

const formatDate = (dateString) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', {
    day: 'numeric',
    month: 'long',
    year: 'numeric'
  })
}

onMounted(() => {
  loadReviews()
})
</script>

<style scoped>
.page-header {
  background: #2b6cb0;
  color: white;
  padding: 60px 0;
  margin-bottom: 60px;
  text-align: center;
}

.page-title {
  font-size: 48px;
  font-weight: 700;
  margin-bottom: 15px;
}

.page-description {
  font-size: 18px;
  opacity: 0.95;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  margin-bottom: 80px;
}

.reviews-stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 30px;
  margin-bottom: 40px;
}

.stat-card {
  background: white;
  padding: 30px;
  border-radius: 15px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  text-align: center;
}

.stat-number {
  font-size: 48px;
  font-weight: 700;
  color: #2b6cb0;
  margin-bottom: 10px;
}

.stat-label {
  color: #718096;
  font-size: 16px;
  margin-bottom: 10px;
}

.rating-stars {
  color: #fbbf24;
  font-size: 24px;
}

.reviews-actions {
  text-align: center;
  margin-bottom: 40px;
}

.filter-bar {
  display: flex;
  gap: 10px;
  margin-bottom: 40px;
  justify-content: center;
  flex-wrap: wrap;
}

.filter-btn {
  padding: 12px 24px;
  background: white;
  border: 2px solid #e2e8f0;
  border-radius: 10px;
  cursor: pointer;
  font-weight: 600;
  color: #4a5568;
  transition: all 0.3s;
}

.filter-btn:hover {
  border-color: #2b6cb0;
  color: #2b6cb0;
}

.filter-btn.active {
  background: #2b6cb0;
  color: white;
  border-color: transparent;
}

.reviews-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
  gap: 30px;
}

.review-card {
  background: white;
  padding: 30px;
  border-radius: 15px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
  position: relative;
}

.review-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
}

.review-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 20px;
}

.review-author-info {
  display: flex;
  gap: 15px;
}

.author-avatar {
  width: 50px;
  height: 50px;
  background: #2b6cb0;
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 18px;
  flex-shrink: 0;
}

.author-details {
  flex: 1;
}

.author-name {
  font-size: 18px;
  font-weight: 600;
  color: #1a202c;
  margin-bottom: 5px;
}

.review-rating {
  color: #fbbf24;
  font-size: 18px;
}

.star {
  margin-right: 2px;
}

.review-date {
  font-size: 14px;
  color: #a0aec0;
}

.review-text {
  color: #4a5568;
  line-height: 1.7;
  margin-bottom: 15px;
}

.featured-badge {
  display: inline-block;
  background: #fef3c7;
  color: #92400e;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
}

.loading {
  text-align: center;
  padding: 80px 20px;
}

.spinner {
  width: 50px;
  height: 50px;
  border: 4px solid #e2e8f0;
  border-top-color: #667eea;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 20px;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.no-reviews {
  text-align: center;
  padding: 80px 20px;
}

.no-reviews-icon {
  font-size: 100px;
  margin-bottom: 20px;
}

.no-reviews h3 {
  font-size: 28px;
  color: #1a202c;
  margin-bottom: 10px;
}

.no-reviews p {
  color: #718096;
  font-size: 16px;
}

/* Modal */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 20px;
}

.modal-content {
  background: white;
  border-radius: 20px;
  max-width: 600px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 30px;
  border-bottom: 2px solid #f7fafc;
}

.modal-header h2 {
  font-size: 28px;
  font-weight: 700;
  color: #1a202c;
}

.modal-close {
  background: none;
  border: none;
  font-size: 28px;
  cursor: pointer;
  color: #718096;
  padding: 5px;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 8px;
  transition: all 0.3s;
}

.modal-close:hover {
  background: #f7fafc;
  color: #1a202c;
}

.review-form {
  padding: 30px;
}

.form-group {
  margin-bottom: 25px;
}

.form-label {
  display: block;
  font-weight: 600;
  color: #2d3748;
  margin-bottom: 10px;
  font-size: 15px;
}

.rating-input {
  display: flex;
  gap: 10px;
}

.star-btn {
  background: none;
  border: none;
  font-size: 36px;
  cursor: pointer;
  color: #e2e8f0;
  transition: all 0.3s;
}

.star-btn:hover,
.star-btn.active {
  color: #fbbf24;
  transform: scale(1.1);
}

.form-control {
  width: 100%;
  padding: 14px 16px;
  border: 2px solid #e2e8f0;
  border-radius: 10px;
  font-size: 15px;
  transition: all 0.3s;
  font-family: inherit;
  resize: vertical;
}

.form-control:focus {
  outline: none;
  border-color: #2b6cb0;
  box-shadow: 0 0 0 3px rgba(43, 108, 176, 0.1);
}

.modal-actions {
  display: flex;
  gap: 15px;
}

.btn {
  padding: 14px 32px;
  border-radius: 10px;
  font-weight: 600;
  text-decoration: none;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 16px;
  display: inline-block;
  text-align: center;
  flex: 1;
}

.btn-primary {
  background: #2b6cb0;
  color: white;
  box-shadow: 0 4px 20px rgba(43, 108, 176, 0.3);
}

.btn-primary:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 6px 25px rgba(43, 108, 176, 0.4);
  background: #2c5282;
}

.btn-primary:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.btn-outline {
  background: white;
  color: #2b6cb0;
  border: 2px solid #2b6cb0;
}

.btn-outline:hover {
  background: #2b6cb0;
  color: white;
}

@media (max-width: 968px) {
  .reviews-stats {
    grid-template-columns: 1fr;
  }

  .reviews-grid {
    grid-template-columns: 1fr;
  }

  .page-title {
    font-size: 36px;
  }
}

@media (max-width: 640px) {
  .page-title {
    font-size: 28px;
  }

  .stat-number {
    font-size: 36px;
  }

  .modal-actions {
    flex-direction: column;
  }
}
</style>