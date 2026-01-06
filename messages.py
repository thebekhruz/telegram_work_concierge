"""
Localized messages for the Work Concierge Bot
Supports: English (EN), Russian (RU), Uzbek (UZB)
"""

MESSAGES = {
    # Welcome and language selection
    "welcome": {
        "en": "👋 Welcome! Please choose your language:",
        "ru": "👋 Добро пожаловать! Пожалуйста, выберите язык:",
        "uzb": "👋 Xush kelibsiz! Iltimos, tilni tanlang:"
    },

    # Main menu - purpose selection
    "choose_purpose": {
        "en": "What would you like to do?",
        "ru": "Что вы хотели бы сделать?",
        "uzb": "Nima qilmoqchisiz?"
    },
    "btn_job": {
        "en": "🔍 Looking for a job",
        "ru": "🔍 Ищу работу",
        "uzb": "🔍 Ish qidirmoqdaman"
    },
    "btn_proposal": {
        "en": "💼 Commercial proposal",
        "ru": "💼 Коммерческое предложение",
        "uzb": "💼 Tijorat taklifi"
    },

    # Job seeker flow
    "job_ask_cv": {
        "en": "📄 Please send your CV (PDF or DOC format):",
        "ru": "📄 Пожалуйста, отправьте ваше резюме (формат PDF или DOC):",
        "uzb": "📄 Iltimos, rezyumeyingizni yuboring (PDF yoki DOC formatida):"
    },
    "job_cv_received": {
        "en": "✅ CV received! Now please share your phone number:",
        "ru": "✅ Резюме получено! Теперь, пожалуйста, поделитесь номером телефона:",
        "uzb": "✅ Rezyume qabul qilindi! Endi telefon raqamingizni yuboring:"
    },
    "job_invalid_cv": {
        "en": "❌ Please send a valid file (PDF or DOC format only):",
        "ru": "❌ Пожалуйста, отправьте файл в правильном формате (только PDF или DOC):",
        "uzb": "❌ Iltimos, to'g'ri formatdagi faylni yuboring (faqat PDF yoki DOC):"
    },
    "job_ask_phone": {
        "en": "📱 Please share your phone number (use the button below or type it manually):",
        "ru": "📱 Пожалуйста, поделитесь номером телефона (используйте кнопку ниже или введите вручную):",
        "uzb": "📱 Iltimos, telefon raqamingizni yuboring (quyidagi tugmani bosing yoki qo'lda kiriting):"
    },
    "btn_share_phone": {
        "en": "📱 Share phone number",
        "ru": "📱 Поделиться номером",
        "uzb": "📱 Telefon raqamini ulashish"
    },
    "job_phone_received": {
        "en": "✅ Phone number received! Please provide any additional information about yourself (experience, skills, desired position, etc.):",
        "ru": "✅ Номер телефона получен! Пожалуйста, предоставьте дополнительную информацию о себе (опыт, навыки, желаемая должность и т.д.):",
        "uzb": "✅ Telefon raqami qabul qilindi! Iltimos, o'zingiz haqingizda qo'shimcha ma'lumot bering (tajriba, ko'nikmalar, istalgan lavozim va h.k.):"
    },
    "job_success": {
        "en": "✅ Thank you! Your application has been sent to our HR team. We will contact you soon!",
        "ru": "✅ Спасибо! Ваша заявка отправлена нашей HR команде. Мы свяжемся с вами в ближайшее время!",
        "uzb": "✅ Rahmat! Arizangiz HR jamoamizga yuborildi. Tez orada siz bilan bog'lanamiz!"
    },

    # Commercial proposal flow
    "proposal_ask_company": {
        "en": "🏢 Please enter your company name:",
        "ru": "🏢 Пожалуйста, введите название вашей компании:",
        "uzb": "🏢 Iltimos, kompaniyangiz nomini kiriting:"
    },
    "proposal_ask_social": {
        "en": "🌐 Please provide your company's social media profile (Instagram, LinkedIn, etc.):",
        "ru": "🌐 Пожалуйста, укажите профиль вашей компании в социальных сетях (Instagram, LinkedIn и т.д.):",
        "uzb": "🌐 Iltimos, kompaniyangizning ijtimoiy tarmoqdagi profilini ko'rsating (Instagram, LinkedIn va h.k.):"
    },
    "proposal_ask_telegram": {
        "en": "📱 Please provide your Telegram contact (@username or phone):",
        "ru": "📱 Пожалуйста, укажите ваш Telegram контакт (@username или телефон):",
        "uzb": "📱 Iltimos, Telegram kontaktingizni ko'rsating (@username yoki telefon):"
    },
    "proposal_ask_phone": {
        "en": "📞 Please provide your phone number:",
        "ru": "📞 Пожалуйста, укажите ваш номер телефона:",
        "uzb": "📞 Iltimos, telefon raqamingizni ko'rsating:"
    },
    "proposal_ask_purpose": {
        "en": "🎯 What is the purpose of your proposal? How can you help us?",
        "ru": "🎯 Какова цель вашего предложения? Чем вы можете нам помочь?",
        "uzb": "🎯 Taklifingizning maqsadi nima? Bizga qanday yordam bera olasiz?"
    },
    "proposal_ask_files": {
        "en": "📎 Please send any relevant files (presentations, price lists, etc.). When done, press 'Done' or send /done:",
        "ru": "📎 Пожалуйста, отправьте соответствующие файлы (презентации, прайс-листы и т.д.). Когда закончите, нажмите 'Готово' или отправьте /done:",
        "uzb": "📎 Iltimos, tegishli fayllarni yuboring (taqdimotlar, narxlar ro'yxati va h.k.). Tugatgach, 'Tayyor' tugmasini bosing yoki /done yuboring:"
    },
    "btn_done": {
        "en": "✅ Done",
        "ru": "✅ Готово",
        "uzb": "✅ Tayyor"
    },
    "btn_skip": {
        "en": "⏭️ Skip",
        "ru": "⏭️ Пропустить",
        "uzb": "⏭️ O'tkazib yuborish"
    },
    "proposal_file_received": {
        "en": "📎 File received! Send more files or press 'Done' when finished:",
        "ru": "📎 Файл получен! Отправьте ещё файлы или нажмите 'Готово' когда закончите:",
        "uzb": "📎 Fayl qabul qilindi! Yana fayl yuboring yoki tugatgach 'Tayyor' tugmasini bosing:"
    },
    "proposal_success": {
        "en": "✅ Thank you! Your commercial proposal has been sent to our team. We will review it and contact you soon!",
        "ru": "✅ Спасибо! Ваше коммерческое предложение отправлено нашей команде. Мы рассмотрим его и свяжемся с вами в ближайшее время!",
        "uzb": "✅ Rahmat! Tijorat taklifingiz jamoamizga yuborildi. Biz uni ko'rib chiqamiz va tez orada siz bilan bog'lanamiz!"
    },

    # Cancel and restart
    "cancelled": {
        "en": "❌ Operation cancelled. Use /start to begin again.",
        "ru": "❌ Операция отменена. Используйте /start чтобы начать снова.",
        "uzb": "❌ Amal bekor qilindi. Qayta boshlash uchun /start yuboring."
    },

    # HR notification template
    "hr_notification": {
        "en": """📋 NEW JOB APPLICATION

👤 From: {name} (@{username})
📱 Phone: {phone}
💬 Additional info:
{info}

📄 CV attached below""",
        "ru": """📋 НОВАЯ ЗАЯВКА НА РАБОТУ

👤 От: {name} (@{username})
📱 Телефон: {phone}
💬 Дополнительная информация:
{info}

📄 Резюме прикреплено ниже""",
        "uzb": """📋 YANGI ISH ARIZASI

👤 Kimdan: {name} (@{username})
📱 Telefon: {phone}
💬 Qo'shimcha ma'lumot:
{info}

📄 Rezyume quyida biriktirilgan"""
    },

    # CMO notification template
    "cmo_notification": {
        "en": """💼 NEW COMMERCIAL PROPOSAL

🏢 Company: {company}
👤 Contact: {name} (@{username})
🌐 Social media: {social}
📱 Telegram: {telegram}
📞 Phone: {phone}

🎯 Purpose:
{purpose}

📎 Files attached below (if any)""",
        "ru": """💼 НОВОЕ КОММЕРЧЕСКОЕ ПРЕДЛОЖЕНИЕ

🏢 Компания: {company}
👤 Контакт: {name} (@{username})
🌐 Соцсети: {social}
📱 Telegram: {telegram}
📞 Телефон: {phone}

🎯 Цель предложения:
{purpose}

📎 Файлы прикреплены ниже (если есть)""",
        "uzb": """💼 YANGI TIJORAT TAKLIFI

🏢 Kompaniya: {company}
👤 Kontakt: {name} (@{username})
🌐 Ijtimoiy tarmoq: {social}
📱 Telegram: {telegram}
📞 Telefon: {phone}

🎯 Taklif maqsadi:
{purpose}

📎 Fayllar quyida biriktirilgan (agar mavjud bo'lsa)"""
    }
}


def get_message(key: str, lang: str = "en") -> str:
    """Get a localized message by key and language."""
    if key in MESSAGES:
        return MESSAGES[key].get(lang, MESSAGES[key].get("en", key))
    return key
