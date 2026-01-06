# Telegram Work Concierge Bot

A multilingual Telegram bot for handling job applications and commercial proposals. The bot supports English, Russian, and Uzbek languages.

## Features

### 🔍 Job Seekers Flow
1. Select language (EN/RU/UZB)
2. Upload CV (PDF or DOC format)
3. Share phone number
4. Provide additional information (experience, skills, desired position)
5. Application is automatically sent to HR team chat

### 💼 Commercial Proposals Flow
1. Select language (EN/RU/UZB)
2. Provide company information:
   - Company name
   - Social media profile
   - Telegram contact
   - Phone number
3. Describe proposal purpose and how you can help
4. Attach relevant files (presentations, price lists, etc.)
5. Proposal is automatically sent to CMO team chat

## Setup

### 1. Create Telegram Bot
1. Message [@BotFather](https://t.me/BotFather) on Telegram
2. Send `/newbot` and follow the instructions
3. Copy the bot token

### 2. Get Chat IDs
To get group/channel chat IDs:
1. Add your bot to the HR and CMO groups
2. Send a message in each group
3. Visit: `https://api.telegram.org/bot<BOT_TOKEN>/getUpdates`
4. Find the `chat.id` values for your groups (they start with `-`)

### 3. Configure Environment
```bash
# Copy example config
cp .env.example .env

# Edit .env with your values
nano .env
```

Required environment variables:
- `BOT_TOKEN` - Your Telegram bot token from BotFather
- `HR_CHAT_ID` - Chat ID of the HR team group (for job applications)
- `CMO_CHAT_ID` - Chat ID of the CMO team group (for commercial proposals)

### 4. Install Dependencies
```bash
# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 5. Run the Bot
```bash
python bot.py
```

## Project Structure

```
telegram_work_concierge/
├── bot.py              # Main bot logic and handlers
├── messages.py         # Localized messages (EN/RU/UZB)
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
├── .env                # Your configuration (not in git)
└── README.md           # This file
```

## Bot Commands

- `/start` - Start the bot and select language
- `/cancel` - Cancel current operation
- `/done` - Finish file upload (commercial proposals)

## Customization

### Adding New Languages
Edit `messages.py` and add translations for your language code in the `MESSAGES` dictionary.

### Modifying Questions
Edit the message templates in `messages.py` to customize questions and responses.

## Deployment

### Using systemd (Linux)
Create `/etc/systemd/system/work-concierge-bot.service`:

```ini
[Unit]
Description=Work Concierge Telegram Bot
After=network.target

[Service]
Type=simple
User=your-user
WorkingDirectory=/path/to/telegram_work_concierge
Environment=PATH=/path/to/telegram_work_concierge/venv/bin
ExecStart=/path/to/telegram_work_concierge/venv/bin/python bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Then:
```bash
sudo systemctl daemon-reload
sudo systemctl enable work-concierge-bot
sudo systemctl start work-concierge-bot
```

### Using Docker
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "bot.py"]
```

## License

MIT License
