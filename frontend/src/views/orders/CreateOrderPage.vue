<template>
  <div class="create-order-page">
    <div class="page-header">
      <div class="container">
        <h1 class="page-title">Создание заказа</h1>
        <p class="page-description">Заполните форму для создания заказа</p>
      </div>
    </div>

    <div class="container">
      <div class="order-form-wrapper">
        <form @submit.prevent="handleSubmit" class="order-form">
          <div class="form-section">
            <h2 class="section-title">Информация об устройстве</h2>
            
            <div class="form-group">
              <label class="form-label">Выберите услугу *</label>
              <select 
                v-model="formData.service" 
                class="form-control"
                required
                @change="onServiceChange"
              >
                <option value="">Выберите услугу</option>
                <option 
                  v-for="service in services" 
                  :key="service.id" 
                  :value="service.id"
                >
                  {{ service.name }} - от {{ service.price_from }} ₽
                </option>
              </select>
            </div>

            <div class="form-group">
              <label class="form-label">Название проблемы *</label>
              <input 
                v-model="formData.title" 
                type="text"
                class="form-control"
                placeholder="Например: Не включается ноутбук"
                required
              >
            </div>

            <div class="form-group">
              <label class="form-label">Тип устройства *</label>
              <select 
                v-model="formData.device_type" 
                class="form-control"
                required
              >
                <option value="">Выберите тип</option>
                <option value="Ноутбук">Ноутбук</option>
                <option value="Компьютер">Компьютер</option>
                <option value="Моноблок">Моноблок</option>
                <option value="Планшет">Планшет</option>
                <option value="Смартфон">Смартфон</option>
                <option value="Другое">Другое</option>
              </select>
            </div>

            <div class="form-group">
              <label class="form-label">Модель устройства</label>
              <input 
                v-model="formData.device_model" 
                type="text"
                class="form-control"
                placeholder="Например: Dell Inspiron 15 3000"
              >
            </div>

            <div class="form-group">
              <label class="form-label">Описание проблемы *</label>
              <textarea 
                v-model="formData.description"
                class="form-control"
                rows="5"
                placeholder="Опишите проблему подробно..."
                required
              ></textarea>
            </div>
          </div>

          <div class="form-section">
            <h2 class="section-title">Контактные данные</h2>
            
            <div class="form-group">
              <label class="form-label">Контактный телефон *</label>
              <input 
                v-model="formData.contact_phone" 
                type="tel"
                class="form-control"
                placeholder="+7 (900) 123-45-67"
                required
              >
            </div>

            <div class="form-group">
              <label class="form-label">Email для связи</label>
              <input 
                v-model="formData.contact_email" 
                type="email"
                class="form-control"
                placeholder="your@email.com"
              >
            </div>

            <div class="form-group">
              <label class="form-label">Дополнительные комментарии</label>
              <textarea 
                v-model="formData.client_notes"
                class="form-control"
                rows="3"
                placeholder="Дополнительная информация..."
              ></textarea>
            </div>
          </div>

          <div class="form-actions">
            <button 
              type="submit" 
              class="btn btn-primary btn-large"
              :disabled="submitting"
            >
              <span v-if="submitting">Отправка...</span>
              <span v-else>Создать заказ</span>
            </button>
            <router-link to="/orders" class="btn btn-outline btn-large">
              Отмена
            </router-link>
          </div>
        </form>

        <div class="order-info-sidebar">
          <div class="info-card">
            <h3>Как это работает?</h3>
            <ol class="steps-list">
              <li>
                <span class="step-number">1</span>
                <span class="step-text">Заполните форму заказа</span>
              </li>
              <li>
                <span class="step-number">2</span>
                <span class="step-text">Мы свяжемся с вами для уточнения деталей</span>
              </li>
              <li>
                <span class="step-number">3</span>
                <span class="step-text">Привезите устройство в сервисный центр</span>
              </li>
              <li>
                <span class="step-number">4</span>
                <span class="step-text">Получите отремонтированное устройство</span>
              </li>
            </ol>
          </div>

          <div class="info-card">
            <h3>Контакты</h3>
            <div class="contact-item">
              <span class="contact-icon">📞</span>
              <a href="tel:+79001234567">+7 (900) 123-45-67</a>
            </div>
            <div class="contact-item">
              <span class="contact-icon">✉️</span>
              <a href="mailto:info@it-alliance.ru">info@it-alliance.ru</a>
            </div>
            <div class="contact-item">
              <span class="contact-icon">📍</span>
              <span>г. Москва, ул. Примерная, д. 1</span>
            </div>
          </div>

          <div class="info-card highlight">
            <h3>🎉 Акция!</h3>
            <p>Бесплатная диагностика при ремонте в нашем сервисном центре</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import servicesApi from '@/services/servicesApi'
import ordersApi from '@/services/ordersApi'
import { useToast } from 'vue-toastification'

