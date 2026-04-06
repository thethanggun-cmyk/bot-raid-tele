import os, time, requests, random, threading
from flask import Flask

app = Flask('')
@app.route('/')
def home(): return "BOT_MUOT_MA"

# --- BỘ NGÔN T ---
NGON_T = ["# Sủa tiếp đi con chó con", "# Cay lòi mắt chưa con", "# Bố mày chấp cả họ mày", "# Nhục chưa con trai", "# Cháy máy chưa em ơi", "# Đợi đấy bố chưa xong đâu", "# Trình còi đừng ra gió", "# Đú thế đéo nào được", "# Về học lại cách làm người", "# Sống lỗi thì ăn vả", "# Tắt máy đi ngủ đi con", "# Nhìn mày thảm hại vcl", "# Cay cú là dấu hiệu thất bại", "# Đéo có cửa đâu", "# Mày chỉ là hạt cát thôi", "# Tuổi tôm đòi đú", "# Gõ phím bằng chân à em", "# Bố mày đứng đây từ chiều", "# Mày là cái thá gì", "# Đừng để bố mày nóng", "# Ngu thì chết bệnh tật gì", "# Nhìn lại gương đi", "# Mày tuổi gì mà đòi cân", "# Bố cho mày nát máy luôn", "# Thông báo nổ liên tục nhé", "# Khóc đi con", "# Mày định chạy đi đâu", "# Cửa nào cho mày", "# Đừng có mà láo nhé", "# Bố mày vả vỡ mồm", "# Mày là đồ rác rưởi", "# Cút ngay cho khuất mắt"]

T1 = os.getenv("TOKEN_1")
CID = os.getenv("CHANNEL_ID")
UID = os.getenv("TARGET_ID")

def raid():
    time.sleep(5)
    s = requests.Session()
    s.headers.update({"Authorization": T1, "Content-Type": "application/json"})
    url = f"https://discord.com/api/v9/channels/{CID}/messages"
    
    print("🚀 ĐANG KHAI HỎA...")
    while True:
        try:
            txt = random.choice(NGON_T)
            # Dùng 1 ký tự ẩn duy nhất để lách, mắt người KHÔNG THỂ thấy
            payload = {"content": f"{txt} <@{UID}> \u200b"}
            
            r = s.post(url, json=payload, timeout=5)
            
            if r.status_code == 200:
                print("✅")
            elif r.status_code == 429: # Nếu bị Discord nhắc nhở thì nghỉ tí
                wait = r.json().get('retry_after', 1)
                time.sleep(wait)
            else:
                print(f"🆘 {r.status_code}")
                
        except:
            pass
        
        # Tốc độ này là "vừa miếng" nhất để không bị đứng
        time.sleep(0.8) 

if __name__ == "__main__":
    # Import threading chuẩn để không lỗi status 1
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=10000), daemon=True).start()
    raid()
