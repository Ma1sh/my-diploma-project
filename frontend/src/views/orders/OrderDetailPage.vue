<template>
  <div class="order-detail-page" v-if="order">
    <div class="page-header">
      <div class="container">
        <nav class="breadcrumbs">
          <router-link to="/">Главная</router-link>
          <span>/</span>
          <router-link to="/orders">Мои заказы</router-link>
          <span>/</span>
          <span>Заказ #{{ order.id }}</span>
        </nav>
      </div>
    </div>

    <div class="container">
      <div class="order-content">
        <div class="order-main">
          <div class="order-header-card">
            <div class="order-title-section">
              <h1 class="order-title">Заказ #{{ order.id }}</h1>
              <div class="order-status" :class="`status-${order.status}`">
                {{ order.status_display }}
              </div>
            </div>
            <div class="order-meta">
              <div class="meta-item">
                <span class="meta-label">Создан:</span>
                <span class="meta-value">{{ formatDate(order.created_at) }}</span>
              </div>
              <div class="meta-item">
                <span class="meta-label">Обновлен:</span>
                <span class="meta-value">{{ formatDate(order.updated_at) }}</span>
              </div>
            </div>
          </div>

          <div class="info-card">
            <h2 class="card-title">Информация о заказе</h2>
            <div class="info-grid">
              <div class="info-item">
                <span class="info-label">Название:</span>
                <span class="info-value">{{ order.title }}</span>
              </div>
              <div class="info-item" v-if="order.service_info">
                <span class="info-label">Услуга:</span>
                <span class="info-value">{{ order.service_info.name }}</span>
              </div>
              <div class="info-item">
                <span class="info-label">Устройство:</span>
                <span class="info-value">{{ order.device_type }}</span>
              </div>
              <div class="info-item" v-if="order.device_model">
                <span class="info-label">Модель:</span>
                <span class="info-value">{{ order.device_model }}</span>
              </div>
              <div class="info-item" v-if="order.estimated_cost">
                <span class="info-label">Предв. стоимость:</span>
                <span class="info-value highlight">{{ order.estimated_cost }} ₽</span>
              </div>
              <div class="info-item" v-if="order.final_cost">
                <span class="info-label">Итоговая стоимость:</span>
                <span class="info-value highlight">{{ order.final_cost }} ₽</span>
              </div>
              <div class="info-item" v-if="order.estimated_date">
                <span class="info-label">Готовность:</span>
                <span class="info-value">{{ formatDate(order.estimated_date) }}</span>
              </div>
            </div>
          </div>

          <div class="info-card">
            <h2 class="card-title">Описание проблемы</h2>
            <p class="description-text">{{ order.description }}</p>
          </div>

          <div class="info-card" v-if="order.admin_notes">
            <h2 class="card-title">Комментарии мастера</h2>
            <div class="admin-notes">
              <span class="notes-icon">💬</span>
              <p>{{ order.admin_notes }}</p>
            </div>
          </div>

          <div class="info-card" v-if="order.client_notes">
            <h2 class="card-title">Ваши комментарии</h2>
            <p class="description-text">{{ order.client_notes }}</p>
          </div>

          <div class="info-card" v-if="order.status_history && order.status_history.length">
            <h2 class="card-title">История изменений</h2>
            <div class="timeline">
              <div 
                v-for="history in order.status_history" 
                :key="history.id"
                class="timeline-item"
              >
                <div class="timeline-dot"></div>
                <div class="timeline-content">
                  <div class="timeline-header">
                    <span class="timeline-status">{{ getStatusLabel(history.status) }}</span>
                    <span class="timeline-date">{{ formatDateTime(history.created_at) }}</span>
                  </div>
                  <p v-if="history.comment" class="timeline-comment">{{ history.comment }}</p>
                  <span v-if="history.created_by_name" class="timeline-author">
                    {{ history.created_by_name }}
                  </span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="order-sidebar">
          <div class="info-card">
            <h3 class="card-title">Контактная информация</h3>
            <div class="contact-list">
              <div class="contact-item">
                <span class="contact-icon">📞</span>
                <a :href="`tel:${order.contact_phone}`">{{ order.contact_phone }}</a>
              </div>
              <div class="contact-item" v-if="order.contact_email">
                <span class="contact-icon">✉️</span>
                <a :href="`mailto:${order.contact_email}`">{{ order.contact_email }}</a>
              </div>
            </div>
          </div>

          <div class="info-card">
            <h3 class="card-title">Клиент</h3>
            <div class="user-info" v-if="order.user_info">
              <div class="user-avatar">
                {{ getInitials(order.user_info.first_name, order.user_info.last_name) }}
              </div>
              <div class="user-details">
                <p class="user-name">
                  {{ order.user_info.first_name }} {{ order.user_info.last_name }}
                </p>
                <p class="user-email">{{ order.user_info.email }}</p>
              </div>
            </div>
          </div>

          <div class="info-card highlight">
            <h3 class="card-title">Нужна помощь?</h3>
            <p>Свяжитесь с нами по телефону или email</p>
            <a href="tel:+79001234567" class="btn btn-primary btn-block">
              📞 Позвонить
            </a>
          </div>

          <div class="info-card" v-if="order.service_info">
            <h3 class="card-title">Выбранная услуга</h3>
            <div class="service-preview">
              <div class="service-image-small">
                <img 
                  v-if="order.service_info.image" 
                  :src="order.service_info.image" 
                  :alt="order.service_info.name"
                >
                <div v-else class="service-placeholder">🔧</div>
              </div>
              <h4>{{ order.service_info.name }}</h4>
              <p class="service-price">от {{ order.service_info.price_from }} ₽</p>
              <router-link 
                :to="`/services/${order.service_info.id}`"
                class="btn btn-outline btn-small btn-block"
              >
                Подробнее
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div v-else class="loading-page">
    <div class="spinner"></div>
    <p>Загрузка заказа...</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import ordersApi from '@/services/ordersApi'
