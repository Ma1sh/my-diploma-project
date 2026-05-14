import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.services.models import ServiceCategory, Service
from apps.reviews.models import Review


print("🚀 Начинаем загрузку данных...")

# Удаляем старые данные (опционально)
print("Очистка старых данных...")
Service.objects.all().delete()
ServiceCategory.objects.all().delete()
Review.objects.filter(user__email='demo@example.com').delete()

# ==================== КАТЕГОРИИ ====================
print("\n📁 Создание категорий...")

categories_data = [
    {
        'name': 'Ремонт ноутбуков',
        'description': 'Профессиональный ремонт ноутбуков любых производителей. Диагностика, замена комплектующих, чистка от пыли.',
        'icon': 'laptop',
        'order': 1
    },
    {
        'name': 'Ремонт компьютеров',
        'description': 'Ремонт и модернизация настольных компьютеров. Сборка ПК под заказ.',
        'icon': 'desktop',
        'order': 2
    },
    {
        'name': 'Ремонт смартфонов',
        'description': 'Ремонт мобильных телефонов и планшетов. Замена дисплеев, батарей, разъемов.',
        'icon': 'smartphone',
        'order': 3
    },
    {
        'name': 'Замена комплектующих',
        'description': 'Апгрейд компьютеров и ноутбуков. Установка SSD, оперативной памяти, видеокарт.',
        'icon': 'hardware',
        'order': 4
    },
    {
        'name': 'Программное обеспечение',
        'description': 'Установка и настройка операционных систем, программ. Удаление вирусов.',
        'icon': 'software',
        'order': 5
    },
    {
        'name': 'Восстановление данных',
        'description': 'Восстановление потерянных данных с жестких дисков, флешек, карт памяти.',
        'icon': 'recovery',
        'order': 6
    },
]

categories = {}
for cat_data in categories_data:
    category, created = ServiceCategory.objects.get_or_create(
        name=cat_data['name'],
        defaults=cat_data
    )
    categories[cat_data['name']] = category
    print(f"✅ {cat_data['name']}")

# ==================== УСЛУГИ ====================
print("\n🔧 Создание услуг...")

