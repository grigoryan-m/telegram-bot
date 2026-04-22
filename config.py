import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# ── WeedeN REST API ──────────────────────────────────────────
ODOO_URL = os.getenv("ODOO_URL", "")          # e.g. https://your-odoo-instance.com
ODOO_API_TOKEN = os.getenv("ODOO_API_TOKEN", "")  # Bearer token for /api/client/register

# ── Manager notifications ────────────────────────────────────
MANAGER_CHAT_ID = os.getenv("MANAGER_CHAT_ID", "")
MANAGER_WORK_START = int(os.getenv("MANAGER_WORK_START", "10"))
MANAGER_WORK_END = int(os.getenv("MANAGER_WORK_END", "18"))

# ── External links ───────────────────────────────────────────
SOCIALS_URL = os.getenv("SOCIALS_URL", "https://example.com/socials")
RECIPE_URL = os.getenv("RECIPE_URL", "https://example.com/recipes")