const router = useRouter()
const route = useRoute()
const authStore = useAuthStore()
const toast = useToast()

const services = ref([])
const submitting = ref(false)

const formData = ref({
  service: route.query.service || '',
  title: '',
  description: '',
  device_type: '',
  device_model: '',
  contact_phone: authStore.user?.phone || '',
  contact_email: authStore.user?.email || '',
  client_notes: ''
})

const loadServices = async () => {
  try {
    const response = await servicesApi.getServices({ page_size: 100 })
    services.value = response.data.results
  } catch (error) {
    console.error('Error loading services:', error)
  }
}

const onServiceChange = () => {
  const selectedService = services.value.find(s => s.id === parseInt(formData.value.service))
  if (selectedService && !formData.value.title) {
    formData.value.title = selectedService.name
  }
}

const handleSubmit = async () => {
  submitting.value = true
  try {
    const response = await ordersApi.createOrder(formData.value)
    toast.success('Заказ успешно создан!')
    router.push(`/orders/${response.data.id}`)
  } catch (error) {
    console.error('Error creating order:', error)
    toast.error('Ошибка при создании заказа')
  } finally {
    submitting.value = false
  }
}

onMounted(() => {
  loadServices()
})
</script>

<style scoped>
.page-header {
  background: #2b6cb0;
  color: white;
  padding: 60px 0;
  margin-bottom: 60px;
}

.page-title {
  font-size: 42px;
  font-weight: 700;
  margin-bottom: 10px;
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

.order-form-wrapper {
  display: grid;
  grid-template-columns: 1fr 380px;
  gap: 40px;
}

.order-form {
  background: white;
  padding: 40px;
  border-radius: 20px;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.08);
}

.form-section {
  margin-bottom: 40px;
  padding-bottom: 40px;
  border-bottom: 2px solid #f7fafc;
}

.form-section:last-of-type {
  border-bottom: none;
}

.section-title {
  font-size: 24px;
  font-weight: 700;
  color: #1a202c;
  margin-bottom: 25px;
}

.form-group {
  margin-bottom: 25px;
}

.form-label {
  display: block;
  font-weight: 600;
  color: #2d3748;
  margin-bottom: 8px;
  font-size: 15px;
}

.form-control {
  width: 100%;
  padding: 14px 16px;
  border: 2px solid #e2e8f0;
  border-radius: 10px;
  font-size: 15px;
  transition: all 0.3s;
  font-family: inherit;
}

.form-control:focus {
  outline: none;
  border-color: #2b6cb0;
  box-shadow: 0 0 0 3px rgba(43, 108, 176, 0.1);
}

select.form-control {
  cursor: pointer;
}

textarea.form-control {
  resize: vertical;
  min-height: 100px;
}

.form-actions {
  display: flex;
  gap: 15px;
}

.btn {
  padding: 14px 32px;
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
  padding: 16px 40px;
  font-size: 18px;
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

/* Sidebar */
.order-info-sidebar {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.info-card {
  background: white;
  padding: 25px;
  border-radius: 15px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
}

.info-card h3 {
  font-size: 20px;
  font-weight: 700;
  color: #1a202c;
  margin-bottom: 20px;
}

.steps-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.steps-list li {
  display: flex;
  gap: 15px;
  margin-bottom: 20px;
  align-items: flex-start;
}

.steps-list li:last-child {
  margin-bottom: 0;
}

.step-number {
  width: 32px;
  height: 32px;
  background: #2b6cb0;
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 14px;
  flex-shrink: 0;
}

.step-text {
  color: #4a5568;
  line-height: 1.6;
  padding-top: 5px;
}

.contact-item {
  display: flex;
  gap: 12px;
  align-items: center;
  margin-bottom: 15px;
  color: #4a5568;
}

.contact-item:last-child {
  margin-bottom: 0;
}

.contact-icon {
  font-size: 20px;
}

.contact-item a {
  color: #2b6cb0;
  text-decoration: none;
  transition: color 0.3s;
}

.contact-item a:hover {
  color: #2c5282;
}

.info-card.highlight {
  background: #2b6cb0;
  color: white;
}

.info-card.highlight h3 {
  color: white;
}

.info-card.highlight p {
  color: white;
  opacity: 0.95;
  line-height: 1.6;
}

/* Responsive */
@media (max-width: 968px) {
  .order-form-wrapper {
    grid-template-columns: 1fr;
  }

  .order-info-sidebar {
    order: -1;
  }

  .page-title {
    font-size: 32px;
  }

  .form-actions {
    flex-direction: column;
  }

  .btn {
    width: 100%;
  }
}

@media (max-width: 640px) {
  .page-title {
    font-size: 28px;
  }

  .order-form {
    padding: 25px;
  }

  .section-title {
    font-size: 20px;
  }
}
</style>