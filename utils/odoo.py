import logging
import xmlrpc.client
import random
import string
from typing import Optional, Dict as Dict, Any

from config import ODOO_URL, ODOO_DB, ODOO_USERNAME, ODOO_PASSWORD

logger = logging.getLogger(__name__)


def _get_odoo_uid() -> Optional[int]:
    try:
        common = xmlrpc.client.ServerProxy(f"{ODOO_URL}/xmlrpc/2/common")
        uid = common.authenticate(ODOO_DB, ODOO_USERNAME, ODOO_PASSWORD, {})
        return uid
    except Exception as e:
        logger.error(f"Odoo auth error: {e}")
        return None


def _get_models():
    return xmlrpc.client.ServerProxy(f"{ODOO_URL}/xmlrpc/2/object")


def _generate_barcode(client_id: int) -> str:
    return f"LC{client_id:08d}"


def find_customer_by_phone(phone: str) -> Optional[Dict[str, Any]]:
    """Returns existing customer dict or None."""
    try:
        uid = _get_odoo_uid()
        if not uid:
            return None
        models = _get_models()
        result = models.execute_kw(
            ODOO_DB, uid, ODOO_PASSWORD,
            "res.partner", "search_read",
            [[["phone", "=", phone]]],
            {"fields": ["id", "name", "phone", "barcode", "x_loyalty_id"], "limit": 1}
        )
        return result[0] if result else None
    except Exception as e:
        logger.error(f"Odoo find_customer error: {e}")
        return None


def create_or_update_customer(
    phone: str,
    age: int,
    country: str,
    messenger_id: str,
    messenger_type: str = "telegram"
) -> Optional[Dict[str, Any]]:
    """
    Create or update customer in Odoo.
    Returns dict with client_id and barcode on success, None on error.
    """
    try:
        uid = _get_odoo_uid()
        if not uid:
            return None
        models = _get_models()

        existing = find_customer_by_phone(phone)

        extra_data = {
            "x_age": age,
            "x_country_name": country,
            "x_messenger_id": messenger_id,
            "x_messenger_type": messenger_type,
        }

        if existing:
            # Update existing
            models.execute_kw(
                ODOO_DB, uid, ODOO_PASSWORD,
                "res.partner", "write",
                [[existing["id"]], extra_data]
            )
            client_id = existing["id"]
            barcode = existing.get("barcode") or _generate_barcode(client_id)
        else:
            # Create new
            partner_data = {
                "phone": phone,
                "name": f"Customer {phone}",
                **extra_data,
            }
            client_id = models.execute_kw(
                ODOO_DB, uid, ODOO_PASSWORD,
                "res.partner", "create",
                [partner_data]
            )
            barcode = _generate_barcode(client_id)
            models.execute_kw(
                ODOO_DB, uid, ODOO_PASSWORD,
                "res.partner", "write",
                [[client_id], {"barcode": barcode}]
            )

        return {
            "client_id": client_id,
            "barcode": barcode,
            "is_new": not bool(existing),
        }

    except Exception as e:
        logger.error(f"Odoo create_or_update error: {e}")
        return None