services_data = [
    # Ремонт ноутбуков
    {
        'category': categories['Ремонт ноутбуков'],
        'name': 'Замена матрицы ноутбука',
        'description': 'Профессиональная замена битой или поврежденной матрицы ноутбука. Работаем с матрицами всех типов: TN, IPS, OLED. Используем только оригинальные комплектующие от проверенных поставщиков. Гарантия на работу 6 месяцев.',
        'price_from': 3500,
        'duration': '1-2 дня',
        'is_popular': True
    },
    {
        'category': categories['Ремонт ноутбуков'],
        'name': 'Чистка системы охлаждения',
        'description': 'Комплексная чистка ноутбука от пыли с заменой термопасты. Снижение температуры процессора и видеокарты на 15-25 градусов. Устранение перегрева и шума кулера.',
        'price_from': 1500,
        'duration': '2-3 часа',
        'is_popular': True
    },
    {
        'category': categories['Ремонт ноутбуков'],
        'name': 'Замена клавиатуры',
        'description': 'Замена неисправной или поврежденной клавиатуры на новую оригинальную. Работаем с ноутбуками всех производителей.',
        'price_from': 2000,
        'duration': '1 день',
        'is_popular': False
    },
    {
        'category': categories['Ремонт ноутбуков'],
        'name': 'Замена батареи ноутбука',
        'description': 'Замена изношенной аккумуляторной батареи. Оригинальные и качественные аналоги в наличии.',
        'price_from': 2500,
        'duration': '1 день',
        'is_popular': False
    },
    {
        'category': categories['Ремонт ноутбуков'],
        'name': 'Ремонт материнской платы',
        'description': 'Компонентный ремонт материнских плат ноутбуков. Замена чипов, конденсаторов, разъемов.',
        'price_from': 3000,
        'duration': '3-5 дней',
        'is_popular': False
    },

    # Ремонт компьютеров
    {
        'category': categories['Ремонт компьютеров'],
        'name': 'Диагностика компьютера',
        'description': 'Полная компьютерная диагностика всех компонентов системного блока. Тестирование процессора, памяти, жесткого диска, видеокарты.',
        'price_from': 500,
        'duration': '1-2 часа',
        'is_popular': True
    },
    {
        'category': categories['Ремонт компьютеров'],
        'name': 'Замена блока питания',
        'description': 'Установка нового блока питания необходимой мощности. Подбор оптимального БП под конфигурацию ПК.',
        'price_from': 1000,
        'duration': '1 час',
        'is_popular': False
    },
    {
        'category': categories['Ремонт компьютеров'],
        'name': 'Чистка компьютера от пыли',
        'description': 'Профессиональная чистка системного блока от пыли. Замена термопасты на процессоре и видеокарте.',
        'price_from': 1200,
        'duration': '1-2 часа',
        'is_popular': True
    },
    {
        'category': categories['Ремонт компьютеров'],
        'name': 'Сборка ПК на заказ',
        'description': 'Индивидуальная сборка компьютера под ваши задачи: игры, работа, монтаж видео. Подбор комплектующих, сборка, настройка.',
        'price_from': 3000,
        'duration': '1-2 дня',
        'is_popular': True
    },

    # Ремонт смартфонов
    {
        'category': categories['Ремонт смартфонов'],
        'name': 'Замена дисплея iPhone',
        'description': 'Замена разбитого или неисправного дисплейного модуля на iPhone любой модели. Оригинальные и качественные копии в наличии.',
        'price_from': 4500,
        'duration': '1-2 часа',
        'is_popular': True
    },
    {
        'category': categories['Ремонт смартфонов'],
        'name': 'Замена дисплея Samsung',
        'description': 'Замена дисплея на смартфонах Samsung Galaxy всех серий. Оригинальные AMOLED экраны.',
        'price_from': 3500,
        'duration': '1-2 часа',
        'is_popular': True
    },
    {
        'category': categories['Ремонт смартфонов'],
        'name': 'Замена аккумулятора',
        'description': 'Замена изношенной батареи на смартфоне любой модели. Оригинальные аккумуляторы с гарантией.',
        'price_from': 1500,
        'duration': '30 минут',
        'is_popular': True
    },
    {
        'category': categories['Ремонт смартфонов'],
        'name': 'Замена разъема зарядки',
        'description': 'Ремонт или замена неисправного разъема зарядки (microUSB, USB-C, Lightning).',
        'price_from': 1800,
        'duration': '1-2 часа',
        'is_popular': False
    },

    # Замена комплектующих
    {
        'category': categories['Замена комплектующих'],
        'name': 'Установка SSD накопителя',
        'description': 'Установка твердотельного накопителя SSD. Клонирование системы с HDD на SSD. Настройка для оптимальной работы.',
        'price_from': 1000,
        'duration': '2-3 часа',
        'is_popular': True
    },
    {
        'category': categories['Замена комплектующих'],
        'name': 'Увеличение оперативной памяти',
        'description': 'Установка дополнительных модулей оперативной памяти RAM. Подбор совместимых планок.',
        'price_from': 800,
        'duration': '30 минут',
        'is_popular': True
    },
    {
        'category': categories['Замена комплектующих'],
        'name': 'Замена видеокарты',
        'description': 'Установка новой видеокарты. Подбор совместимой модели, установка драйверов.',
        'price_from': 1200,
        'duration': '1 час',
        'is_popular': False
    },
    {
        'category': categories['Замена комплектующих'],
        'name': 'Замена процессора',
        'description': 'Замена процессора на более мощный. Подбор совместимого CPU, замена термопасты.',
        'price_from': 1500,
        'duration': '1-2 часа',
        'is_popular': False
    },

    # Программное обеспечение
    {
        'category': categories['Программное обеспечение'],
        'name': 'Установка Windows',
        'description': 'Установка операционной системы Windows (10, 11). Установка драйверов, настройка системы.',
        'price_from': 1000,
        'duration': '2-3 часа',
        'is_popular': True
    },
    {
        'category': categories['Программное обеспечение'],
        'name': 'Удаление вирусов',
        'description': 'Комплексная проверка и очистка системы от вирусов, троянов, рекламного ПО. Установка антивируса.',
        'price_from': 800,
        'duration': '1-2 часа',
        'is_popular': True
    },
    {
        'category': categories['Программное обеспечение'],
        'name': 'Установка программ',
        'description': 'Установка необходимых программ и приложений. Настройка офисного пакета, браузеров, мессенджеров.',
        'price_from': 500,
        'duration': '1 час',
        'is_popular': False
    },
    {
        'category': categories['Программное обеспечение'],
        'name': 'Оптимизация системы',
        'description': 'Ускорение работы компьютера. Очистка от мусора, настройка автозагрузки, дефрагментация.',
        'price_from': 700,
        'duration': '1-2 часа',
        'is_popular': False
    },

    # Восстановление данных
    {
        'category': categories['Восстановление данных'],
        'name': 'Восстановление данных с HDD',
        'description': 'Восстановление удаленных или потерянных файлов с жесткого диска. Работаем с любыми повреждениями.',
        'price_from': 3000,
        'duration': '1-3 дня',
        'is_popular': False
    },
    {
        'category': categories['Восстановление данных'],
        'name': 'Восстановление данных с SSD',
        'description': 'Восстановление информации с твердотельных накопителей SSD.',
        'price_from': 3500,
        'duration': '2-4 дня',
        'is_popular': False
    },
    {
        'category': categories['Восстановление данных'],
        'name': 'Восстановление данных с флешки',
        'description': 'Восстановление файлов с USB накопителей и карт памяти.',
        'price_from': 1500,
        'duration': '1-2 дня',
        'is_popular': False
    },
]

for service_data in services_data:
    service, created = Service.objects.get_or_create(
        name=service_data['name'],
        defaults=service_data
    )
    status = "✅" if created else "⏭️"
    print(f"{status} {service_data['name']} - {service_data['price_from']} ₽")

