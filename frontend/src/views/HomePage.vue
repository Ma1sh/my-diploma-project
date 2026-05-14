<template>
  <div class="home-page">
    <!-- Hero Section -->
    <section class="hero">
      <div class="container">
        <div class="hero-content">
          <div class="hero-text">
            <h1 class="hero-title">
              Профессиональный ремонт<br>
              <span class="highlight-text">компьютерной техники</span>
            </h1>
            <p class="hero-description">
              Качественный сервис, доступные цены и гарантия на все виды работ.
              Более 10 лет опыта в сфере IT-услуг.
            </p>
            <div class="hero-buttons">
              <router-link to="/orders/create" class="btn btn-primary btn-large">
                Оставить заявку
              </router-link>
              <router-link to="/services" class="btn btn-outline-white btn-large">
                Наши услуги
              </router-link>
            </div>
            
            <div class="hero-features">
              <div class="feature-item">
                <span class="feature-icon">✓</span>
                <span>Гарантия качества</span>
              </div>
              <div class="feature-item">
                <span class="feature-icon">✓</span>
                <span>Быстрый ремонт</span>
              </div>
              <div class="feature-item">
                <span class="feature-icon">✓</span>
                <span>Доступные цены</span>
              </div>
            </div>
          </div>
          
          <div class="hero-image">
            <div class="image-placeholder">
              <div class="tech-icon">💻</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Popular Services -->
    <section class="popular-services">
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">Популярные услуги</h2>
          <router-link to="/services" class="view-all-link">
            Все услуги →
          </router-link>
        </div>

        <div class="services-grid" v-if="popularServices.length">
          <div 
            v-for="service in popularServices" 
            :key="service.id" 
            class="service-card"
            @click="goToService(service.id)"
          >
            <div class="service-image">
              <img 
                v-if="service.image" 
                :src="service.image" 
                :alt="service.name"
              >
              <div v-else class="service-placeholder">🔧</div>
            </div>
            <div class="service-info">
              <h3 class="service-name">{{ service.name }}</h3>
              <p class="service-price">от {{ service.price_from }} ₽</p>
              <p class="service-duration">⏱ {{ service.duration }}</p>
            </div>
          </div>
        </div>

        <div v-else class="loading">
          Загрузка услуг...
        </div>
      </div>
    </section>

    <!-- Advantages -->
    <section class="advantages">
      <div class="container">
        <h2 class="section-title">Почему выбирают нас</h2>
        
        <div class="advantages-grid">
          <div class="advantage-card">
            <div class="advantage-icon">🎯</div>
            <h3>Профессионализм</h3>
            <p>Квалифицированные специалисты с многолетним опытом работы</p>
          </div>
          
          <div class="advantage-card">
            <div class="advantage-icon">⚡</div>
            <h3>Оперативность</h3>
            <p>Быстрая диагностика и ремонт в кратчайшие сроки</p>
          </div>
          
          <div class="advantage-card">
            <div class="advantage-icon">💰</div>
            <h3>Выгодные цены</h3>
            <p>Конкурентные цены и регулярные акции для клиентов</p>
          </div>
          
          <div class="advantage-card">
            <div class="advantage-icon">🛡️</div>
            <h3>Гарантия</h3>
            <p>Официальная гарантия на все виды выполненных работ</p>
          </div>
          
          <div class="advantage-card">
            <div class="advantage-icon">🔧</div>
            <h3>Качество</h3>
            <p>Используем только оригинальные запчасти и комплектующие</p>
          </div>
          
          <div class="advantage-card">
            <div class="advantage-icon">📱</div>
            <h3>Удобство</h3>
            <p>Онлайн запись и отслеживание статуса заказа</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Reviews -->
    <section class="reviews" v-if="featuredReviews.length">
      <div class="container">
        <h2 class="section-title">Отзывы наших клиентов</h2>
        
        <div class="reviews-grid">
          <div 
            v-for="review in featuredReviews" 
            :key="review.id" 
            class="review-card"
          >
            <div class="review-header">
              <div class="review-avatar">
                {{ getInitials(review.user_name) }}
              </div>
              <div class="review-author">
                <h4>{{ review.user_name }}</h4>
                <div class="review-rating">
                  <span v-for="star in 5" :key="star" class="star">
                    {{ star <= review.rating ? '★' : '☆' }}
                  </span>
                </div>
              </div>
            </div>
            <p class="review-text">{{ review.text }}</p>
            <span class="review-date">{{ formatDate(review.created_at) }}</span>
          </div>
        </div>

        <div class="reviews-footer">
          <router-link to="/reviews" class="btn btn-outline">
            Все отзывы
          </router-link>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="cta-section">
      <div class="container">
        <div class="cta-content">
          <h2 class="cta-title">Готовы начать?</h2>
          <p class="cta-description">
            Оставьте заявку прямо сейчас и получите бесплатную диагностику
          </p>
          <router-link to="/orders/create" class="btn btn-primary btn-large">
            Оставить заявку
          </router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { useToast } from 'vue-toastification'

