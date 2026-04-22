import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
ODOO_URL = os.getenv("ODOO_URL", "")
ODOO_DB = os.getenv("ODOO_DB", "")
ODOO_USERNAME = os.getenv("ODOO_USERNAME", "")
ODOO_PASSWORD = os.getenv("ODOO_PASSWORD", "")

MANAGER_CHAT_ID = os.getenv("MANAGER_CHAT_ID", "")  # Telegram ID менеджера или группы
MANAGER_WORK_START = int(os.getenv("MANAGER_WORK_START", "10"))
MANAGER_WORK_END = int(os.getenv("MANAGER_WORK_END", "18"))

SOCIALS_URL = os.getenv("SOCIALS_URL", "https://example.com/socials")
RECIPE_URL = os.getenv("RECIPE_URL", "https://example.com/recipes")
