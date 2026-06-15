# ─────────────────────────────────────────────────────────
# config.example.py
#
# Copy this file to config.py and fill in your real values.
# NEVER upload config.py to GitHub — it contains your
# private credentials.
# ─────────────────────────────────────────────────────────

# Telegram API credentials
# Get these from https://my.telegram.org
API_ID = "your_api_id_here"
API_HASH = "your_api_hash_here"
PHONE_NUMBER = "+91XXXXXXXXXX"

# Channel IDs to monitor
# These are negative integers — find them via Telegram
PRIVATE_CHANNEL_ID = -100000000000
LINKED_GROUP_ID    = -100000000000
PUBLIC_CHANNEL_ID  = -100000000000

# Target bots/channels to forward validated signals to
TARGET_SOLANA_BOT = "@your_solana_bot"
TARGET_TRON_BOT   = "@your_tron_bot"
TARGET_BROADCAST  = "@your_broadcast_channel"

# Your referral link base (signal address gets appended)
# Example: "https://t.me/somebot?start=ref-yourname-"
REFERRAL_LINK_BASE = "https://t.me/yourbot?start=ref-yourname-"

# Path to file containing your custom broadcast message
CUSTOM_MESSAGE_FILE = "custom_message.txt"
