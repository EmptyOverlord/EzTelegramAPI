# EzTelegramAPI

![Python versions](https://img.shields.io/pypi/pyversions/requests.svg)

> **The simplest way to send Telegram messages from Python.**  
> One function. Zero boilerplate. Just send.

---

## Installation

```bash
pip install EzTelegramAPI
```

---

## Quickstart

```python
from eztelegramapi import send_message

TOKEN   = "123456789:AABBCCDDEEFFaabbccddeeff-1234567890"  # from @BotFather
CHAT_ID = 987654321                                         # your chat ID

send_message(TOKEN, CHAT_ID, "Hello from EzTelegramAPI! 🚀")
```

That's it. Seriously.

---

## Why EzTelegramAPI?

| | EzTelegramAPI | Other libraries |
|---|---------------|---|
| Setup | None          | Config, classes, handlers... |
| Lines to send a message | **1**         | 5–20+ |
| Dependencies | `requests`    | Multiple |
| Learning curve | Zero          | Non-zero |

---

## API Reference

### `send_message(token, chat_id, text)`

| Parameter | Type | Description |
|-----------|------|-------------|
| `token` | `str` | Your bot token from [@BotFather](https://t.me/BotFather) |
| `chat_id` | `int` | Target chat or user ID |
| `text` | `str` | Message text (supports emoji ✅) |

**Returns:** `requests.Response` — the raw Telegram API response.

---

## Examples

**Alert on error:**
```python
try:
    risky_operation()
except Exception as e:
    send_message(TOKEN, CHAT_ID, f"🔴 Error: {e}")
```

**Cron job notification:**
```python
from datetime import datetime

now = datetime.now().strftime("%Y-%m-%d %H:%M")
send_message(TOKEN, CHAT_ID, f"✅ Backup finished at {now}")
```

**Send your public IP address:**
```python
import requests

ip = requests.get("https://api.ipify.org").text
send_message(TOKEN, CHAT_ID, f"🌐 My IP: {ip}")
```

---

## How to get your Chat ID

1. Start a chat with [@userinfobot](https://t.me/userinfobot)
2. Send `/start`
3. It replies with your numeric ID — use that as `chat_id`

---

## License

MIT