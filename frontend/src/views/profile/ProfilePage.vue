<template>
  <div class="profile-page">
    <div class="page-header">
      <div class="container">
        <h1 class="page-title">Мой профиль</h1>
      </div>
    </div>

    <div class="container">
      <div class="profile-content">
        <div class="profile-sidebar">
          <div class="profile-card">
            <div class="profile-avatar">
              <img v-if="authStore.user?.avatar" :src="authStore.user.avatar" alt="Avatar">
              <div v-else class="avatar-placeholder">
                {{ getInitials() }}
              </div>
            </div>
            <h2>{{ authStore.user?.first_name }} {{ authStore.user?.last_name }}</h2>
            <p>{{ authStore.user?.email }}</p>
          </div>

          <div class="profile-stats">
            <div class="stat-item">
              <span class="stat-value">{{ ordersCount }}</span>
              <span class="stat-label">Всего заказов</span>
            </div>
            <div class="stat-item">
              <span class="stat-value">{{ formatDate(authStore.user?.created_at) }}</span>
              <span class="stat-label">С нами с</span>
            </div>
          </div>
        </div>

        <div class="profile-main">
          <form @submit.prevent="handleUpdateProfile" class="profile-form">
            <div class="form-section">
              <h2 class="section-title">Личная информация</h2>
              
              <div class="form-row">
                <div class="form-group">
                  <label class="form-label">Имя</label>
                  <input 
                    v-model="formData.first_name"
                    type="text"
                    class="form-control"
                    required
                  >
                </div>

                <div class="form-group">
                  <label class="form-label">Фамилия</label>
                  <input 
                    v-model="formData.last_name"
                    type="text"
                    class="form-control"
                    required
                  >
                </div>
              </div>

              <div class="form-group">
                <label class="form-label">Email</label>
                <input 
                  v-model="formData.email"
                  type="email"
                  class="form-control"
                  required
                >
              </div>

              <div class="form-group">
                <label class="form-label">Телефон</label>
                <input 
                  v-model="formData.phone"
                  type="tel"
                  class="form-control"
                >
              </div>
            </div>

            <div class="form-actions">
              <button 
                type="submit" 
                class="btn btn-primary"
                :disabled="loading"
              >
                <span v-if="loading">Сохранение...</span>
                <span v-else>Сохранить изменения</span>
              </button>
            </div>
          </form>

          <div class="danger-zone">
            <h2 class="section-title">Опасная зона</h2>
            <div class="danger-content">
              <div class="danger-info">
                <h3>Выход из аккаунта</h3>
                <p>Вы будете перенаправлены на главную страницу</p>
              </div>
              <button @click="handleLogout" class="btn btn-danger">
                Выйти
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import ordersApi from '@/services/ordersApi'
import { useToast } from 'vue-toastification'

const router = useRouter()
const authStore = useAuthStore()
const toast = useToast()

const loading = ref(false)
const ordersCount = ref(0)

const formData = ref({
  first_name: '',
  last_name: '',
  email: '',
  phone: ''
})

const loadOrdersCount = async () => {
  try {
    const response = await ordersApi.getOrders()
    ordersCount.value = response.data.count
  } catch (error) {
    console.error('Error loading orders count:', error)
  }
}

const getInitials = () => {
  const firstName = authStore.user?.first_name || ''
  const lastName = authStore.user?.last_name || ''
  return `${firstName[0] || ''}${lastName[0] || ''}`.toUpperCase()
}

const formatDate = (dateString) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', {
    month: 'long',
    year: 'numeric'
  })
}

const handleUpdateProfile = async () => {
  loading.value = true
  try {
    await authStore.updateProfile(formData.value)
    toast.success('Профиль успешно обновлен!')
  } catch (error) {
    console.error('Error updating profile:', error)
    toast.error('Ошибка обновления профиля')
  } finally {
    loading.value = false
  }
}

const handleLogout = () => {
  authStore.logout()
  toast.success('Вы вышли из системы')
  router.push('/')
}

onMounted(() => {
  if (authStore.user) {
    formData.value = {
      first_name: authStore.user.first_name,
      last_name: authStore.user.last_name,
      email: authStore.user.email,
      phone: authStore.user.phone || ''
    }
  }
  loadOrdersCount()
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
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  margin-bottom: 80px;
}

.profile-content {
  display: grid;
  grid-template-columns: 350px 1fr;
  gap: 40px;
}

.profile-sidebar {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.profile-card {
  background: white;
  padding: 40px;
  border-radius: 20px;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.08);
  text-align: center;
}

.profile-avatar {
  width: 120px;
  height: 120px;
  margin: 0 auto 20px;
  border-radius: 50%;
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
}

.profile-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.avatar-placeholder {
  width: 100%;
  height: 100%;
  background: #2b6cb0;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 48px;
  font-weight: 700;
}

.profile-card h2 {
  font-size: 24px;
  font-weight: 700;
  color: #1a202c;
  margin-bottom: 5px;
}

.profile-card p {
  color: #718096;
}

.profile-stats {
  background: white;
  padding: 30px;
  border-radius: 20px;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.08);
  display: grid;
  gap: 20px;
}

.stat-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 5px;
}

.stat-value {
  font-size: 32px;
  font-weight: 700;
  color: #2b6cb0;
}

.stat-label {
  font-size: 14px;
  color: #718096;
}

.profile-main {
  display: flex;
  flex-direction: column;
  gap: 30px;
}

.profile-form {
  background: white;
  padding: 40px;
  border-radius: 20px;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.08);
}

.form-section {
  margin-bottom: 30px;
}

.section-title {
  font-size: 24px;
  font-weight: 700;
  color: #1a202c;
  margin-bottom: 25px;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

.form-group {
  margin-bottom: 20px;
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

.form-actions {
  padding-top: 20px;
  border-top: 2px solid #f7fafc;
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

.danger-zone {
  background: white;
  padding: 40px;
  border-radius: 20px;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.08);
  border: 2px solid #fed7d7;
}

.danger-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.danger-info h3 {
  font-size: 18px;
  font-weight: 600;
  color: #1a202c;
  margin-bottom: 5px;
}

.danger-info p {
  color: #718096;
  font-size: 14px;
}

.btn-danger {
  background: #c53030;
  color: white;
}

.btn-danger:hover {
  background: #9b2c2c;
  transform: translateY(-2px);
}

@media (max-width: 968px) {
  .profile-content {
    grid-template-columns: 1fr;
  }

  .form-row {
    grid-template-columns: 1fr;
  }

  .danger-content {
    flex-direction: column;
    gap: 20px;
    text-align: center;
  }

  .btn {
    width: 100%;
  }
}

@media (max-width: 640px) {
  .page-title {
    font-size: 32px;
  }
}
</style>