<template>
  <div class="contact-page">
    <div class="page-header">
      <div class="container">
        <h1 class="page-title">Контакты</h1>
        <p class="page-description">Свяжитесь с нами удобным для вас способом</p>
      </div>
    </div>

    <div class="container">
      <div class="contact-grid">
        <div class="contact-info">
          <div class="info-card">
            <h2>Наши контакты</h2>
            
            <div class="contact-item">
              <div class="contact-icon">📞</div>
              <div class="contact-details">
                <h3>Телефон</h3>
                <a href="tel:+79001234567">+7 (900) 123-45-67</a>
                <p>Пн-Пт: 9:00 - 20:00<br>Сб-Вс: 10:00 - 18:00</p>
              </div>
            </div>

            <div class="contact-item">
              <div class="contact-icon">✉️</div>
              <div class="contact-details">
                <h3>Email</h3>
                <a href="mailto:info@it-alliance.ru">info@it-alliance.ru</a>
                <p>Ответим в течение 24 часов</p>
              </div>
            </div>

            <div class="contact-item">
              <div class="contact-icon">📍</div>
              <div class="contact-details">
                <h3>Адрес</h3>
                <p>г. Белореченск</p>
              </div>
            </div>

            <div class="contact-item">
              <div class="contact-icon">🕐</div>
              <div class="contact-details">
                <h3>Режим работы</h3>
                <p>
                  Понедельник - Пятница: 9:00 - 20:00<br>
                  Суббота - Воскресенье: 10:00 - 18:00
                </p>
              </div>
            </div>
          </div>

          <div class="social-card">
            <h3>Мы в социальных сетях</h3>
            <div class="social-links">
              <a href="#" class="social-link">
                <span class="social-icon">VK</span>
                <span>ВКонтакте</span>
              </a>
              <a href="#" class="social-link">
                <span class="social-icon">TG</span>
                <span>Telegram</span>
              </a>
              <a href="#" class="social-link">
                <span class="social-icon">WA</span>
                <span>WhatsApp</span>
              </a>
            </div>
          </div>
        </div>

        <div class="contact-form-wrapper">
          <div class="form-card">
            <h2>Отправить сообщение</h2>
            <p class="form-description">
              Заполните форму и мы свяжемся с вами в ближайшее время
            </p>

            <form @submit.prevent="handleSubmit" class="contact-form">
              <div class="form-group">
                <label class="form-label">Ваше имя *</label>
                <input 
                  v-model="formData.name"
                  type="text"
                  class="form-control"
                  placeholder="Иван Иванов"
                  required
                >
              </div>

              <div class="form-group">
                <label class="form-label">Email *</label>
                <input 
                  v-model="formData.email"
                  type="email"
                  class="form-control"
                  placeholder="your@email.com"
                  required
                >
              </div>

              <div class="form-group">
                <label class="form-label">Телефон</label>
                <input 
                  v-model="formData.phone"
                  type="tel"
                  class="form-control"
                  placeholder="+7 (900) 123-45-67"
                >
              </div>

              <div class="form-group">
                <label class="form-label">Тема обращения *</label>
                <select v-model="formData.subject" class="form-control" required>
                  <option value="">Выберите тему</option>
                  <option value="repair">Ремонт техники</option>
                  <option value="consultation">Консультация</option>
                  <option value="partnership">Сотрудничество</option>
                  <option value="complaint">Жалоба</option>
                  <option value="other">Другое</option>
                </select>
              </div>

              <div class="form-group">
                <label class="form-label">Сообщение *</label>
                <textarea 
                  v-model="formData.message"
                  class="form-control"
                  rows="6"
                  placeholder="Опишите вашу проблему или вопрос..."
                  required
                ></textarea>
              </div>

              <button 
                type="submit" 
                class="btn btn-primary btn-block"
                :disabled="submitting"
              >
                <span v-if="submitting">Отправка...</span>
                <span v-else>Отправить сообщение</span>
              </button>
            </form>
          </div>
        </div>
      </div>

      <!-- Map -->
      <div class="map-section">
        <h2 class="section-title">Как нас найти</h2>
        <div class="map-placeholder">
          <div class="map-icon">🗺️</div>
          <p>г. Белореченск</p>
          <p class="map-hint">Карта будет здесь (интеграция с картами)</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useToast } from 'vue-toastification'

