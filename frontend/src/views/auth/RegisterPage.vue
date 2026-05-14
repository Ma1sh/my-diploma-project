<template>
  <div class="auth-page">
    <div class="auth-container">
      <div class="auth-box">
        <div class="auth-header">
          <div class="logo">
            <div class="logo-icon">
              <span class="logo-text">IT</span>
            </div>
            <span class="logo-title">IT Альянс</span>
          </div>
          <h1>Регистрация</h1>
          <p>Создайте аккаунт для доступа ко всем возможностям</p>
        </div>

        <form @submit.prevent="handleRegister" class="auth-form">
          <div class="form-row">
            <div class="form-group">
              <label class="form-label">Имя *</label>
              <input 
                v-model="formData.first_name"
                type="text"
                class="form-control"
                placeholder="Иван"
                required
              >
            </div>

            <div class="form-group">
              <label class="form-label">Фамилия *</label>
              <input 
                v-model="formData.last_name"
                type="text"
                class="form-control"
                placeholder="Иванов"
                required
              >
            </div>
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
            <label class="form-label">Пароль *</label>
            <div class="password-input">
              <input 
                v-model="formData.password"
                :type="showPassword ? 'text' : 'password'"
                class="form-control"
                placeholder="Минимум 8 символов"
                required
                minlength="8"
              >
              <button 
                type="button"
                class="password-toggle"
                @click="showPassword = !showPassword"
              >
                {{ showPassword ? '👁️' : '👁️‍🗨️' }}
              </button>
            </div>
          </div>

          <div class="form-group">
            <label class="form-label">Подтверждение пароля *</label>
            <div class="password-input">
              <input 
                v-model="formData.re_password"
                :type="showPasswordConfirm ? 'text' : 'password'"
                class="form-control"
                placeholder="Повторите пароль"
                required
              >
              <button 
                type="button"
                class="password-toggle"
                @click="showPasswordConfirm = !showPasswordConfirm"
              >
                {{ showPasswordConfirm ? '👁️' : '👁️‍🗨️' }}
              </button>
            </div>
          </div>

          <div class="password-match" v-if="formData.re_password">
            <span 
              :class="passwordsMatch ? 'match-success' : 'match-error'"
            >
              {{ passwordsMatch ? '✓ Пароли совпадают' : '✗ Пароли не совпадают' }}
            </span>
          </div>

          <button 
            type="submit" 
            class="btn btn-primary btn-block"
            :disabled="loading || !passwordsMatch"
          >
            <span v-if="loading">Регистрация...</span>
            <span v-else>Зарегистрироваться</span>
          </button>
        </form>

        <div class="auth-footer">
          <p>Уже есть аккаунт? 
            <router-link to="/login">Войти</router-link>
          </p>
        </div>
      </div>

      <div class="auth-image">
        <div class="image-content">
          <h2>Присоединяйтесь к нам!</h2>
          <p>Зарегистрируйтесь и получите доступ ко всем преимуществам нашего сервиса</p>
          <div class="features-list">
            <div class="feature">
              <span class="feature-icon">✓</span>
              <span>Онлайн заказы</span>
            </div>
            <div class="feature">
              <span class="feature-icon">✓</span>
              <span>Отслеживание статуса</span>
            </div>
            <div class="feature">
              <span class="feature-icon">✓</span>
              <span>История заказов</span>
            </div>
            <div class="feature">
              <span class="feature-icon">✓</span>
              <span>Специальные предложения</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../../stores/auth'
import { useToast } from 'vue-toastification'

const router = useRouter()
const authStore = useAuthStore()
const toast = useToast()

const formData = ref({
  first_name: '',
  last_name: '',
  email: '',
  phone: '',
  password: '',
  re_password: ''
})

const loading = ref(false)
const showPassword = ref(false)
const showPasswordConfirm = ref(false)

const passwordsMatch = computed(() => {
  return formData.value.password === formData.value.re_password
})

