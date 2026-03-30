import os, asyncio, threading
from pyrogram import Client
from flask import Flask

# Web server giả để Render không tắt bot
app_web = Flask(__name__)
@app_web.route('/')
def home(): return "Bot is live!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app_web.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)

async def start_bot():
    api_id = int(os.getenv("API_ID"))
    api_hash = os.getenv("API_HASH")
    session = os.getenv("SESSION")
    noidung = os.getenv("NOIDUNG", "Raid!")
    
    bot = Client("my_bot", session_string=session, api_id=api_id, api_hash=api_hash)
    
    async with bot:
        print("--- BOT CHÍNH THỨC LIVE ---")
        while True:
            try:
                await bot.send_message("@lebanqcute", noidung)
                print(f"Đã vã: {noidung}")
                await asyncio.sleep(2)
            except Exception as e:
                print(f"Lỗi: {e}")
                await asyncio.sleep(10)

if __name__ == "__main__":
    threading.Thread(target=run_web, daemon=True).start()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(start_bot())