const toast = useToast()

const submitting = ref(false)
const formData = ref({
  name: '',
  email: '',
  phone: '',
  subject: '',
  message: ''
})

const handleSubmit = async () => {
  submitting.value = true
  
  // Симуляция отправки (здесь можно добавить реальный API запрос)
  setTimeout(() => {
    toast.success('Сообщение отправлено! Мы свяжемся с вами в ближайшее время.')
    formData.value = {
      name: '',
      email: '',
      phone: '',
      subject: '',
      message: ''
    }
    submitting.value = false
  }, 1500)
}
</script>

<style scoped>
.page-header {
  background: #2b6cb0;
  color: white;
  padding: 60px 0;
  margin-bottom: 80px;
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

.contact-grid {
  display: grid;
  grid-template-columns: 400px 1fr;
  gap: 40px;
  margin-bottom: 80px;
}

/* Contact Info */
.info-card {
  background: white;
  padding: 40px;
  border-radius: 20px;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.08);
  margin-bottom: 30px;
}

.info-card h2 {
  font-size: 28px;
  font-weight: 700;
  color: #1a202c;
  margin-bottom: 30px;
}

.contact-item {
  display: flex;
  gap: 20px;
  margin-bottom: 30px;
  padding-bottom: 30px;
  border-bottom: 2px solid #f7fafc;
}

.contact-item:last-child {
  border-bottom: none;
  margin-bottom: 0;
  padding-bottom: 0;
}

.contact-icon {
  width: 50px;
  height: 50px;
  background: #2b6cb0;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  flex-shrink: 0;
}

.contact-details h3 {
  font-size: 18px;
  font-weight: 600;
  color: #1a202c;
  margin-bottom: 8px;
}

.contact-details a {
  color: #2b6cb0;
  text-decoration: none;
  font-weight: 600;
  font-size: 16px;
  transition: color 0.3s;
  display: block;
  margin-bottom: 5px;
}

.contact-details a:hover {
  color: #2c5282;
}

.contact-details p {
  color: #718096;
  line-height: 1.6;
  font-size: 14px;
}

.social-card {
  background: white;
  padding: 30px;
  border-radius: 20px;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.08);
}

.social-card h3 {
  font-size: 20px;
  font-weight: 600;
  color: #1a202c;
  margin-bottom: 20px;
}

.social-links {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.social-link {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px;
  background: #f7fafc;
  border-radius: 10px;
  text-decoration: none;
  color: #4a5568;
  font-weight: 500;
  transition: all 0.3s;
}

.social-link:hover {
  background: #2b6cb0;
  color: white;
  transform: translateY(-3px);
}

.social-icon {
  width: 40px;
  height: 40px;
  background: white;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 12px;
}

/* Contact Form */
.form-card {
  background: white;
  padding: 40px;
  border-radius: 20px;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.08);
}

.form-card h2 {
  font-size: 28px;
  font-weight: 700;
  color: #1a202c;
  margin-bottom: 10px;
}

.form-description {
  color: #718096;
  margin-bottom: 30px;
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
}

.btn {
  padding: 16px 40px;
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

.btn-block {
  width: 100%;
}

/* Map */
.section-title {
  font-size: 32px;
  font-weight: 700;
  color: #1a202c;
  text-align: center;
  margin-bottom: 40px;
}

.map-placeholder {
  background: white;
  padding: 80px 40px;
  border-radius: 20px;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.08);
  text-align: center;
}

.map-icon {
  font-size: 80px;
  margin-bottom: 20px;
}

.map-placeholder p {
  font-size: 18px;
  color: #4a5568;
  margin-bottom: 10px;
}

.map-hint {
  color: #a0aec0;
  font-size: 14px;
}

@media (max-width: 968px) {
  .contact-grid {
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

  .info-card,
  .form-card {
    padding: 25px;
  }
}
</style>