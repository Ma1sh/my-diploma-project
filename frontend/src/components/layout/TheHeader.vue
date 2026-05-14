<template>
  <header class="header" :class="{ 'header-scrolled': isScrolled }">
    <div class="container">
      <div class="header-content">
        <router-link to="/" class="logo">
          <div class="logo-icon">
            <span class="logo-text">IT</span>
          </div>
          <div class="logo-name">
            <span class="logo-title">IT Альянс</span>
            <span class="logo-subtitle">Сервисный центр</span>
          </div>
        </router-link>

        <button class="mobile-menu-btn" @click="toggleMobileMenu">
          <span></span>
          <span></span>
          <span></span>
        </button>

        <nav class="nav" :class="{ 'nav-open': isMobileMenuOpen }">
          <router-link to="/" class="nav-link" @click="closeMobileMenu">Главная</router-link>
          <router-link to="/services" class="nav-link" @click="closeMobileMenu">Услуги</router-link>
          <router-link to="/about" class="nav-link" @click="closeMobileMenu">О нас</router-link>
          <router-link to="/reviews" class="nav-link" @click="closeMobileMenu">Отзывы</router-link>
          <router-link to="/contact" class="nav-link" @click="closeMobileMenu">Контакты</router-link>
          
          <div class="nav-auth">
            <template v-if="authStore.isAuthenticated">
              <router-link to="/orders" class="nav-link" @click="closeMobileMenu">
                Мои заказы
              </router-link>
              <router-link to="/profile" class="nav-link" @click="closeMobileMenu">
                Профиль
              </router-link>
              <button @click="handleLogout" class="btn btn-outline">Выход</button>
            </template>
            <template v-else>
              <router-link to="/login" class="btn btn-outline" @click="closeMobileMenu">
                Войти
              </router-link>
              <router-link to="/register" class="btn btn-primary" @click="closeMobileMenu">
                Регистрация
              </router-link>
            </template>
          </div>
        </nav>
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../../stores/auth'
import { useToast } from 'vue-toastification'

const router = useRouter()
const authStore = useAuthStore()
const toast = useToast()

const isScrolled = ref(false)
const isMobileMenuOpen = ref(false)

const handleScroll = () => {
  isScrolled.value = window.scrollY > 50
}

const toggleMobileMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value
}

const closeMobileMenu = () => {
  isMobileMenuOpen.value = false
}

const handleLogout = () => {
  authStore.logout()
  toast.success('Вы успешно вышли из системы')
  router.push('/')
  closeMobileMenu()
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
.header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background: white;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
  z-index: 1000;
  transition: all 0.3s ease;
}

.header-scrolled {
  box-shadow: 0 2px 20px rgba(0, 0, 0, 0.1);
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.header-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 80px;
}

.logo {
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
  transition: transform 0.3s ease;
}

.logo:hover {
  transform: scale(1.05);
}

.logo-icon {
  width: 50px;
  height: 50px;
  background: #2b6cb0;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 15px rgba(43, 108, 176, 0.3);
}

.logo-text {
  color: white;
  font-size: 24px;
  font-weight: 700;
}

.logo-name {
  display: flex;
  flex-direction: column;
}

.logo-title {
  font-size: 20px;
  font-weight: 700;
  color: #1a202c;
  line-height: 1.2;
}

.logo-subtitle {
  font-size: 12px;
  color: #718096;
  font-weight: 500;
}

.mobile-menu-btn {
  display: none;
  flex-direction: column;
  gap: 5px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 5px;
}

.mobile-menu-btn span {
  display: block;
  width: 25px;
  height: 3px;
  background: #1a202c;
  transition: all 0.3s ease;
}

.nav {
  display: flex;
  align-items: center;
  gap: 30px;
}

.nav-link {
  color: #4a5568;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.3s ease;
  position: relative;
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: -5px;
  left: 0;
  width: 0;
  height: 2px;
  background: #2b6cb0;
  transition: width 0.3s ease;
}

.nav-link:hover {
  color: #2b6cb0;
}

.nav-link:hover::after,
.nav-link.router-link-active::after {
  width: 100%;
}

.nav-link.router-link-active {
  color: #2b6cb0;
}

.nav-auth {
  display: flex;
  align-items: center;
  gap: 15px;
}

.btn {
  padding: 10px 24px;
  border-radius: 8px;
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

.btn-primary:hover {
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

@media (max-width: 968px) {
  .mobile-menu-btn {
    display: flex;
  }

  .nav {
    position: fixed;
    top: 80px;
    left: 0;
    right: 0;
    background: white;
    flex-direction: column;
    padding: 20px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    transform: translateX(-100%);
    transition: transform 0.3s ease;
    max-height: calc(100vh - 80px);
    overflow-y: auto;
  }

  .nav-open {
    transform: translateX(0);
  }

  .nav-auth {
    flex-direction: column;
    width: 100%;
  }

  .btn {
    width: 100%;
  }
}
</style>