import { useToast } from 'vue-toastification'

const route = useRoute()
const router = useRouter()
const toast = useToast()

const order = ref(null)

const statusLabels = {
  'new': 'Новая',
  'in_progress': 'В работе',
  'waiting_parts': 'Ожидание запчастей',
  'ready': 'Готова',
  'completed': 'Завершена',
  'cancelled': 'Отменена'
}

const loadOrder = async () => {
  try {
    const response = await ordersApi.getOrder(route.params.id)
    order.value = response.data
  } catch (error) {
    console.error('Error loading order:', error)
    toast.error('Заказ не найден')
    router.push('/orders')
  }
}

const formatDate = (dateString) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', {
    day: 'numeric',
    month: 'long',
    year: 'numeric'
  })
}

const formatDateTime = (dateString) => {
  const date = new Date(dateString)
  return date.toLocaleString('ru-RU', {
    day: 'numeric',
    month: 'long',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

const getStatusLabel = (status) => {
  return statusLabels[status] || status
}

const getInitials = (firstName, lastName) => {
  return `${firstName?.[0] || ''}${lastName?.[0] || ''}`.toUpperCase()
}

onMounted(() => {
  loadOrder()
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
  margin-bottom: 80px;
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

.order-content {
  display: grid;
  grid-template-columns: 1fr 380px;
  gap: 30px;
}

.order-header-card {
  background: white;
  padding: 30px;
  border-radius: 15px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  margin-bottom: 25px;
}

.order-title-section {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  padding-bottom: 20px;
  border-bottom: 2px solid #f7fafc;
}

.order-title {
  font-size: 32px;
  font-weight: 700;
  color: #1a202c;
}

.order-status {
  padding: 10px 20px;
  border-radius: 20px;
  font-size: 14px;
  font-weight: 600;
}

.status-new { background: #bee3f8; color: #2c5282; }
.status-in_progress { background: #feebc8; color: #c05621; }
.status-waiting_parts { background: #fed7d7; color: #c53030; }
.status-ready { background: #c6f6d5; color: #22543d; }
.status-completed { background: #e2e8f0; color: #2d3748; }
.status-cancelled { background: #fed7d7; color: #742a2a; }

.order-meta {
  display: flex;
  gap: 30px;
}

.meta-item {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.meta-label {
  font-size: 14px;
  color: #718096;
}

.meta-value {
  font-size: 16px;
  font-weight: 600;
  color: #1a202c;
}

.info-card {
  background: white;
  padding: 30px;
  border-radius: 15px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  margin-bottom: 25px;
}

.card-title {
  font-size: 22px;
  font-weight: 700;
  color: #1a202c;
  margin-bottom: 20px;
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
}

.info-item {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.info-label {
  font-size: 14px;
  color: #718096;
}

.info-value {
  font-size: 16px;
  font-weight: 600;
  color: #1a202c;
}

.info-value.highlight {
  color: #667eea;
  font-size: 20px;
}

.description-text {
  color: #4a5568;
  line-height: 1.8;
  font-size: 16px;
}

.admin-notes {
  display: flex;
  gap: 15px;
  padding: 20px;
  background: #f7fafc;
  border-radius: 12px;
  border-left: 4px solid #667eea;
}

.notes-icon {
  font-size: 24px;
}

.admin-notes p {
  color: #4a5568;
  line-height: 1.6;
  margin: 0;
}

/* Timeline */
.timeline {
  position: relative;
  padding-left: 30px;
}

.timeline::before {
  content: '';
  position: absolute;
  left: 8px;
  top: 8px;
  bottom: 8px;
  width: 2px;
  background: #e2e8f0;
}

.timeline-item {
  position: relative;
  margin-bottom: 25px;
}

.timeline-item:last-child {
  margin-bottom: 0;
}

.timeline-dot {
  position: absolute;
  left: -26px;
  top: 4px;
  width: 18px;
  height: 18px;
  background: #2b6cb0;
  border-radius: 50%;
  border: 3px solid white;
  box-shadow: 0 0 0 2px #2b6cb0;
}

.timeline-content {
  background: #f7fafc;
  padding: 15px;
  border-radius: 10px;
}

.timeline-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}

.timeline-status {
  font-weight: 600;
  color: #1a202c;
}

.timeline-date {
  font-size: 13px;
  color: #718096;
}

.timeline-comment {
  color: #4a5568;
  margin: 8px 0;
  font-size: 14px;
}

.timeline-author {
  font-size: 13px;
  color: #2b6cb0;
  font-weight: 500;
}

/* Sidebar */
.contact-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.contact-item {
  display: flex;
  gap: 12px;
  align-items: center;
}

.contact-icon {
  font-size: 20px;
}

.contact-item a {
  color: #667eea;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.3s;
}

.contact-item a:hover {
  color: #764ba2;
}

.user-info {
  display: flex;
  gap: 15px;
  align-items: center;
}

.user-avatar {
  width: 60px;
  height: 60px;
  background: #2b6cb0;
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 20px;
}

.user-details {
  flex: 1;
}

.user-name {
  font-weight: 600;
  color: #1a202c;
  margin-bottom: 5px;
}

.user-email {
  font-size: 14px;
  color: #718096;
}

.info-card.highlight {
  background: #2b6cb0;
  color: white;
}

.info-card.highlight .card-title {
  color: white;
}

.info-card.highlight p {
  color: white;
  opacity: 0.95;
  margin-bottom: 20px;
}

.service-preview {
  text-align: center;
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
  border-radius: 12px;
}

.service-placeholder {
  font-size: 50px;
}

.service-price {
  font-size: 20px;
  font-weight: 700;
  color: #2b6cb0;
  margin-bottom: 15px;
}

.service-price {
  font-size: 20px;
  font-weight: 700;
  color: #667eea;
  margin-bottom: 15px;
}

.btn {
  padding: 12px 24px;
  border-radius: 10px;
  font-weight: 600;
  text-decoration: none;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 14px;
  display: inline-block;
  text-align: center;
}

.btn-primary {
  background: white;
  color: #2b6cb0;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 15px rgba(255, 255, 255, 0.3);
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

.btn-block {
  width: 100%;
}

.btn-small {
  padding: 8px 16px;
  font-size: 13px;
}

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
  .order-content {
    grid-template-columns: 1fr;
  }

  .order-title-section {
    flex-direction: column;
    align-items: flex-start;
    gap: 15px;
  }

  .order-meta {
    flex-direction: column;
    gap: 15px;
  }

  .info-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 640px) {
  .order-title {
    font-size: 24px;
  }
}
</style>