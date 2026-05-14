import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/HomePage.vue')
  },
  {
    path: '/services',
    name: 'Services',
    component: () => import('@/views/ServicesPage.vue')
  },
  {
    path: '/services/:id',
    name: 'ServiceDetail',
    component: () => import('@/views/ServiceDetailPage.vue')
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('@/views/AboutPage.vue')
  },
  {
    path: '/reviews',
    name: 'Reviews',
    component: () => import('@/views/ReviewsPage.vue')
  },
  {
    path: '/contact',
    name: 'Contact',
    component: () => import('@/views/ContactPage.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/auth/LoginPage.vue'),
    meta: { guest: true }
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import('@/views/auth/RegisterPage.vue'),
    meta: { guest: true }
  },
  {
    path: '/profile',
    name: 'Profile',
    component: () => import('@/views/profile/ProfilePage.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/orders',
    name: 'Orders',
    component: () => import('@/views/orders/OrdersPage.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/orders/create',
    name: 'CreateOrder',
    component: () => import('@/views/orders/CreateOrderPage.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/orders/:id',
    name: 'OrderDetail',
    component: () => import('@/views/orders/OrderDetailPage.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('@/views/NotFoundPage.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  }
})

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore()
  
  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next({ name: 'Login', query: { redirect: to.fullPath } })
  } else if (to.meta.guest && authStore.isAuthenticated) {
    next({ name: 'Home' })
  } else {
    next()
  }
})

export default router