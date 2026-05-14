<template>
  <div class="service-detail-page" v-if="service">
    <div class="page-header">
      <div class="container">
        <nav class="breadcrumbs">
          <router-link to="/">Главная</router-link>
          <span>/</span>
          <router-link to="/services">Услуги</router-link>
          <span>/</span>
          <span>{{ service.name }}</span>
        </nav>
      </div>
    </div>

    <div class="container">
      <div class="service-content">
        <div class="service-main">
          <div class="service-image-block">
            <img 
              v-if="service.image" 
              :src="service.image" 
              :alt="service.name"
              class="service-image"
            >
            <div v-else class="service-placeholder">🔧</div>
          </div>

          <div class="service-info-block">
            <div class="service-category-badge">
              {{ service.category_name }}
            </div>
            
            <h1 class="service-title">{{ service.name }}</h1>
            
            <div class="service-meta">
              <div class="meta-item">
                <span class="meta-icon">💰</span>
                <div>
                  <div class="meta-label">Стоимость</div>
                  <div class="meta-value">от {{ service.price_from }} ₽</div>
                </div>
              </div>
              <div class="meta-item">
                <span class="meta-icon">⏱</span>
                <div>
                  <div class="meta-label">Срок выполнения</div>
                  <div class="meta-value">{{ service.duration }}</div>
                </div>
              </div>
            </div>

            <div class="service-description">
              <h2>Описание услуги</h2>
              <p>{{ service.description }}</p>
            </div>

            <div class="service-actions">
              <router-link 
                v-if="authStore.isAuthenticated"
                :to="`/orders/create?service=${service.id}`" 
                class="btn btn-primary btn-large"
              >
                Заказать услугу
              </router-link>
              <router-link 
                v-else
                to="/login" 
                class="btn btn-primary btn-large"
              >
                Войдите для заказа
              </router-link>
              <a href="tel:+79001234567" class="btn btn-outline btn-large">
                📞 Позвонить
              </a>
            </div>
          </div>
        </div>

        <div class="related-services" v-if="relatedServices.length">
          <h2>Похожие услуги</h2>
          <div class="services-grid">
            <div 
              v-for="relService in relatedServices" 
              :key="relService.id"
              class="service-card"
              @click="goToService(relService.id)"
            >
              <div class="service-image-small">
                <img 
                  v-if="relService.image" 
                  :src="relService.image" 
                  :alt="relService.name"
                >
                <div v-else class="service-placeholder-small">🔧</div>
              </div>
              <div class="service-info">
                <h3>{{ relService.name }}</h3>
                <p class="service-price">от {{ relService.price_from }} ₽</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div v-else class="loading-page">
    <div class="spinner"></div>
    <p>Загрузка...</p>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import servicesApi from '@/services/servicesApi'
import { useToast } from 'vue-toastification'

const route = useRoute()
const router = useRouter()
const authStore = useAuthStore()
const toast = useToast()

const service = ref(null)
const relatedServices = ref([])

const loadService = async () => {
  try {
    const response = await servicesApi.getService(route.params.id)
    service.value = response.data
    loadRelatedServices()
  } catch (error) {
    console.error('Error loading service:', error)
    toast.error('Услуга не найдена')
    router.push('/services')
  }
}

const loadRelatedServices = async () => {
  if (!service.value) return
  
  try {
    const response = await servicesApi.getServices({
      category: service.value.category,
      page_size: 4
    })
    relatedServices.value = response.data.results
      .filter(s => s.id !== service.value.id)
      .slice(0, 3)
  } catch (error) {
    console.error('Error loading related services:', error)
  }
}

const goToService = (id) => {
  router.push(`/services/${id}`)
}

watch(() => route.params.id, () => {
  if (route.params.id) {
    loadService()
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }
})

onMounted(() => {
  loadService()
})
</script>

