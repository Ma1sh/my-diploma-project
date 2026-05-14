<template>
  <div class="services-page">
    <div class="page-header">
      <div class="container">
        <h1 class="page-title">Наши услуги</h1>
        <p class="page-description">
          Полный спектр услуг по ремонту и обслуживанию компьютерной техники
        </p>
      </div>
    </div>

    <div class="container">
      <div class="services-content">
        <!-- Filters -->
        <aside class="filters-sidebar">
          <div class="filter-section">
            <h3 class="filter-title">Категории</h3>
            <div class="filter-list">
              <label class="filter-item">
                <input 
                  type="radio" 
                  name="category" 
                  value="" 
                  v-model="filters.category"
                  @change="loadServices"
                >
                <span>Все категории</span>
              </label>
              <label 
                v-for="category in categories" 
                :key="category.id" 
                class="filter-item"
              >
                <input 
                  type="radio" 
                  name="category" 
                  :value="category.id"
                  v-model="filters.category"
                  @change="loadServices"
                >
                <span>{{ category.name }}</span>
                <span class="filter-count">{{ category.services_count }}</span>
              </label>
            </div>
          </div>

          <div class="filter-section">
            <h3 class="filter-title">Фильтры</h3>
            <label class="filter-checkbox">
              <input 
                type="checkbox" 
                v-model="filters.is_popular"
                @change="loadServices"
              >
              <span>Только популярные</span>
            </label>
          </div>

          <div class="filter-section">
            <h3 class="filter-title">Поиск</h3>
            <input 
              type="text" 
              class="search-input"
              placeholder="Поиск услуг..."
              v-model="filters.search"
              @input="debouncedSearch"
            >
          </div>
        </aside>

        <!-- Services List -->
        <div class="services-main">
          <div class="services-header">
            <p class="services-count">
              Найдено услуг: {{ totalServices }}
            </p>
            <select 
              class="sort-select" 
              v-model="filters.ordering"
              @change="loadServices"
            >
              <option value="">По умолчанию</option>
              <option value="price_from">Сначала дешевые</option>
              <option value="-price_from">Сначала дорогие</option>
              <option value="-created_at">Сначала новые</option>
            </select>
          </div>

          <div v-if="loading" class="loading">
            <div class="spinner"></div>
            <p>Загрузка услуг...</p>
          </div>

          <div v-else-if="services.length" class="services-grid">
            <div 
              v-for="service in services" 
              :key="service.id" 
              class="service-card"
              @click="goToService(service.id)"
            >
              <div class="service-badge" v-if="service.is_popular">
                ⭐ Популярное
              </div>
              <div class="service-image">
                <img 
                  v-if="service.image" 
                  :src="service.image" 
                  :alt="service.name"
                >
                <div v-else class="service-placeholder">🔧</div>
              </div>
              <div class="service-info">
                <span class="service-category">{{ service.category_name }}</span>
                <h3 class="service-name">{{ service.name }}</h3>
                <p class="service-price">от {{ service.price_from }} ₽</p>
                <p class="service-duration">⏱ {{ service.duration }}</p>
                <button class="btn btn-primary btn-block">Подробнее</button>
              </div>
            </div>
          </div>

          <div v-else class="no-results">
            <div class="no-results-icon">🔍</div>
            <h3>Услуги не найдены</h3>
            <p>Попробуйте изменить параметры поиска</p>
          </div>

          <!-- Pagination -->
          <div v-if="totalPages > 1" class="pagination">
            <button 
              class="pagination-btn"
              :disabled="currentPage === 1"
              @click="changePage(currentPage - 1)"
            >
              ← Назад
            </button>
            
            <div class="pagination-pages">
              <button
                v-for="page in displayedPages"
                :key="page"
                class="pagination-page"
                :class="{ active: page === currentPage }"
                @click="changePage(page)"
              >
                {{ page }}
              </button>
            </div>

            <button 
              class="pagination-btn"
              :disabled="currentPage === totalPages"
              @click="changePage(currentPage + 1)"
            >
              Вперед →
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import servicesApi from '@/services/servicesApi'

const router = useRouter()

const categories = ref([])
const services = ref([])
const loading = ref(false)
const currentPage = ref(1)
const totalServices = ref(0)
const totalPages = ref(1)

const filters = ref({
  category: '',
  is_popular: false,
  search: '',
  ordering: ''
})

let searchTimeout = null

const displayedPages = computed(() => {
  const pages = []
  const maxVisible = 5
  let start = Math.max(1, currentPage.value - Math.floor(maxVisible / 2))
  let end = Math.min(totalPages.value, start + maxVisible - 1)
  
  if (end - start < maxVisible - 1) {
    start = Math.max(1, end - maxVisible + 1)
  }
  
  for (let i = start; i <= end; i++) {
    pages.push(i)
  }
  
  return pages
})

const loadCategories = async () => {
  try {
    const response = await servicesApi.getCategories()
    categories.value = response.data.results
  } catch (error) {
    console.error('Error loading categories:', error)
  }
}

