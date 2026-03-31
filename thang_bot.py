import threading, random, requests, time, os
from flask import Flask

# 1. MÁY THỞ CHO RENDER
app = Flask('')
@app.route('/')
def home(): return "BOT_DA_LEN_SAN"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# 2. LẤY MỌI THỨ TỪ ENVIRONMENT (KHO BÍ MẬT CỦA RENDER)
TOKEN = os.getenv("USER_TOKEN")
CH_ID = os.getenv("CHANNEL_ID")

# KHO NGÔN "VÃ"
NGON = [
    "# **Vã cho tỉnh người! 👊**", "# **Sủa tiếp đi! 🐶**", 
    "# **Câm nín luôn! 🤫**", "# **Raid cháy máy! 🔥**",
    "# **Trình còi biến đi!**", "# **Cay lắm đúng không? 🌶️**"
]

def raid():
    if not TOKEN or not CH_ID:
        print("LỖI: Thiếu USER_TOKEN hoặc CHANNEL_ID trong Environment!")
        return

    headers = {
        "Authorization": TOKEN,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    print(f"--- ĐANG VÃ CHANNEL {CH_ID} ---")
    
    while True:
        try:
            payload = {"content": random.choice(NGON)}
            r = requests.post(f"https://discord.com/api/v9/channels/{CH_ID}/messages", headers=headers, json=payload)
            
            if r.status_code == 429:
                wait = r.json().get('retry_after', 5)
                time.sleep(wait)
            elif r.status_code == 401:
                print("LỖI: Token sai hoặc bị văng!")
                break
            elif r.status_code == 404:
                print("LỖI: Không tìm thấy ID kênh này!")
                break
            else:
                print(f"Đã vã vào kênh {CH_ID}")
            
            time.sleep(0.2) # Tốc độ 0.2s
            
        except Exception as e:
            print(f"Lỗi: {e}")
            time.sleep(1)

if __name__ == "__main__":
    threading.Thread(target=run_web, daemon=True).start()
    raid()