const handleRegister = async () => {
  if (!passwordsMatch.value) {
    toast.error('Пароли не совпадают')
    return
  }

  loading.value = true
  try {
    await authStore.register(formData.value)
    toast.success('Регистрация успешна! Теперь вы можете войти')
    router.push('/login')
  } catch (error) {
    console.error('Registration error:', error)
    if (error.response?.data?.email) {
      toast.error('Пользователь с таким email уже существует')
    } else {
      toast.error('Ошибка регистрации. Проверьте данные')
    }
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.auth-page {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #2b6cb0;
  padding: 40px 20px;
}

.auth-container {
  max-width: 1100px;
  width: 100%;
  display: grid;
  grid-template-columns: 1fr 1fr;
  background: white;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
}

.auth-box {
  padding: 60px 50px;
  max-height: 90vh;
  overflow-y: auto;
}

.auth-header {
  margin-bottom: 30px;
}

.logo {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 25px;
}

.logo-icon {
  width: 50px;
  height: 50px;
  background: #2b6cb0;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 15px rgba(43, 108, 176, 0.4);
}

.logo-text {
  color: white;
  font-size: 24px;
  font-weight: 700;
}

.logo-title {
  font-size: 22px;
  font-weight: 700;
  color: #1a202c;
}

.auth-header h1 {
  font-size: 32px;
  font-weight: 700;
  color: #1a202c;
  margin-bottom: 10px;
}

.auth-header p {
  color: #718096;
  font-size: 16px;
}

.auth-form {
  margin-bottom: 25px;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 15px;
}

.form-group {
  margin-bottom: 20px;
}

.form-label {
  display: block;
  font-weight: 600;
  color: #2d3748;
  margin-bottom: 8px;
  font-size: 14px;
}

.form-control {
  width: 100%;
  padding: 12px 14px;
  border: 2px solid #e2e8f0;
  border-radius: 10px;
  font-size: 14px;
  transition: all 0.3s;
  font-family: inherit;
}

.form-control:focus {
  outline: none;
  border-color: #2b6cb0;
  box-shadow: 0 0 0 3px rgba(43, 108, 176, 0.1);
}

.password-input {
  position: relative;
}

.password-toggle {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  cursor: pointer;
  font-size: 18px;
  padding: 5px;
}

.password-match {
  margin-bottom: 20px;
  font-size: 14px;
  font-weight: 600;
}

.match-success {
  color: #22543d;
}

.match-error {
  color: #c53030;
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

.auth-footer {
  text-align: center;
  padding-top: 20px;
  border-top: 2px solid #f7fafc;
}

.auth-footer p {
  color: #718096;
}

.auth-footer a {
  color: #2b6cb0;
  text-decoration: none;
  font-weight: 600;
  transition: color 0.3s;
}

.auth-footer a:hover {
  color: #2c5282;
}

.auth-image {
  background: #2b6cb0;
  padding: 60px 50px;
  display: flex;
  align-items: center;
  color: white;
  position: relative;
  overflow: hidden;
}

.auth-image::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: url('data:image/svg+xml,<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="40" fill="rgba(255,255,255,0.05)"/></svg>');
  opacity: 0.2;
}

.image-content {
  position: relative;
  z-index: 1;
}

.image-content h2 {
  font-size: 36px;
  font-weight: 700;
  margin-bottom: 20px;
  line-height: 1.2;
}

.image-content p {
  font-size: 18px;
  line-height: 1.6;
  opacity: 0.95;
  margin-bottom: 40px;
}

.features-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.feature {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 16px;
}

.feature-icon {
  width: 28px;
  height: 28px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
}

@media (max-width: 968px) {
  .auth-container {
    grid-template-columns: 1fr;
  }

  .auth-image {
    display: none;
  }

  .auth-box {
    padding: 40px 30px;
  }

  .form-row {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 640px) {
  .auth-box {
    padding: 30px 20px;
  }

  .auth-header h1 {
    font-size: 26px;
  }
}
</style>