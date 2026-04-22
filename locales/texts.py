TEXTS = {
    "en": {
        "welcome": (
            "👋 Welcome! Please choose your language:"
        ),
        "lang_set": "✅ Language set to English.",
        "main_menu": "🏠 *Main Menu*\nChoose an option below:",
        "btn_stores": "📍 Find nearest store",
        "btn_loyalty": "🎁 Get loyalty card",
        "btn_manager": "💬 Contact manager",
        "btn_about": "ℹ️ About us",
        "btn_socials": "📲 Our socials",
        "btn_back": "⬅️ Back",
        "btn_main_menu": "🏠 Main menu",
        "btn_change_lang": "🌐 Change language",

        "loading": "⏳ Processing...",


        "loyalty_hint": "Get your loyalty card in 30 seconds and receive a bonus 🎁",

        # Reminders
        "loyalty_reminder": "It takes 30 seconds to create loyalty card for bonuses in every store",
        "after_phone_reminder": "Finish registration to activate your bonus",
        "loyalty5m_reminder": "Without registration you can’t get rewards in stores",
        # Loyalty flow
        "loyalty_start": (
            "🎁 *Get access to bonuses, discounts and faster service*\n\n"
            "Please enter your phone number in international format:\n"
            "Example: +66812345678"
        ),
        "loyalty_phone_invalid": "❌ Invalid phone number. Please use international format, e.g. +66812345678",
        "loyalty_otp_sent": "📱 OTP code sent to *{phone}*\n\nPlease enter the 6-digit code:",
        "loyalty_otp_invalid": "❌ Invalid OTP code. Please try again or press /start to restart.",
        "loyalty_otp_attempts": "❌ Too many failed attempts. Please start over with /start",
        "loyalty_ask_age": "✅ Phone verified!\n\nPlease enter your age:",
        "loyalty_age_invalid": "❌ Please enter a valid age (1-120):",
        "loyalty_ask_country": "🌍 Please enter your country (e.g. Thailand, Russia, USA):",
        "loyalty_success": (
            "🎉 *Registration successful!*\n\n"
            "👤 Client ID: `{client_id}`\n"
            "📱 Phone: {phone}\n\n"
            "🏷 Your loyalty card barcode: `{barcode}`\n\n"
            "Show this code at any of our stores to earn points!"
        ),
        "loyalty_already_exists": (
            "✅ *You are already registered!*\n\n"
            "👤 Client ID: `{client_id}`\n"
            "🏷 Barcode: `{barcode}`\n\n"
            "Your data has been updated."
        ),
        "loyalty_crm_error": "⚠️ A technical error occurred. Please try again later or contact our manager.",

        # New keys for WeedeN REST API flow
        "loyalty_ask_name": "✅ Phone verified!\n\nPlease enter your full name:",
        "loyalty_name_invalid": "❌ Please enter your real full name (at least 2 characters):",
        "loyalty_ask_tourist": "🌍 Are you visiting as a tourist?",
        "loyalty_ask_thai_citizen": "🇹🇭 Are you a Thai citizen?",
        "btn_yes": "✅ Yes",
        "btn_no": "❌ No",
        # Fallback templates when API doesn't return a formatted message
        "loyalty_success": (
            "🎉 *Registration successful!*\n\n"
            "📱 Phone: {phone}\n"
            "🏷 Your loyalty card barcode: `{barcode}`\n\n"
            "Show this code at any of our stores to get your discount!"
        ),
        "loyalty_already_exists": (
            "✅ *Welcome back!*\n\n"
            "📱 Phone: {phone}\n"
            "🏷 Barcode: `{barcode}`\n\n"
            "Your information has been updated."
        ),

        # Store search
        "stores_request_geo": (
            "📍 *Find nearest store*\n\n"
            "Please share your location or choose a region manually:"
        ),
        "btn_send_geo": "📍 Share location",
        "btn_choose_region": "🗺 Choose region",
        "stores_choose_region": "Please select your region:",
        "stores_not_found": "😔 No stores found nearby. Try a different region.",
        "stores_result": "📍 *Nearest stores ({count} found):*",
        "btn_open_maps": "🗺 Open in Google Maps",
        "store_card": (
            "🏪 *{name}*\n"
            "📍 {address}\n"
            "🕐 {hours}\n"
        ),

        # Manager
        "manager_hello": (
            "💬 *Manager Chat*\n\n"
            "Our AI assistant will help you first.\n"
            "Type your question:"
        ),
        "manager_offline": (
            "🕐 Our managers work from 10:00 to 18:00.\n\n"
            "You can leave a message and we'll get back to you:"
        ),
        "manager_transfer": "🔄 Transferring you to a live manager...",
        "manager_transferred": "✅ A manager will respond shortly. Please wait.",
        "manager_left_message": "✅ Your message has been saved. We'll contact you soon!",
        "btn_transfer_manager": "👤 Talk to a human",
        "ai_error": "⚠️ AI assistant is temporarily unavailable. Connecting you to a manager...",

        # About
        "about_text": (
            "ℹ️ *About Us*\n\n"
            "We are a leading retail company providing quality products.\n\n"
            "🌐 Our stores are located across multiple countries.\n"
            "📞 Support: available 24/7 via this bot.\n\n"
            "Use the menu below to explore more:"
        ),

        # Socials
        "socials_text": "📲 *Our Social Media*\n\nVisit our mini-landing page for all links:",
        "btn_open_socials": "🔗 Open social links",

        # Errors
        "error_generic": "⚠️ Something went wrong. Please try again.",
    },

    "ru": {
        "welcome": "👋 Добро пожаловать! Пожалуйста, выберите язык:",
        "lang_set": "✅ Язык установлен: Русский.",
        "main_menu": "🏠 *Главное меню*\nВыберите раздел:",
        "btn_stores": "📍 Найти ближайший магазин",
        "btn_loyalty": "🎁 Получить карту лояльности",
        "btn_manager": "💬 Связаться с менеджером",
        "btn_about": "ℹ️ О компании",
        "btn_socials": "📲 Наши соцсети",
        "btn_back": "⬅️ Назад",
        "btn_main_menu": "🏠 Главное меню",
        "btn_change_lang": "🌐 Сменить язык",
        "loading": "⏳ Загрузка...",

        "loyalty_hint": "Получите карту лояльности за 30 секунд и получите бонус 🎁",
        # Reminders
        "loyalty_reminder": "Создание карты лояльности для получения бонусов в любом магазине занимает 30 секунд",
        "after_phone_reminder": "Завершите регистрацию, чтобы активировать бонус",
        "loyalty5m_reminder": "Без регистрации вы не сможете получать бонусы в магазинах",
        "loyalty_start": (
            "🎁 *Получите доступ к бонусам, скидкам и более оперативному обслуживанию*\n\n"
            "Введите номер телефона в международном формате:\n"
            "Пример: +79123456789"
        ),
        "loyalty_phone_invalid": "❌ Неверный формат. Используйте международный формат, например: +79123456789",
        "loyalty_otp_sent": "📱 OTP-код отправлен на *{phone}*\n\nВведите 6-значный код:",
        "loyalty_otp_invalid": "❌ Неверный OTP-код. Попробуйте ещё раз или нажмите /start.",
        "loyalty_otp_attempts": "❌ Превышено число попыток. Начните заново с /start",
        "loyalty_ask_age": "✅ Телефон подтверждён!\n\nВведите ваш возраст:",
        "loyalty_age_invalid": "❌ Введите корректный возраст (1-120):",
        "loyalty_ask_country": "🌍 Введите вашу страну (например: Россия, Таиланд, США):",
        "loyalty_success": (
            "🎉 *Регистрация успешна!*\n\n"
            "👤 ID клиента: `{client_id}`\n"
            "📱 Телефон: {phone}\n\n"
            "🏷 Ваш штрихкод карты лояльности: `{barcode}`\n\n"
            "Покажите этот код в любом нашем магазине для начисления баллов!"
        ),
        "loyalty_already_exists": (
            "✅ *Вы уже зарегистрированы!*\n\n"
            "👤 ID клиента: `{client_id}`\n"
            "🏷 Штрихкод: `{barcode}`\n\n"
            "Ваши данные обновлены."
        ),
        "loyalty_crm_error": "⚠️ Произошла техническая ошибка. Попробуйте позже или свяжитесь с менеджером.",

        # Новые ключи для REST API
        "loyalty_ask_name": "✅ Телефон подтверждён!\n\nВведите ваше полное имя:",
        "loyalty_name_invalid": "❌ Введите настоящее имя (минимум 2 символа):",
        "loyalty_ask_tourist": "🌍 Вы приехали как турист?",
        "loyalty_ask_thai_citizen": "🇹🇭 Вы гражданин Таиланда?",
        "btn_yes": "✅ Да",
        "btn_no": "❌ Нет",
        "loyalty_success": (
            "🎉 *Регистрация прошла успешно!*\n\n"
            "📱 Телефон: {phone}\n"
            "🏷 Штрихкод карты: `{barcode}`\n\n"
            "Покажите этот код в магазине для получения скидки!"
        ),
        "loyalty_already_exists": (
            "✅ *С возвращением!*\n\n"
            "📱 Телефон: {phone}\n"
            "🏷 Штрихкод: `{barcode}`\n\n"
            "Ваши данные обновлены."
        ),

        "stores_request_geo": (
            "📍 *Поиск ближайшего магазина*\n\n"
            "Поделитесь геолокацией или выберите регион вручную:"
        ),
        "btn_send_geo": "📍 Отправить геолокацию",
        "btn_choose_region": "🗺 Выбрать регион",
        "stores_choose_region": "Выберите ваш регион:",
        "stores_not_found": "😔 Рядом не найдено магазинов. Попробуйте другой регион.",
        "stores_result": "📍 *Ближайшие магазины (найдено: {count}):*",
        "btn_open_maps": "🗺 Открыть в Google Maps",
        "store_card": (
            "🏪 *{name}*\n"
            "📍 {address}\n"
            "🕐 {hours}\n"
        ),

        "manager_hello": (
            "💬 *Чат с менеджером*\n\n"
            "Сначала вам ответит AI-ассистент.\n"
            "Напишите ваш вопрос:"
        ),
        "manager_offline": (
            "🕐 Менеджеры работают с 10:00 до 18:00.\n\n"
            "Вы можете оставить сообщение, и мы свяжемся с вами:"
        ),
        "manager_transfer": "🔄 Передаём вас живому менеджеру...",
        "manager_transferred": "✅ Менеджер скоро ответит. Пожалуйста, подождите.",
        "manager_left_message": "✅ Ваше сообщение сохранено. Мы свяжемся с вами в ближайшее время!",
        "btn_transfer_manager": "👤 Связаться с человеком",
        "ai_error": "⚠️ AI-ассистент временно недоступен. Соединяем с менеджером...",

        "about_text": (
            "ℹ️ *О компании*\n\n"
            "Мы — ведущая розничная компания, предлагающая качественные продукты.\n\n"
            "🌐 Наши магазины расположены в нескольких странах.\n"
            "📞 Поддержка доступна 24/7 через этого бота.\n\n"
            "Используйте меню для навигации:"
        ),

        "socials_text": "📲 *Наши соцсети*\n\nПосетите наш мини-лендинг со всеми ссылками:",
        "btn_open_socials": "🔗 Открыть соцсети",
        "error_generic": "⚠️ Что-то пошло не так. Попробуйте ещё раз.",
    },

    "th": {
        "welcome": "👋 ยินดีต้อนรับ! กรุณาเลือกภาษา:",
        "lang_set": "✅ ตั้งค่าภาษาเป็นภาษาไทยแล้ว",
        "main_menu": "🏠 *เมนูหลัก*\nเลือกหัวข้อ:",
        "btn_stores": "📍 ค้นหาร้านใกล้เคียง",
        "btn_loyalty": "🎁 รับบัตรสะสมแต้ม",
        "btn_manager": "💬 ติดต่อผู้จัดการ",
        "btn_about": "ℹ️ เกี่ยวกับเรา",
        "btn_socials": "📲 โซเชียลมีเดียของเรา",
        "btn_back": "⬅️ กลับ",
        "btn_main_menu": "🏠 เมนูหลัก",
        "btn_change_lang": "🌐 เปลี่ยนภาษา",
        "loading": "⏳ กำลังโหลด",
        "loyalty_hint": "รับบัตรสะสมแต้มใน 30 วินาทีและรับโบนัส 🎁",
        # Reminders
        "loyalty_reminder": "การสร้างบัตรสะสมแต้มเพื่อรับโบนัสที่ร้านค้าใดก็ได้ใช้เวลาเพียง 30 วินาที",
        "after_phone_reminder": "กรอกข้อมูลลงทะเบียนให้ครบถ้วนเพื่อเปิดใช้งานโบนัส",
        "loyalty5m_reminder": "หากไม่ลงทะเบียน คุณจะไม่สามารถรับโบนัสในร้านค้าได้",
        "loyalty_start": (
            "🎁 *รับสิทธิ์พิเศษ ส่วนลด และบริการที่รวดเร็วยิ่งขึ้น*\n\n"
            "กรุณาใส่หมายเลขโทรศัพท์ในรูปแบบสากล:\n"
            "ตัวอย่าง: +66812345678"
        ),
        "loyalty_phone_invalid": "❌ หมายเลขโทรศัพท์ไม่ถูกต้อง กรุณาใช้รูปแบบสากล เช่น +66812345678",
        "loyalty_otp_sent": "📱 ส่งรหัส OTP ไปยัง *{phone}* แล้ว\n\nกรุณาใส่รหัส 6 หลัก:",
        "loyalty_otp_invalid": "❌ รหัส OTP ไม่ถูกต้อง กรุณาลองอีกครั้ง",
        "loyalty_otp_attempts": "❌ ลองผิดพลาดหลายครั้งเกินไป กรุณาเริ่มใหม่",
        "loyalty_ask_age": "✅ ยืนยันเบอร์โทรแล้ว!\n\nกรุณาใส่อายุของคุณ:",
        "loyalty_age_invalid": "❌ กรุณาใส่อายุที่ถูกต้อง (1-120):",
        "loyalty_ask_country": "🌍 กรุณาใส่ประเทศของคุณ (เช่น Thailand, Russia):",
        "loyalty_success": (
            "🎉 *ลงทะเบียนสำเร็จ!*\n\n"
            "👤 รหัสลูกค้า: `{client_id}`\n"
            "📱 โทรศัพท์: {phone}\n\n"
            "🏷 บาร์โค้ดบัตรสะสมแต้ม: `{barcode}`\n\n"
            "แสดงรหัสนี้ที่ร้านค้าของเราเพื่อสะสมแต้ม!"
        ),
        "loyalty_already_exists": (
            "✅ *คุณลงทะเบียนแล้ว!*\n\n"
            "👤 รหัสลูกค้า: `{client_id}`\n"
            "🏷 บาร์โค้ด: `{barcode}`\n\n"
            "อัปเดตข้อมูลของคุณแล้ว"
        ),
        "loyalty_crm_error": "⚠️ เกิดข้อผิดพลาด กรุณาลองใหม่ภายหลังหรือติดต่อผู้จัดการ",

        # คีย์ใหม่สำหรับ REST API
        "loyalty_ask_name": "✅ ยืนยันเบอร์โทรแล้ว!\n\nกรุณาใส่ชื่อ-นามสกุล:",
        "loyalty_name_invalid": "❌ กรุณาใส่ชื่อจริง (อย่างน้อย 2 ตัวอักษร):",
        "loyalty_ask_tourist": "🌍 คุณมาในฐานะนักท่องเที่ยวใช่ไหม?",
        "loyalty_ask_thai_citizen": "🇹🇭 คุณเป็นพลเมืองไทยหรือไม่?",
        "btn_yes": "✅ ใช่",
        "btn_no": "❌ ไม่ใช่",
        "loyalty_success": (
            "🎉 *ลงทะเบียนสำเร็จ!*\n\n"
            "📱 เบอร์โทร: {phone}\n"
            "🏷 บาร์โค้ดบัตรสะสมแต้ม: `{barcode}`\n\n"
            "แสดงรหัสนี้ที่ร้านเพื่อรับส่วนลด!"
        ),
        "loyalty_already_exists": (
            "✅ *ยินดีต้อนรับกลับมา!*\n\n"
            "📱 เบอร์โทร: {phone}\n"
            "🏷 บาร์โค้ด: `{barcode}`\n\n"
            "อัปเดตข้อมูลของคุณแล้ว"
        ),

        "stores_request_geo": "📍 *ค้นหาร้านใกล้เคียง*\n\nแชร์ตำแหน่งหรือเลือกภูมิภาคด้วยตนเอง:",
        "btn_send_geo": "📍 แชร์ตำแหน่ง",
        "btn_choose_region": "🗺 เลือกภูมิภาค",
        "stores_choose_region": "กรุณาเลือกภูมิภาคของคุณ:",
        "stores_not_found": "😔 ไม่พบร้านค้าใกล้เคียง ลองเลือกภูมิภาคอื่น",
        "stores_result": "📍 *ร้านค้าใกล้เคียง (พบ {count} แห่ง):*",
        "btn_open_maps": "🗺 เปิดใน Google Maps",
        "store_card": "🏪 *{name}*\n📍 {address}\n🕐 {hours}\n",

        "manager_hello": "💬 *แชทกับผู้จัดการ*\n\nผู้ช่วย AI จะตอบก่อน\nพิมพ์คำถามของคุณ:",
        "manager_offline": "🕐 ผู้จัดการทำงานตั้งแต่ 10:00 ถึง 18:00\n\nคุณสามารถฝากข้อความไว้ได้:",
        "manager_transfer": "🔄 กำลังโอนไปยังผู้จัดการ...",
        "manager_transferred": "✅ ผู้จัดการจะตอบในไม่ช้า กรุณารอสักครู่",
        "manager_left_message": "✅ บันทึกข้อความของคุณแล้ว เราจะติดต่อกลับโดยเร็ว!",
        "btn_transfer_manager": "👤 คุยกับคน",
        "ai_error": "⚠️ AI ไม่พร้อมใช้งานชั่วคราว กำลังเชื่อมต่อกับผู้จัดการ...",

        "about_text": (
            "ℹ️ *เกี่ยวกับเรา*\n\n"
            "เราเป็นบริษัทค้าปลีกชั้นนำที่มอบสินค้าคุณภาพ\n\n"
            "🌐 ร้านค้าของเราอยู่ในหลายประเทศ\n"
            "📞 บริการตลอด 24/7 ผ่านบอตนี้\n\n"
            "ใช้เมนูเพื่อสำรวจเพิ่มเติม:"
        ),

        "socials_text": "📲 *โซเชียลมีเดียของเรา*\n\nเยี่ยมชมหน้า mini-landing ของเรา:",
        "btn_open_socials": "🔗 เปิดโซเชียลมีเดีย",
        "error_generic": "⚠️ เกิดข้อผิดพลาด กรุณาลองอีกครั้ง",
    }
}


def t(lang: str, key: str, **kwargs) -> str:
    text = TEXTS.get(lang, TEXTS["en"]).get(key, TEXTS["en"].get(key, key))
    if kwargs:
        return text.format(**kwargs)
    return text
