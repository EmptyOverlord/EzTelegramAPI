# EzTelegramAPI
![Python versions](https://img.shields.io/pypi/pyversions/requests.svg)
> **The simplest way to send Telegram messages from Python.**  
> Two functions. Zero boilerplate. Just send.
---
🔗 GitHub: https://github.com/EmptyOverlord/EzTelegramAPI  
📦 PyPI: https://pypi.org/project/eztelegramapi/
---
## Installation
```bash
pip install EzTelegramAPI
```
---
## Quickstart
```python
from eztelegramapi import send_message, edit_message

TOKEN   = "123456789:AABBCCDDEEFFaabbccddeeff-1234567890"  # from @BotFather
CHAT_ID = 987654321                                         # your chat ID

msg_id = send_message(TOKEN, CHAT_ID, "Hello from EzTelegramAPI! 🚀")
edit_message(TOKEN, CHAT_ID, msg_id, "Updated message ✏️")
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
### `send_message(token, chat_id, text, *, return_message_id=True)`
| Parameter | Type | Description |
|-----------|------|-------------|
| `token` | `str` | Your bot token from [@BotFather](https://t.me/BotFather) |
| `chat_id` | `int` | Target chat or user ID |
| `text` | `str` | Message text (supports emoji ✅) |
| `return_message_id` | `bool` | If `True` (default) returns `message_id`, else raw `Response` |

**Returns:** `int` (message_id) or `requests.Response`

---

### `edit_message(token, chat_id, message_id, text)`
| Parameter | Type | Description |
|-----------|------|-------------|
| `token` | `str` | Your bot token from [@BotFather](https://t.me/BotFather) |
| `chat_id` | `int` | Target chat or user ID |
| `message_id` | `int` | ID of the message to edit |
| `text` | `str` | New message text |

**Returns:** `requests.Response`

---
## Examples
**Live progress update:**
```python
import time

msg_id = send_message(TOKEN, CHAT_ID, "⏳ Job started...")
time.sleep(5)
edit_message(TOKEN, CHAT_ID, msg_id, "✅ Job finished!")
```
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
---
## How to get your Chat ID
1. Start a chat with [@userinfobot](https://t.me/userinfobot)
2. Send `/start`
3. It replies with your numeric ID — use that as `chat_id`
---
## License
MIT
