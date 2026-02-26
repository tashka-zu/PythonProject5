# Docker project

Проект для онлайн-обучения с использованием Django, PostgreSQL, Redis, Celery и Docker.

## Требования

- Docker
- Docker Compose

## Установка и запуск

1. **Клонируйте репозиторий:**
   ```bash
   git clone <ссылка_на_репозиторий>
   cd <название_проекта>

2. **Создайте файл .env по шаблону:**
- Скопируйте .env.example в .env:
   ```bash
   cp .env.example .env
- Заполните переменные окружения (см. .env.example).

3. **Запустите проект с помощью Docker Compose:**
   ```bash
   docker-compose up --build

4. **Примените миграции (если нужно):**
   ```bash
   docker-compose exec backend python manage.py migrate


### Проверка работоспособности
```markdown
- **Бэкенд:** Откройте [http://localhost:8000](http://localhost:8000) в браузере.
- **База данных:** Подключитесь к PostgreSQL на `localhost:5432` с данными из `.env`.
- **Redis:** Проверьте подключение к `localhost:6379`.
- **Celery:** Логи доступны в консоли после запуска `docker-compose up`.