import os, asyncio, threading
from telethon import TelegramClient
from telethon.sessions import StringSession
from flask import Flask

# 1. TẠO MÁY THỞ CHO RENDER (FLASK)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot Telethon is Live!"

def run_web():
    # Render sẽ cấp một cái PORT tự động, phải chạy Flask trên đó
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)

# 2. HÀM CHẠY BOT RAID
async def start_bot():
    # Lấy biến môi trường từ Settings bên Render
    api_id = int(os.getenv("API_ID"))
    api_hash = os.getenv("API_HASH")
    session = os.getenv("SESSION")
    noidung = os.getenv("NOIDUNG", "Raid!")
    target = "@lebanqcute"

    # Khởi tạo Telethon Client
    client = TelegramClient(StringSession(session), api_id, api_hash)
    
    try:
        await client.connect()
        # Kiểm tra xem có đăng nhập được không
        if not await client.is_user_authorized():
            print("LỖI: Mã SESSION của mày không hợp lệ hoặc đã hết hạn!")
            return

        print("--- BOT TELETHON CHÍNH THỨC LIVE ---")
        
        while True:
            try:
                # Gửi tin nhắn đến thằng kia
                await client.send_message(target, noidung)
                print(f"Đã vã bằng Telethon: {noidung}")
                # Nghỉ 2 giây rồi vã tiếp
                await asyncio.sleep(2)
            except Exception as e:
                print(f"Lỗi khi đang gửi: {e}")
                await asyncio.sleep(10)
                
    except Exception as e:
        print(f"Lỗi kết nối nghiêm trọng: {e}")

# 3. ĐIỀU KHIỂN CHÍNH
if __name__ == "__main__":
    # Chạy web server ở luồng riêng (Thread)
    threading.Thread(target=run_web, daemon=True).start()
    
    # Tạo vòng lặp mới để tránh lỗi "There is no current event loop"
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    try:
        loop.run_until_complete(start_bot())
    except KeyboardInterrupt:
        pass
