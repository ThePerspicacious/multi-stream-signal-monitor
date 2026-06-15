# ─────────────────────────────────────────────────────────
# config.example.py
#
# Copy this file to config.py and fill in your real values.
# ─────────────────────────────────────────────────────────

# Telegram API credentials
# Get these from https://my.telegram.org/auth
API_ID = "your_api_id_here"
API_HASH = "your_api_hash_here"
PHONE_NUMBER = "+123XXXXXXXXXX"

# Channel IDs to monitor
# These are negative integers — find them via @userinfobot inside telegram.
# Replace with your desired IDs
PRIVATE_CHANNEL_ID = -100000000000
LINKED_GROUP_ID    = -100000000000
PUBLIC_CHANNEL_ID  = -100000000000

# Target bots/channels to forward validated signals to
TARGET_SOLANA_BOT = "@your_solana_bot"
TARGET_TRON_BOT   = "@your_tron_bot"
TARGET_BROADCAST_CHANNEL = "@your_broadcast_channel" # # Can also use Channel ID instead of username. ( Group/channel both works )

# Your custom link base (signal address gets appended)
# Example: "https://t.me/xyzbot?start=r-itz_thewolf"
REFERRAL_LINK_BASE = "https://t.me/yourbot?start=ref-yourname-" #Best usecase is to use a custom referral link from a tradingbot.

# Path to file containing your custom broadcast message
CUSTOM_MESSAGE_FILE = "custom_message.txt"