const loadServices = async () => {
  loading.value = true
  try {
    const params = {
      page: currentPage.value,
      ...filters.value
    }
    
    // Remove empty filters
    Object.keys(params).forEach(key => {
      if (params[key] === '' || params[key] === false) {
        delete params[key]
      }
    })
    
    const response = await servicesApi.getServices(params)
    services.value = response.data.results
    totalServices.value = response.data.count
    totalPages.value = Math.ceil(response.data.count / 10)
  } catch (error) {
    console.error('Error loading services:', error)
  } finally {
    loading.value = false
  }
}

const debouncedSearch = () => {
  clearTimeout(searchTimeout)
  searchTimeout = setTimeout(() => {
    currentPage.value = 1
    loadServices()
  }, 500)
}

const changePage = (page) => {
  currentPage.value = page
  loadServices()
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

const goToService = (id) => {
  router.push(`/services/${id}`)
}

onMounted(() => {
  loadCategories()
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
}

.services-content {
  display: grid;
  grid-template-columns: 280px 1fr;
  gap: 40px;
  margin-bottom: 60px;
}

/* Filters */
.filters-sidebar {
  position: sticky;
  top: 100px;
  height: fit-content;
}

.filter-section {
  background: white;
  padding: 25px;
  border-radius: 15px;
  box-shadow: 0 2px 15px rgba(0, 0, 0, 0.08);
  margin-bottom: 20px;
}

.filter-title {
  font-size: 18px;
  font-weight: 600;
  color: #1a202c;
  margin-bottom: 15px;
}

.filter-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.filter-item {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  padding: 8px;
  border-radius: 8px;
  transition: background 0.2s;
}

.filter-item:hover {
  background: #f7fafc;
}

.filter-item input[type="radio"] {
  cursor: pointer;
}

.filter-item span {
  flex: 1;
  color: #4a5568;
}

.filter-count {
  background: #e2e8f0;
  color: #4a5568;
  padding: 2px 8px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 600;
}

.filter-checkbox {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  padding: 8px;
}

.filter-checkbox input[type="checkbox"] {
  cursor: pointer;
  width: 18px;
  height: 18px;
}

.search-input {
  width: 100%;
  padding: 12px;
  border: 2px solid #e2e8f0;
  border-radius: 8px;
  font-size: 14px;
  transition: border-color 0.3s;
}

.search-input:focus {
  outline: none;
  border-color: #667eea;
}

/* Services Main */
.services-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
  padding: 20px;
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}

.services-count {
  font-weight: 600;
  color: #4a5568;
}

.sort-select {
  padding: 10px 15px;
  border: 2px solid #e2e8f0;
  border-radius: 8px;
  font-size: 14px;
  cursor: pointer;
  background: white;
}

.sort-select:focus {
  outline: none;
  border-color: #667eea;
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
  position: relative;
}

.service-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
}

.service-badge {
  position: absolute;
  top: 15px;
  right: 15px;
  background: #fbbf24;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  z-index: 1;
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

.service-category {
  display: inline-block;
  background: #e2e8f0;
  color: #4a5568;
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 600;
  margin-bottom: 10px;
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
  color: #667eea;
  margin-bottom: 8px;
}

.service-duration {
  color: #718096;
  font-size: 14px;
  margin-bottom: 15px;
}

.btn {
  padding: 12px 24px;
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
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
}

.btn-block {
  width: 100%;
}

/* Loading */
.loading {
  text-align: center;
  padding: 60px 20px;
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

/* No Results */
.no-results {
  text-align: center;
  padding: 80px 20px;
}

.no-results-icon {
  font-size: 80px;
  margin-bottom: 20px;
}

.no-results h3 {
  font-size: 24px;
  color: #1a202c;
  margin-bottom: 10px;
}

.no-results p {
  color: #718096;
}

/* Pagination */
.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
  margin-top: 40px;
}

.pagination-btn {
  padding: 10px 20px;
  background: white;
  border: 2px solid #e2e8f0;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
  color: #4a5568;
  transition: all 0.3s;
}

.pagination-btn:hover:not(:disabled) {
  border-color: #667eea;
  color: #667eea;
}

.pagination-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.pagination-pages {
  display: flex;
  gap: 5px;
}

.pagination-page {
  width: 40px;
  height: 40px;
  background: white;
  border: 2px solid #e2e8f0;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
  color: #4a5568;
  transition: all 0.3s;
}

.pagination-page:hover {
  border-color: #667eea;
  color: #667eea;
}

.pagination-page.active {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-color: transparent;
}

/* Responsive */
@media (max-width: 968px) {
  .services-content {
    grid-template-columns: 1fr;
  }

  .filters-sidebar {
    position: static;
  }

  .page-title {
    font-size: 36px;
  }

  .services-header {
    flex-direction: column;
    gap: 15px;
    align-items: stretch;
  }

  .sort-select {
    width: 100%;
  }
}

@media (max-width: 640px) {
  .page-title {
    font-size: 28px;
  }

  .services-grid {
    grid-template-columns: 1fr;
  }

  .pagination {
    flex-wrap: wrap;
  }
}
</style>