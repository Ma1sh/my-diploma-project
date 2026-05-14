<template>
  <div class="about-page">
    <div class="page-header">
      <div class="container">
        <h1 class="page-title">О нас</h1>
        <p class="page-description">IT Альянс - надежный партнер в мире технологий</p>
      </div>
    </div>

    <div class="container">
      <!-- Company Info -->
      <section class="company-info">
        <div class="info-content">
          <h2>Профессиональный сервисный центр</h2>
          <p>
            IT Альянс - это современный сервисный центр, специализирующийся на ремонте и 
            обслуживании компьютерной техники и электроники. Мы работаем на рынке более 
            10 лет и за это время заслужили доверие тысяч клиентов.
          </p>
          <p>
            Наша команда состоит из высококвалифицированных специалистов, которые постоянно 
            повышают свою квалификацию и следят за последними тенденциями в мире технологий.
          </p>
        </div>
        <div class="info-image">
          <div class="image-placeholder">
            <span class="placeholder-icon">🏢</span>
          </div>
        </div>
      </section>

      <!-- Our Advantages -->
      <section class="advantages-section">
        <h2 class="section-title">Наши преимущества</h2>
        
        <div class="advantages-grid">
          <div class="advantage-card">
            <div class="advantage-icon">👨‍💻</div>
            <h3>Опытные специалисты</h3>
            <p>Наши мастера имеют сертификаты и многолетний опыт работы</p>
          </div>

          <div class="advantage-card">
            <div class="advantage-icon">🛠️</div>
            <h3>Современное оборудование</h3>
            <p>Используем профессиональное оборудование для диагностики и ремонта</p>
          </div>

          <div class="advantage-card">
            <div class="advantage-icon">✅</div>
            <h3>Гарантия качества</h3>
            <p>Предоставляем официальную гарантию на все виды работ</p>
          </div>

          <div class="advantage-card">
            <div class="advantage-icon">💎</div>
            <h3>Оригинальные запчасти</h3>
            <p>Работаем только с проверенными поставщиками комплектующих</p>
          </div>

          <div class="advantage-card">
            <div class="advantage-icon">⚡</div>
            <h3>Быстрый ремонт</h3>
            <p>Большинство ремонтов выполняем в течение 1-3 дней</p>
          </div>

          <div class="advantage-card">
            <div class="advantage-icon">💰</div>
            <h3>Доступные цены</h3>
            <p>Честные цены без скрытых платежей и наценок</p>
          </div>
        </div>
      </section>

      <!-- Statistics -->
      <section class="statistics-section">
        <h2 class="section-title">Цифры, которые говорят сами за себя</h2>
        
        <div class="stats-grid">
          <div class="stat-item">
            <div class="stat-number">10+</div>
            <div class="stat-label">лет на рынке</div>
          </div>
          <div class="stat-item">
            <div class="stat-number">5000+</div>
            <div class="stat-label">выполненных заказов</div>
          </div>
          <div class="stat-item">
            <div class="stat-number">98%</div>
            <div class="stat-label">довольных клиентов</div>
          </div>
          <div class="stat-item">
            <div class="stat-number">50+</div>
            <div class="stat-label">видов услуг</div>
          </div>
        </div>
      </section>

      <!-- Team -->
      <section class="team-section">
        <h2 class="section-title">Наша команда</h2>
        
        <div class="team-grid">
          <div class="team-member">
            <div class="member-avatar">👨‍💼</div>
            <h3>Иванов Иван</h3>
            <p class="member-role">Руководитель сервисного центра</p>
            <p class="member-description">
              15 лет опыта в IT-сфере. Сертифицированный специалист по ремонту техники Apple и PC.
            </p>
          </div>

          <div class="team-member">
            <div class="member-avatar">👨‍🔧</div>
            <h3>Петров Петр</h3>
            <p class="member-role">Старший мастер</p>
            <p class="member-description">
              Специализация на ремонте материнских плат и восстановлении данных. 12 лет опыта.
            </p>
          </div>

          <div class="team-member">
            <div class="member-avatar">👩‍💻</div>
            <h3>Сидорова Анна</h3>
            <p class="member-role">Инженер-диагност</p>
            <p class="member-description">
              Эксперт по диагностике и ремонту ноутбуков. Сертифицированный специалист HP и Dell.
            </p>
          </div>
        </div>
      </section>

      <!-- CTA -->
      <section class="cta-section">
        <div class="cta-content">
          <h2>Готовы доверить нам свою технику?</h2>
          <p>Свяжитесь с нами прямо сейчас и получите бесплатную консультацию</p>
          <div class="cta-buttons">
            <router-link to="/orders/create" class="btn btn-primary btn-large">
              Оставить заявку
            </router-link>
            <router-link to="/contact" class="btn btn-outline btn-large">
              Контакты
            </router-link>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

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

