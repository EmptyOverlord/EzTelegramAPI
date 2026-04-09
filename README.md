# EzTelegramAPI
![Python versions](https://img.shields.io/pypi/pyversions/requests.svg)
> **The simplest way to send Telegram messages from Python.**  
> Four functions. One class. Zero boilerplate. Just send.
---
🔗 GitHub: https://github.com/EmptyOverlord/EzTelegramAPI  
📦 PyPI: https://pypi.org/project/eztelegramapi/
---
## Installation
```bash
pip install EzTelegramAPI
```
---
## Two ways to use it

### 1. Functions — quick and direct
No setup, just call and go. Perfect for one-off scripts and alerts.
```python
from eztelegramapi import send_message, edit_message, delete_message, forward_message

TOKEN   = "123456789:AABBCCDDEEFFaabbccddeeff-1234567890"
CHAT_ID = 987654321

msg_id = send_message(TOKEN, CHAT_ID, "Hello from EzTelegramAPI! 🚀")
edit_message(TOKEN, CHAT_ID, msg_id, "Updated message ✏️")
delete_message(TOKEN, CHAT_ID, msg_id)
forward_message(TOKEN, from_chat_id=CHAT_ID, to_chat_id=987654322, message_id=msg_id)
```

### 2. Class — no repetition
Set your token and chat_id once, never pass them again.
```python
from eztelegramapi import EzTelegramBot

bot = EzTelegramBot(token="123456789:AABBCCDDEEFFaabbccddeeff-1234567890", chat_id=987654321)

msg_id = bot.send_message("Hello from EzTelegramAPI! 🚀")
bot.edit_message(msg_id, "Updated message ✏️")
bot.delete_message(msg_id)
bot.forward_message(from_chat_id=987654322, message_id=msg_id)
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

### Functions

#### `send_message(token, chat_id, text, *, return_message_id=True)`
| Parameter | Type | Description |
|-----------|------|-------------|
| `token` | `str` | Your bot token from [@BotFather](https://t.me/BotFather) |
| `chat_id` | `int` | Target chat or user ID |
| `text` | `str` | Message text (supports emoji ✅) |
| `return_message_id` | `bool` | If `True` (default) returns `message_id`, else raw `Response` |

**Returns:** `int` (message_id) or `requests.Response`

---
#### `edit_message(token, chat_id, message_id, text)`
| Parameter | Type | Description |
|-----------|------|-------------|
| `token` | `str` | Your bot token from [@BotFather](https://t.me/BotFather) |
| `chat_id` | `int` | Target chat or user ID |
| `message_id` | `int` | ID of the message to edit |
| `text` | `str` | New message text |

**Returns:** `requests.Response`

---
#### `delete_message(token, chat_id, message_id)`
| Parameter | Type | Description |
|-----------|------|-------------|
| `token` | `str` | Your bot token from [@BotFather](https://t.me/BotFather) |
| `chat_id` | `int` | Target chat or user ID |
| `message_id` | `int` | ID of the message to delete |

**Returns:** `requests.Response`

---
#### `forward_message(token, from_chat_id, to_chat_id, message_id)`
| Parameter | Type | Description |
|-----------|------|-------------|
| `token` | `str` | Your bot token from [@BotFather](https://t.me/BotFather) |
| `from_chat_id` | `int` | Chat to forward the message from |
| `to_chat_id` | `int` | Chat to forward the message to |
| `message_id` | `int` | ID of the message to forward |

**Returns:** `int` (message_id of the forwarded message)

---
### Class

#### `EzTelegramBot(token, chat_id=None)`
| Parameter | Type | Description |
|-----------|------|-------------|
| `token` | `str` | Your bot token from [@BotFather](https://t.me/BotFather) |
| `chat_id` | `int \| None` | Default chat ID — can be overridden per call |

All methods mirror the functions above but without `token` and with optional `chat_id`.

---
## Examples

**Live progress update:**
```python
import time

msg_id = bot.send_message("⏳ Job started...")
time.sleep(5)
bot.edit_message(msg_id, "✅ Job finished!")
```
**Clean up after yourself:**
```python
msg_id = bot.send_message("⏳ Processing...")
do_work()
bot.delete_message(msg_id)
```
**Alert on error:**
```python
try:
    risky_operation()
except Exception as e:
    bot.send_message(f"🔴 Error: {e}")
```
**Cron job notification:**
```python
from datetime import datetime

now = datetime.now().strftime("%Y-%m-%d %H:%M")
bot.send_message(f"✅ Backup finished at {now}")
```
**Send to a different chat on the fly:**
```python
bot.send_message("Alert!", chat_id=OTHER_CHAT_ID)
```
---
## How to get your Chat ID
1. Start a chat with [@userinfobot](https://t.me/userinfobot)
2. Send `/start`
3. It replies with your numeric ID — use that as `chat_id`
---
## License
MIT