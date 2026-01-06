#!/usr/bin/env python3
"""
Telegram Work Concierge Bot
Handles job applications and commercial proposals
"""

import os
import logging
from typing import Dict, Any

from dotenv import load_dotenv
from telegram import (
    Update,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ConversationHandler,
    ContextTypes,
    filters,
)

from messages import get_message, MESSAGES

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot configuration
BOT_TOKEN = os.getenv("BOT_TOKEN")
HR_CHAT_ID = os.getenv("HR_CHAT_ID")
CMO_CHAT_ID = os.getenv("CMO_CHAT_ID")

# Conversation states
(
    LANGUAGE,
    PURPOSE,
    # Job seeker states
    JOB_CV,
    JOB_PHONE,
    JOB_INFO,
    # Commercial proposal states
    PROPOSAL_COMPANY,
    PROPOSAL_SOCIAL,
    PROPOSAL_TELEGRAM,
    PROPOSAL_PHONE,
    PROPOSAL_PURPOSE,
    PROPOSAL_FILES,
) = range(11)

# User data keys
USER_LANG = "lang"
USER_CV_FILE_ID = "cv_file_id"
USER_CV_FILE_NAME = "cv_file_name"
USER_PHONE = "phone"
USER_INFO = "info"
USER_COMPANY = "company"
USER_SOCIAL = "social"
USER_TELEGRAM = "telegram_contact"
USER_PURPOSE = "purpose"
USER_FILES = "files"


def get_lang(context: ContextTypes.DEFAULT_TYPE) -> str:
    """Get user's selected language, default to English."""
    return context.user_data.get(USER_LANG, "en")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Start the conversation and ask for language selection."""
    # Clear any previous user data
    context.user_data.clear()

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🇬🇧 English", callback_data="lang_en"),
            InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru"),
            InlineKeyboardButton("🇺🇿 O'zbek", callback_data="lang_uzb"),
        ]
    ])

    await update.message.reply_text(
        "👋 Welcome! / Добро пожаловать! / Xush kelibsiz!\n\n"
        "Please choose your language:",
        reply_markup=keyboard
    )
    return LANGUAGE


async def language_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle language selection callback."""
    query = update.callback_query
    await query.answer()

    lang = query.data.replace("lang_", "")
    context.user_data[USER_LANG] = lang

    # Show purpose selection
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(get_message("btn_job", lang), callback_data="purpose_job")],
        [InlineKeyboardButton(get_message("btn_proposal", lang), callback_data="purpose_proposal")],
    ])

    await query.edit_message_text(
        get_message("choose_purpose", lang),
        reply_markup=keyboard
    )
    return PURPOSE


async def purpose_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle purpose selection callback."""
    query = update.callback_query
    await query.answer()

    lang = get_lang(context)
    purpose = query.data.replace("purpose_", "")

    if purpose == "job":
        await query.edit_message_text(get_message("job_ask_cv", lang))
        return JOB_CV
    else:  # proposal
        await query.edit_message_text(get_message("proposal_ask_company", lang))
        return PROPOSAL_COMPANY


# ============ JOB SEEKER FLOW ============

async def job_receive_cv(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle CV file upload."""
    lang = get_lang(context)

    if update.message.document:
        file_name = update.message.document.file_name.lower()
        if file_name.endswith(('.pdf', '.doc', '.docx')):
            context.user_data[USER_CV_FILE_ID] = update.message.document.file_id
            context.user_data[USER_CV_FILE_NAME] = update.message.document.file_name

            # Ask for phone number with share button
            keyboard = ReplyKeyboardMarkup(
                [[KeyboardButton(get_message("btn_share_phone", lang), request_contact=True)]],
                resize_keyboard=True,
                one_time_keyboard=True
            )

            await update.message.reply_text(
                get_message("job_cv_received", lang) + "\n\n" + get_message("job_ask_phone", lang),
                reply_markup=keyboard
            )
            return JOB_PHONE
        else:
            await update.message.reply_text(get_message("job_invalid_cv", lang))
            return JOB_CV
    else:
        await update.message.reply_text(get_message("job_invalid_cv", lang))
        return JOB_CV