section {
  margin-bottom: 100px;
}

.section-title {
  font-size: 36px;
  font-weight: 700;
  color: #1a202c;
  text-align: center;
  margin-bottom: 50px;
}

/* Company Info */
.company-info {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
  align-items: center;
}

.info-content h2 {
  font-size: 32px;
  font-weight: 700;
  color: #1a202c;
  margin-bottom: 25px;
}

.info-content p {
  color: #4a5568;
  line-height: 1.8;
  font-size: 17px;
  margin-bottom: 20px;
}

.info-image {
  display: flex;
  align-items: center;
  justify-content: center;
}

.image-placeholder {
  width: 100%;
  aspect-ratio: 1;
  background: #2b6cb0;
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);
}

.placeholder-icon {
  font-size: 150px;
}

/* Advantages */
.advantages-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 30px;
}

.advantage-card {
  background: white;
  padding: 40px;
  border-radius: 15px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  text-align: center;
  transition: all 0.3s ease;
}

.advantage-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
}

.advantage-icon {
  font-size: 60px;
  margin-bottom: 20px;
}

.advantage-card h3 {
  font-size: 22px;
  font-weight: 600;
  color: #1a202c;
  margin-bottom: 15px;
}

.advantage-card p {
  color: #718096;
  line-height: 1.6;
}

/* Statistics */
.statistics-section {
  background: #2b6cb0;
  padding: 80px 40px;
  border-radius: 20px;
  color: white;
}

.statistics-section .section-title {
  color: white;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 40px;
}

.stat-item {
  text-align: center;
}

.stat-number {
  font-size: 56px;
  font-weight: 700;
  margin-bottom: 10px;
}

.stat-label {
  font-size: 18px;
  opacity: 0.95;
}

/* Team */
.team-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 40px;
}

.team-member {
  background: white;
  padding: 40px;
  border-radius: 15px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  text-align: center;
  transition: all 0.3s ease;
}

.team-member:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
}

.member-avatar {
  width: 120px;
  height: 120px;
  margin: 0 auto 20px;
  background: #2b6cb0;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 60px;
}

.team-member h3 {
  font-size: 24px;
  font-weight: 700;
  color: #1a202c;
  margin-bottom: 5px;
}

.member-role {
  color: #2b6cb0;
  font-weight: 600;
  margin-bottom: 15px;
  font-size: 16px;
}

.member-description {
  color: #718096;
  line-height: 1.6;
}

/* CTA */
.cta-section {
  background: #f7fafc;
  padding: 80px 40px;
  border-radius: 20px;
  text-align: center;
}

.cta-content h2 {
  font-size: 36px;
  font-weight: 700;
  color: #1a202c;
  margin-bottom: 15px;
}

.cta-content p {
  font-size: 18px;
  color: #718096;
  margin-bottom: 30px;
}

.cta-buttons {
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

.btn-large {
  padding: 18px 48px;
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

@media (max-width: 968px) {
  .company-info {
    grid-template-columns: 1fr;
  }

  .page-title {
    font-size: 36px;
  }

  .section-title {
    font-size: 28px;
  }

  .cta-buttons {
    flex-direction: column;
  }

  .btn {
    width: 100%;
  }

  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 640px) {
  .page-title {
    font-size: 28px;
  }

  .advantages-grid,
  .team-grid {
    grid-template-columns: 1fr;
  }

  .stats-grid {
    grid-template-columns: 1fr;
  }

  .stat-number {
    font-size: 42px;
  }
}
</style>