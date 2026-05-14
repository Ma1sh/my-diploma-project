<template>
  <div class="orders-page">
    <div class="page-header">
      <div class="container">
        <h1 class="page-title">Мои заказы</h1>
        <router-link to="/orders/create" class="btn btn-primary">
          + Создать заказ
        </router-link>
      </div>
    </div>

    <div class="container">
      <!-- Filters -->
      <div class="filters-bar">
        <button 
          v-for="status in statuses" 
          :key="status.value"
          class="filter-btn"
          :class="{ active: filters.status === status.value }"
          @click="filterByStatus(status.value)"
        >
          {{ status.label }}
        </button>
      </div>

      <!-- Orders List -->
      <div v-if="loading" class="loading">
        <div class="spinner"></div>
        <p>Загрузка заказов...</p>
      </div>

      <div v-else-if="orders.length" class="orders-list">
        <div 
          v-for="order in orders" 
          :key="order.id"
          class="order-card"
          @click="goToOrder(order.id)"
        >
          <div class="order-header">
            <div class="order-number">
              <h3>Заказ #{{ order.id }}</h3>
              <span class="order-date">{{ formatDate(order.created_at) }}</span>
            </div>
            <div class="order-status" :class="`status-${order.status}`">
              {{ order.status_display }}
            </div>
          </div>

          <div class="order-body">
            <h4 class="order-title">{{ order.title }}</h4>
            <p class="order-service" v-if="order.service_name">
              Услуга: {{ order.service_name }}
            </p>
            <p class="order-device">{{ order.device_type }}</p>
          </div>

          <div class="order-footer">
            <div class="order-info">
              <span v-if="order.estimated_cost" class="order-cost">
                💰 {{ order.estimated_cost }} ₽
              </span>
              <span v-if="order.estimated_date" class="order-deadline">
                📅 {{ formatDate(order.estimated_date) }}
              </span>
            </div>
            <button class="btn btn-outline btn-small">Подробнее →</button>
          </div>
        </div>
      </div>

      <div v-else class="no-orders">
        <div class="no-orders-icon">📦</div>
        <h3>У вас пока нет заказов</h3>
        <p>Создайте свой первый заказ, чтобы начать работу с нами</p>
        <router-link to="/orders/create" class="btn btn-primary">
          Создать заказ
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import ordersApi from '@/services/ordersApi'

const router = useRouter()

const orders = ref([])
const loading = ref(false)
const filters = ref({
  status: ''
})

const statuses = [
  { value: '', label: 'Все' },
  { value: 'new', label: 'Новые' },
  { value: 'in_progress', label: 'В работе' },
  { value: 'ready', label: 'Готовы' },
  { value: 'completed', label: 'Завершены' },
  { value: 'cancelled', label: 'Отменены' }
]

const loadOrders = async () => {
  loading.value = true
  try {
    const params = {}
    if (filters.value.status) {
      params.status = filters.value.status
    }
    
    const response = await ordersApi.getOrders(params)
    orders.value = response.data.results
  } catch (error) {
    console.error('Error loading orders:', error)
  } finally {
    loading.value = false
  }
}

const filterByStatus = (status) => {
  filters.value.status = status
  loadOrders()
}

const goToOrder = (id) => {
  router.push(`/orders/${id}`)
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
  loadOrders()
})
</script>

<style scoped>
.page-header {
  background: #2b6cb0;
  color: white;
  padding: 60px 0;
  margin-bottom: 40px;
}

.page-header .container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.page-title {
  font-size: 42px;
  font-weight: 700;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  margin-bottom: 60px;
}

.filters-bar {
  display: flex;
  gap: 10px;
  margin-bottom: 30px;
  overflow-x: auto;
  padding: 10px 0;
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
  white-space: nowrap;
}

.filter-btn:hover {
  border-color: #667eea;
  color: #667eea;
}

.filter-btn.active {
  background: #2b6cb0;
  color: white;
  border-color: transparent;
}

.orders-list {
  display: grid;
  gap: 20px;
}

.order-card {
  background: white;
  border-radius: 15px;
  padding: 25px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
  cursor: pointer;
}

.order-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
}

.order-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 20px;
  padding-bottom: 20px;
  border-bottom: 2px solid #f7fafc;
}

.order-number h3 {
  font-size: 22px;
  font-weight: 700;
  color: #1a202c;
  margin-bottom: 5px;
}

.order-date {
  color: #718096;
  font-size: 14px;
}

.order-status {
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 14px;
  font-weight: 600;
}

.status-new {
  background: #bee3f8;
  color: #2c5282;
}

.status-in_progress {
  background: #feebc8;
  color: #c05621;
}

.status-waiting_parts {
  background: #fed7d7;
  color: #c53030;
}

.status-ready {
  background: #c6f6d5;
  color: #22543d;
}

.status-completed {
  background: #e2e8f0;
  color: #2d3748;
}

.status-cancelled {
  background: #fed7d7;
  color: #742a2a;
}

.order-body {
  margin-bottom: 20px;
}

.order-title {
  font-size: 18px;
  font-weight: 600;
  color: #1a202c;
  margin-bottom: 10px;
}

.order-service {
  color: #667eea;
  font-weight: 500;
  margin-bottom: 5px;
}

.order-device {
  color: #718096;
  font-size: 14px;
}

.order-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 20px;
  border-top: 2px solid #f7fafc;
}

.order-info {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
}

.order-cost,
.order-deadline {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-weight: 600;
  color: #4a5568;
  font-size: 14px;
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
  background: #2b6cb0;
  color: white;
  box-shadow: 0 4px 15px rgba(43, 108, 176, 0.3);
}

.btn-primary:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(43, 108, 176, 0.4);
  background: #2c5282;
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

.btn-small {
  padding: 8px 16px;
  font-size: 13px;
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

.no-orders {
  text-align: center;
  padding: 80px 20px;
}

.no-orders-icon {
  font-size: 100px;
  margin-bottom: 20px;
}

.no-orders h3 {
  font-size: 28px;
  color: #1a202c;
  margin-bottom: 10px;
}

.no-orders p {
  color: #718096;
  margin-bottom: 30px;
  font-size: 16px;
}

@media (max-width: 768px) {
  .page-header .container {
    flex-direction: column;
    gap: 20px;
    align-items: flex-start;
  }

  .page-title {
    font-size: 32px;
  }

  .btn-primary {
    width: 100%;
  }

  .order-header {
    flex-direction: column;
    gap: 15px;
  }

  .order-footer {
    flex-direction: column;
    gap: 15px;
    align-items: stretch;
  }

  .order-info {
    flex-direction: column;
    gap: 10px;
  }

  .btn-small {
    width: 100%;
  }
}
</style>