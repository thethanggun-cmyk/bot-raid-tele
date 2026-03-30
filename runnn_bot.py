import os, asyncio, threading
from pyrogram import Client
from flask import Flask

# "Máy thở" giúp Render giữ bot sống
app = Flask(__name__)
@app.route('/')
def home(): return "LIVE"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

async def start_bot():
    # Lấy thông tin từ cấu hình Render
    api_id = int(os.getenv("API_ID"))
    api_hash = os.getenv("API_HASH")
    session = os.getenv("SESSION")
    target = "@lebanqcute"
    text = os.getenv("NOIDUNG", "Raid!")
    
    bot = Client("my_bot", session_string=session, api_id=api_id, api_hash=api_hash)
    
    async with bot:
        print("--- BOT ĐÃ LÊN SÀN ---")
        while True:
            try:
                await bot.send_message(target, text)
                print(f"Vừa vã xong: {text}")
                await asyncio.sleep(2)
            except Exception as e:
                print(f"Lỗi: {e}")
                await asyncio.sleep(10)

if __name__ == "__main__":
    # Chạy web server ở luồng riêng
    threading.Thread(target=run_web, daemon=True).start()
    
    # KHẮC PHỤC LỖI EVENT LOOP TRÊN RENDER
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    
    loop.run_until_complete(start_bot())