async def job_receive_phone(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle phone number from job seeker."""
    lang = get_lang(context)

    if update.message.contact:
        context.user_data[USER_PHONE] = update.message.contact.phone_number
    else:
        context.user_data[USER_PHONE] = update.message.text

    await update.message.reply_text(
        get_message("job_phone_received", lang),
        reply_markup=ReplyKeyboardRemove()
    )
    return JOB_INFO


async def job_receive_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle additional info and send to HR."""
    lang = get_lang(context)
    user = update.effective_user

    context.user_data[USER_INFO] = update.message.text

    # Prepare notification message for HR
    notification = get_message("hr_notification", lang).format(
        name=user.full_name,
        username=user.username or "N/A",
        phone=context.user_data.get(USER_PHONE, "N/A"),
        info=context.user_data.get(USER_INFO, "N/A")
    )

    # Send notification and CV to HR chat
    if HR_CHAT_ID:
        try:
            await context.bot.send_message(chat_id=HR_CHAT_ID, text=notification)
            await context.bot.send_document(
                chat_id=HR_CHAT_ID,
                document=context.user_data[USER_CV_FILE_ID],
                filename=context.user_data.get(USER_CV_FILE_NAME, "CV")
            )
            logger.info(f"Job application sent to HR from user {user.id}")
        except Exception as e:
            logger.error(f"Failed to send to HR: {e}")

    await update.message.reply_text(get_message("job_success", lang))

    # Clear user data
    context.user_data.clear()
    return ConversationHandler.END


# ============ COMMERCIAL PROPOSAL FLOW ============

async def proposal_receive_company(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle company name input."""
    lang = get_lang(context)
    context.user_data[USER_COMPANY] = update.message.text

    await update.message.reply_text(get_message("proposal_ask_social", lang))
    return PROPOSAL_SOCIAL


async def proposal_receive_social(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle social media profile input."""
    lang = get_lang(context)
    context.user_data[USER_SOCIAL] = update.message.text

    await update.message.reply_text(get_message("proposal_ask_telegram", lang))
    return PROPOSAL_TELEGRAM


async def proposal_receive_telegram(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle Telegram contact input."""
    lang = get_lang(context)
    context.user_data[USER_TELEGRAM] = update.message.text

    # Ask for phone number with share button
    keyboard = ReplyKeyboardMarkup(
        [[KeyboardButton(get_message("btn_share_phone", lang), request_contact=True)]],
        resize_keyboard=True,
        one_time_keyboard=True
    )

    await update.message.reply_text(
        get_message("proposal_ask_phone", lang),
        reply_markup=keyboard
    )
    return PROPOSAL_PHONE


async def proposal_receive_phone(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle phone number for commercial proposal."""
    lang = get_lang(context)

    if update.message.contact:
        context.user_data[USER_PHONE] = update.message.contact.phone_number
    else:
        context.user_data[USER_PHONE] = update.message.text

    await update.message.reply_text(
        get_message("proposal_ask_purpose", lang),
        reply_markup=ReplyKeyboardRemove()
    )
    return PROPOSAL_PURPOSE


async def proposal_receive_purpose(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle proposal purpose/description."""
    lang = get_lang(context)
    context.user_data[USER_PURPOSE] = update.message.text
    context.user_data[USER_FILES] = []  # Initialize files list

    keyboard = ReplyKeyboardMarkup(
        [
            [KeyboardButton(get_message("btn_done", lang))],
            [KeyboardButton(get_message("btn_skip", lang))]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )

    await update.message.reply_text(
        get_message("proposal_ask_files", lang),
        reply_markup=keyboard
    )
    return PROPOSAL_FILES


async def proposal_receive_file(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle file uploads for commercial proposal."""
    lang = get_lang(context)

    if update.message.document:
        files = context.user_data.get(USER_FILES, [])
        files.append({
            "file_id": update.message.document.file_id,
            "file_name": update.message.document.file_name
        })
        context.user_data[USER_FILES] = files

        keyboard = ReplyKeyboardMarkup(
            [[KeyboardButton(get_message("btn_done", lang))]],
            resize_keyboard=True,
            one_time_keyboard=True
        )

        await update.message.reply_text(
            get_message("proposal_file_received", lang),
            reply_markup=keyboard
        )
        return PROPOSAL_FILES

    # If not a file, check if it's the done/skip button
    return await proposal_done(update, context)


async def proposal_done(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Finish proposal submission and send to CMO."""
    lang = get_lang(context)
    user = update.effective_user

    # Prepare notification message for CMO
    notification = get_message("cmo_notification", lang).format(
        company=context.user_data.get(USER_COMPANY, "N/A"),
        name=user.full_name,
        username=user.username or "N/A",
        social=context.user_data.get(USER_SOCIAL, "N/A"),
        telegram=context.user_data.get(USER_TELEGRAM, "N/A"),
        phone=context.user_data.get(USER_PHONE, "N/A"),
        purpose=context.user_data.get(USER_PURPOSE, "N/A")
    )

    # Send to CMO chat
    if CMO_CHAT_ID:
        try:
            await context.bot.send_message(chat_id=CMO_CHAT_ID, text=notification)

            # Send attached files
            files = context.user_data.get(USER_FILES, [])
            for file_info in files:
                await context.bot.send_document(
                    chat_id=CMO_CHAT_ID,
                    document=file_info["file_id"],
                    filename=file_info.get("file_name", "file")
                )

            logger.info(f"Commercial proposal sent to CMO from user {user.id}")
        except Exception as e:
            logger.error(f"Failed to send to CMO: {e}")

    await update.message.reply_text(
        get_message("proposal_success", lang),
        reply_markup=ReplyKeyboardRemove()
    )

    # Clear user data
    context.user_data.clear()
    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancel the conversation."""
    lang = get_lang(context)
    context.user_data.clear()

    await update.message.reply_text(
        get_message("cancelled", lang),
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


def main() -> None:
    """Start the bot."""
    if not BOT_TOKEN:
        logger.error("BOT_TOKEN not set! Please configure your .env file.")
        return

    if not HR_CHAT_ID:
        logger.warning("HR_CHAT_ID not set! Job applications won't be forwarded.")

    if not CMO_CHAT_ID:
        logger.warning("CMO_CHAT_ID not set! Commercial proposals won't be forwarded.")

    # Create application
    application = Application.builder().token(BOT_TOKEN).build()

    # Define conversation handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            LANGUAGE: [
                CallbackQueryHandler(language_callback, pattern="^lang_")
            ],
            PURPOSE: [
                CallbackQueryHandler(purpose_callback, pattern="^purpose_")
            ],
            # Job seeker flow
            JOB_CV: [
                MessageHandler(filters.Document.ALL, job_receive_cv),
                MessageHandler(filters.TEXT & ~filters.COMMAND, job_receive_cv)
            ],
            JOB_PHONE: [
                MessageHandler(filters.CONTACT, job_receive_phone),
                MessageHandler(filters.TEXT & ~filters.COMMAND, job_receive_phone)
            ],
            JOB_INFO: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, job_receive_info)
            ],
            # Commercial proposal flow
            PROPOSAL_COMPANY: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, proposal_receive_company)
            ],
            PROPOSAL_SOCIAL: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, proposal_receive_social)
            ],
            PROPOSAL_TELEGRAM: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, proposal_receive_telegram)
            ],
            PROPOSAL_PHONE: [
                MessageHandler(filters.CONTACT, proposal_receive_phone),
                MessageHandler(filters.TEXT & ~filters.COMMAND, proposal_receive_phone)
            ],
            PROPOSAL_PURPOSE: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, proposal_receive_purpose)
            ],
            PROPOSAL_FILES: [
                MessageHandler(filters.Document.ALL, proposal_receive_file),
                MessageHandler(filters.TEXT & ~filters.COMMAND, proposal_done),
                CommandHandler("done", proposal_done)
            ],
        },
        fallbacks=[CommandHandler("cancel", cancel), CommandHandler("start", start)],
    )

    # Add handler
    application.add_handler(conv_handler)

    # Start the bot
    logger.info("Bot starting...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