<style scoped>
.page-header {
  background: #f7fafc;
  padding: 20px 0;
  margin-bottom: 40px;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.breadcrumbs {
  display: flex;
  gap: 10px;
  align-items: center;
  color: #718096;
  font-size: 14px;
}

.breadcrumbs a {
  color: #667eea;
  text-decoration: none;
  transition: color 0.3s;
}

.breadcrumbs a:hover {
  color: #764ba2;
}

.service-content {
  margin-bottom: 80px;
}

.service-main {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
  margin-bottom: 80px;
}

.service-image-block {
  position: sticky;
  top: 100px;
  height: fit-content;
}

.service-image {
  width: 100%;
  border-radius: 20px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
}

.service-placeholder {
  width: 100%;
  aspect-ratio: 1;
  background: #2b6cb0;
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 150px;
}

.service-category-badge {
  display: inline-block;
  background: #e2e8f0;
  color: #4a5568;
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 14px;
  font-weight: 600;
  margin-bottom: 20px;
}

.service-title {
  font-size: 42px;
  font-weight: 700;
  color: #1a202c;
  margin-bottom: 30px;
  line-height: 1.2;
}

.service-meta {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  margin-bottom: 40px;
}

.meta-item {
  display: flex;
  gap: 15px;
  padding: 20px;
  background: #f7fafc;
  border-radius: 15px;
}

.meta-icon {
  font-size: 36px;
}

.meta-label {
  font-size: 14px;
  color: #718096;
  margin-bottom: 5px;
}

.meta-value {
  font-size: 20px;
  font-weight: 700;
  color: #1a202c;
}

.service-description {
  margin-bottom: 40px;
}

.service-description h2 {
  font-size: 24px;
  font-weight: 700;
  color: #1a202c;
  margin-bottom: 15px;
}

.service-description p {
  color: #4a5568;
  line-height: 1.8;
  font-size: 16px;
}

.service-actions {
  display: flex;
  gap: 15px;
}

.btn {
  padding: 16px 32px;
  border-radius: 12px;
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
  padding: 18px 40px;
  font-size: 18px;
}

.btn-primary {
  background: #2b6cb0;
  color: white;
  box-shadow: 0 4px 20px rgba(43, 108, 176, 0.3);
}

.btn-primary:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 25px rgba(43, 108, 176, 0.4);
  background: #2c5282;
}

.btn-outline {
  background: white;
  color: #667eea;
  border: 2px solid #667eea;
}

.btn-outline:hover {
  background: #667eea;
  color: white;
}

/* Related Services */
.related-services h2 {
  font-size: 32px;
  font-weight: 700;
  color: #1a202c;
  margin-bottom: 30px;
}

.services-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
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

.service-image-small {
  width: 100%;
  height: 150px;
  background: #2b6cb0;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 15px;
}

.service-image-small img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.service-placeholder-small {
  font-size: 60px;
}

.service-info {
  padding: 20px;
}

.service-info h3 {
  font-size: 18px;
  font-weight: 600;
  color: #1a202c;
  margin-bottom: 10px;
}

.service-price {
  font-size: 20px;
  font-weight: 700;
  color: #2b6cb0;
  margin-bottom: 15px;
}

/* Loading */
.loading-page {
  min-height: 60vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.spinner {
  width: 60px;
  height: 60px;
  border: 5px solid #e2e8f0;
  border-top-color: #667eea;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 20px;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Responsive */
@media (max-width: 968px) {
  .service-main {
    grid-template-columns: 1fr;
    gap: 40px;
  }

  .service-image-block {
    position: static;
  }

  .service-title {
    font-size: 32px;
  }

  .service-meta {
    grid-template-columns: 1fr;
  }

  .service-actions {
    flex-direction: column;
  }

  .btn {
    width: 100%;
  }

  .services-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 640px) {
  .service-title {
    font-size: 28px;
  }

  .service-placeholder {
    font-size: 100px;
  }
}
</style>