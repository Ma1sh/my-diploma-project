<template>
  <div class="not-found-page">
    <div class="not-found-content">
      <div class="error-code">404</div>
      <h1 class="error-title">Страница не найдена</h1>
      <p class="error-description">
        К сожалению, запрашиваемая вами страница не существует или была перемещена
      </p>
      <div class="error-actions">
        <router-link to="/" class="btn btn-primary">
          На главную
        </router-link>
        <router-link to="/services" class="btn btn-outline">
          Наши услуги
        </router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>
.not-found-page {
  min-height: 80vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
}

.not-found-content {
  text-align: center;
  max-width: 600px;
}

.error-code {
  font-size: 150px;
  font-weight: 700;
  color: #2b6cb0;
  line-height: 1;
  margin-bottom: 20px;
}

.error-title {
  font-size: 42px;
  font-weight: 700;
  color: #1a202c;
  margin-bottom: 20px;
}

.error-description {
  font-size: 18px;
  color: #718096;
  margin-bottom: 40px;
  line-height: 1.6;
}

.error-actions {
  display: flex;
  gap: 15px;
  justify-content: center;
}

.btn {
  padding: 16px 40px;
  border-radius: 12px;
  font-weight: 600;
  text-decoration: none;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 18px;
  display: inline-block;
  text-align: center;
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
  color: #2b6cb0;
  border: 2px solid #2b6cb0;
}

.btn-outline:hover {
  background: #2b6cb0;
  color: white;
}

@media (max-width: 640px) {
  .error-code {
    font-size: 100px;
  }

  .error-title {
    font-size: 32px;
  }

  .error-actions {
    flex-direction: column;
  }

  .btn {
    width: 100%;
  }
}
</style>