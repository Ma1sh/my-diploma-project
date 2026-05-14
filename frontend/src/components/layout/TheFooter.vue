<template>
  <footer class="footer">
    <div class="container">
      <div class="footer-content">
        <div class="footer-section">
          <div class="footer-logo">
            <div class="logo-icon">
              <span class="logo-text">IT</span>
            </div>
            <div class="logo-name">
              <span class="logo-title">IT Альянс</span>
              <span class="logo-subtitle">Сервисный центр</span>
            </div>
          </div>
          <p class="footer-description">
            Профессиональный ремонт компьютерной техники и электроники. 
            Гарантия качества и доступные цены.
          </p>
        </div>

        <div class="footer-section">
          <h3 class="footer-title">Навигация</h3>
          <nav class="footer-nav">
            <router-link to="/" class="footer-link">Главная</router-link>
            <router-link to="/services" class="footer-link">Услуги</router-link>
            <router-link to="/about" class="footer-link">О нас</router-link>
            <router-link to="/reviews" class="footer-link">Отзывы</router-link>
            <router-link to="/contact" class="footer-link">Контакты</router-link>
          </nav>
        </div>

        <div class="footer-section">
          <h3 class="footer-title">Контакты</h3>
          <div class="footer-contacts">
            <a href="tel:+79001234567" class="footer-contact">
              <span class="contact-icon">📞</span>
              +7 (900) 123-45-67
            </a>
            <a href="mailto:info@it-alliance.ru" class="footer-contact">
              <span class="contact-icon">✉️</span>
              info@it-alliance.ru
            </a>
            <div class="footer-contact">
              <span class="contact-icon">📍</span>
              г. Москва, ул. Примерная, д. 1
            </div>
            <div class="footer-contact">
              <span class="contact-icon">🕐</span>
              Пн-Пт: 9:00 - 20:00<br>
              Сб-Вс: 10:00 - 18:00
            </div>
          </div>
        </div>

        <div class="footer-section">
          <h3 class="footer-title">Мы в соцсетях</h3>
          <div class="footer-social">
            <a href="#" class="social-link" aria-label="VK">VK</a>
            <a href="#" class="social-link" aria-label="Telegram">TG</a>
            <a href="#" class="social-link" aria-label="WhatsApp">WA</a>
          </div>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; 2024 IT Альянс. Все права защищены.</p>
        <p>Разработано для преддипломной практики</p>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  background: #1a202c;
  color: #a0aec0;
  padding: 60px 0 30px;
  margin-top: 80px;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.footer-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 40px;
  margin-bottom: 40px;
}

.footer-section {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.footer-logo {
  display: flex;
  align-items: center;
  gap: 12px;
}

.logo-icon {
  width: 45px;
  height: 45px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
}

.logo-text {
  color: white;
  font-size: 20px;
  font-weight: 700;
}

.logo-name {
  display: flex;
  flex-direction: column;
}

.logo-title {
  font-size: 18px;
  font-weight: 700;
  color: white;
  line-height: 1.2;
}

.logo-subtitle {
  font-size: 12px;
  color: #a0aec0;
  font-weight: 500;
}

.footer-description {
  line-height: 1.6;
  font-size: 14px;
}

.footer-title {
  color: white;
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 5px;
}

.footer-nav {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.footer-link {
  color: #a0aec0;
  text-decoration: none;
  transition: color 0.3s ease;
  font-size: 14px;
}

.footer-link:hover {
  color: #667eea;
}

.footer-contacts {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.footer-contact {
  color: #a0aec0;
  text-decoration: none;
  display: flex;
  align-items: flex-start;
  gap: 10px;
  transition: color 0.3s ease;
  font-size: 14px;
  line-height: 1.6;
}

.footer-contact:hover {
  color: #667eea;
}

.contact-icon {
  font-size: 18px;
}

.footer-social {
  display: flex;
  gap: 15px;
}

.social-link {
  width: 40px;
  height: 40px;
  border-radius: 8px;
  background: #2d3748;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  font-weight: 600;
  font-size: 12px;
  transition: all 0.3s ease;
}

.social-link:hover {
  background: #667eea;
  transform: translateY(-3px);
}

.footer-bottom {
  padding-top: 30px;
  border-top: 1px solid #2d3748;
  text-align: center;
  font-size: 14px;
}

.footer-bottom p {
  margin: 5px 0;
}

@media (max-width: 768px) {
  .footer-content {
    grid-template-columns: 1fr;
    gap: 30px;
  }
}
</style>