const router = useRouter()
const toast = useToast()

const popularServices = ref([])
const featuredReviews = ref([])

const loadPopularServices = async () => {
  try {
    const response = await axios.get('/api/services/', { params: { is_popular: true } })
    popularServices.value = response.data.results.slice(0, 6)
  } catch (error) {
    console.error('Error loading services:', error)
  }
}

const loadFeaturedReviews = async () => {
  try {
    const response = await axios.get('/api/reviews/featured/')
    featuredReviews.value = response.data.slice(0, 3)
  } catch (error) {
    console.error('Error loading reviews:', error)
  }
}

const goToService = (id) => {
  router.push(`/services/${id}`)
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
  loadPopularServices()
  loadFeaturedReviews()
})
</script>

<style scoped>
.home-page {
  min-height: 100vh;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

/* Hero Section */
.hero {
  padding: 80px 0;
  background: #2b6cb0;
  color: white;
  position: relative;
  overflow: hidden;
}

.hero::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: url('data:image/svg+xml,<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="40" fill="rgba(255,255,255,0.05)"/></svg>');
  opacity: 0.1;
}

.hero-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
  align-items: center;
  position: relative;
  z-index: 1;
}

.hero-title {
  font-size: 48px;
  font-weight: 700;
  margin-bottom: 20px;
  line-height: 1.2;
}

.highlight-text {
  color: #fbbf24;
}

.hero-description {
  font-size: 18px;
  line-height: 1.6;
  margin-bottom: 30px;
  opacity: 0.95;
}

.hero-buttons {
  display: flex;
  gap: 15px;
  margin-bottom: 40px;
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
}

.btn-large {
  padding: 16px 40px;
  font-size: 18px;
}

.btn-primary {
  background: #fbbf24;
  color: #1a202c;
  box-shadow: 0 4px 20px rgba(251, 191, 36, 0.3);
}

.btn-primary:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 25px rgba(251, 191, 36, 0.4);
  background: #f59e0b;
}

.btn-outline-white {
  background: transparent;
  color: white;
  border: 2px solid white;
}

.btn-outline-white:hover {
  background: white;
  color: #2b6cb0;
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

.hero-features {
  display: flex;
  gap: 30px;
  flex-wrap: wrap;
}

.feature-item {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 16px;
}

.feature-icon {
  width: 24px;
  height: 24px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
}

.hero-image {
  display: flex;
  align-items: center;
  justify-content: center;
}

.image-placeholder {
  width: 400px;
  height: 400px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  backdrop-filter: blur(10px);
  border: 2px solid rgba(255, 255, 255, 0.2);
}

.tech-icon {
  font-size: 150px;
}

/* Sections */
section {
  padding: 80px 0;
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 40px;
}

.section-title {
  font-size: 36px;
  font-weight: 700;
  color: #1a202c;
}

.view-all-link {
  color: #2b6cb0;
  text-decoration: none;
  font-weight: 600;
  font-size: 16px;
  transition: color 0.3s ease;
}

.view-all-link:hover {
  color: #2c5282;
}

/* Services Grid */
.services-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 30px;
}

