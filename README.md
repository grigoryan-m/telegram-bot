# 🤖 Loyalty Telegram Bot

Telegram-бот для программы лояльности с поддержкой трёх языков (EN / RU / TH),
интеграцией с Odoo CRM и AI-ассистентом.

## Возможности

- 🌐 Мультиязычность: English, Русский, ภาษาไทย
- 🎁 Регистрация в программе лояльности (OTP + Odoo CRM)
- 📍 Поиск ближайших магазинов (геолокация или регион, радиус 3 км)
- 💬 Чат с AI-ассистентом + передача менеджеру
- 📊 Аналитика всех ключевых событий (локально + Google Analytics 4)
- 📲 Переход в соцсети с трекингом

---

## Быстрый старт

### 1. Клонируй репозиторий

```bash
git clone https://github.com/your-org/loyalty-bot.git
cd loyalty-bot
```

### 2. Создай `.env` файл

```bash
cp .env.example .env
nano .env  # заполни все переменные
```

### 3. Запусти через Docker (рекомендуется)

```bash
docker compose up -d
docker compose logs -f  # смотреть логи
```

### Или локально без Docker

```bash
pip install -r requirements.txt
python bot.py
```

---

## Деплой

### VPS (Ubuntu/Debian) через systemd

```bash
# 1. Скопировать файлы
scp -r . user@your-server:/opt/loyalty_bot

# 2. Создать сервис
sudo nano /etc/systemd/system/loyalty_bot.service
```

```ini
[Unit]
Description=Loyalty Telegram Bot
After=network.target

[Service]
WorkingDirectory=/opt/loyalty_bot
ExecStart=/usr/bin/python3 bot.py
Restart=always
RestartSec=5
EnvironmentFile=/opt/loyalty_bot/.env
User=www-data

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable loyalty_bot
sudo systemctl start loyalty_bot
sudo systemctl status loyalty_bot
```

### Railway / Render (без своего сервера)

1. Загрузи код на GitHub
2. Зайди на railway.app или render.com
3. Подключи репозиторий → Add Service → Deploy from GitHub
4. В разделе Variables добавь все переменные из `.env.example`
5. Start command: `python bot.py`

---

## Структура проекта

```
loyalty_bot/
├── bot.py                  # точка входа
├── config.py               # настройки из .env
├── states.py               # FSM-состояния
├── handlers/
│   ├── start.py            # /start, выбор языка, главное меню
│   ├── loyalty.py          # регистрация (телефон → OTP → возраст → страна)
│   ├── stores.py           # поиск магазинов
│   ├── manager.py          # AI-чат + передача менеджеру
│   ├── about.py            # О компании
│   └── socials.py          # Соцсети
├── locales/
│   └── texts.py            # все тексты EN / RU / TH
├── utils/
│   ├── keyboards.py        # все клавиатуры
│   ├── odoo.py             # интеграция с Odoo CRM
│   ├── otp.py              # OTP генерация и проверка
│   ├── ai.py               # Claude AI-ассистент
│   ├── stores.py           # поиск магазинов (Haversine, 3 км)
│   ├── user_data.py        # хранение языка пользователя
│   └── analytics.py        # трекинг событий
├── data/
│   └── stores.json         # база магазинов
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env.example
```

---

## Что нужно доделать

| Задача | Файл |
|--------|------|
| Заполнить базу магазинов | `data/stores.json` |
| Подключить SMS-провайдер (Twilio и т.д.) | `utils/otp.py` → `send_otp_sms()` |
| Проверить поля Odoo | `utils/odoo.py` (x_age, x_loyalty_id и т.д.) |
| Вписать ссылки на соцсети и рецепты | `.env` → SOCIALS_URL, RECIPE_URL |
| Обновить текст "О компании" | `locales/texts.py` → ключ `about_text` |
| Настроить часовой пояс менеджеров | `handlers/manager.py` → `TZ_OFFSET` |
| Регионы для ручного выбора | `utils/keyboards.py` → `regions_keyboard()` |

---

## Аналитика

Все события пишутся в `data/analytics.jsonl` (одна строка JSON = одно событие).

Отслеживаемые события:
- `bot_started` — первый запуск
- `language_selected` — выбор языка
- `menu_opened` — открытие главного меню
- `loyalty_started` — начало регистрации
- `loyalty_completed` — успешная регистрация
- `loyalty_error` — ошибка CRM
- `store_search_geo` — поиск по геолокации
- `store_search_region` — поиск по региону
- `manager_started` — открытие чата
- `manager_transferred` — передача менеджеру
- `manager_message_left` — оставлено сообщение вне рабочего времени
- `socials_opened` — открытие соцсетей
- `about_opened` — открытие раздела "О компании"

Для Google Analytics 4 укажи `GA4_MEASUREMENT_ID` и `GA4_API_SECRET` в `.env`.
