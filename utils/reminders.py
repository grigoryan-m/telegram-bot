import asyncio
from locales.texts import t

# chat_id -> {reminder_name: task}
reminder_tasks = {}


async def send_loyalty_reminder(bot, chat_id, lang):
    try:
        await asyncio.sleep(7200)
        await bot.send_message(
            chat_id,
            t(lang, "loyalty_reminder")
        )
    except asyncio.CancelledError:
        pass


def start_reminder(bot, chat_id, lang, name: str, delay: int, text_key: str):
    """
    name: уникальное имя ремайнда (loyalty, timeout_5min и т.д.)
    delay: время в секундах
    text_key: ключ перевода
    """

    async def _task():
        try:
            await asyncio.sleep(delay)
            await bot.send_message(chat_id, t(lang, text_key))
        except asyncio.CancelledError:
            pass

    task = asyncio.create_task(_task())

    if chat_id not in reminder_tasks:
        reminder_tasks[chat_id] = {}

    reminder_tasks[chat_id][name] = task


def cancel_reminder(chat_id, name: str = None):
    """
    name=None → удалить все ремайндеры чата
    name="loyalty" → удалить конкретный
    """

    if chat_id not in reminder_tasks:
        return

    if name is None:
        # удалить все
        for task in reminder_tasks[chat_id].values():
            task.cancel()
        del reminder_tasks[chat_id]
        return

    task = reminder_tasks[chat_id].get(name)

    if task:
        task.cancel()
        del reminder_tasks[chat_id][name]

    if not reminder_tasks[chat_id]:
        del reminder_tasks[chat_id]