.service-card {
  background: white;
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
  cursor: pointer;
}

.service-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
}

.service-image {
  width: 100%;
  height: 200px;
  background: #2b6cb0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.service-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.service-placeholder {
  font-size: 80px;
}

.service-info {
  padding: 20px;
}

.service-name {
  font-size: 20px;
  font-weight: 600;
  color: #1a202c;
  margin-bottom: 10px;
}

.service-price {
  font-size: 24px;
  font-weight: 700;
  color: #2b6cb0;
  margin-bottom: 8px;
}

.service-duration {
  color: #718096;
  font-size: 14px;
}

/* Advantages */
.advantages {
  background: #f7fafc;
}

.advantages-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
  margin-top: 40px;
}

.advantage-card {
  background: white;
  padding: 40px;
  border-radius: 15px;
  text-align: center;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
  transition: all 0.3s ease;
}

.advantage-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.1);
}

.advantage-icon {
  font-size: 60px;
  margin-bottom: 20px;
}

.advantage-card h3 {
  font-size: 22px;
  font-weight: 600;
  color: #1a202c;
  margin-bottom: 15px;
}

.advantage-card p {
  color: #718096;
  line-height: 1.6;
}

/* Reviews */
.reviews-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 30px;
  margin-top: 40px;
}

.review-card {
  background: white;
  padding: 30px;
  border-radius: 15px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
}

.review-card:hover {
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
}

.review-header {
  display: flex;
  gap: 15px;
  margin-bottom: 20px;
}

.review-avatar {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background: #2b6cb0;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 18px;
  flex-shrink: 0;
}

.review-author h4 {
  font-size: 18px;
  font-weight: 600;
  color: #1a202c;
  margin-bottom: 5px;
}

.review-rating {
  color: #fbbf24;
  font-size: 18px;
}

.review-text {
  color: #4a5568;
  line-height: 1.6;
  margin-bottom: 15px;
}

.review-date {
  font-size: 14px;
  color: #a0aec0;
}

.reviews-footer {
  text-align: center;
  margin-top: 40px;
}

/* CTA Section */
.cta-section {
  background: #2b6cb0;
  color: white;
}

.cta-content {
  text-align: center;
  max-width: 700px;
  margin: 0 auto;
}

.cta-title {
  font-size: 42px;
  font-weight: 700;
  margin-bottom: 20px;
}

.cta-description {
  font-size: 20px;
  margin-bottom: 30px;
  opacity: 0.95;
}

.loading {
  text-align: center;
  padding: 40px;
  color: #718096;
  font-size: 18px;
}

/* Responsive */
@media (max-width: 968px) {
  .hero-content {
    grid-template-columns: 1fr;
    text-align: center;
  }

  .hero-title {
    font-size: 36px;
  }

  .hero-buttons {
    justify-content: center;
  }

  .hero-features {
    justify-content: center;
  }

  .image-placeholder {
    width: 300px;
    height: 300px;
  }

  .tech-icon {
    font-size: 100px;
  }

  .section-title {
    font-size: 28px;
  }

  .section-header {
    flex-direction: column;
    gap: 20px;
  }
}

@media (max-width: 640px) {
  .hero-title {
    font-size: 28px;
  }

  .hero-description {
    font-size: 16px;
  }

  .hero-buttons {
    flex-direction: column;
  }

  .btn-large {
    width: 100%;
  }

  .services-grid,
  .advantages-grid,
  .reviews-grid {
    grid-template-columns: 1fr;
  }

  .cta-title {
    font-size: 32px;
  }

  .cta-description {
    font-size: 18px;
  }
}
</style>