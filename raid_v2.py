import os, time, requests, random
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask('')

@app.route('/')
def home():
    return "BOT_DANG_XA_DAN_KHONG_NGHI"

# --- BỘ NGÔN T ---
NGON_T = ["# Sủa tiếp đi con chó con", "# Cay lòi mắt chưa con", "# Bố mày chấp cả họ mày", "# Nhục chưa con trai", "# Cháy máy chưa em ơi", "# Đợi đấy bố chưa xong đâu", "# Trình còi đừng ra gió", "# Đú thế đéo nào được", "# Về học lại cách làm người", "# Sống lỗi thì ăn vả", "# Tắt máy đi ngủ đi con", "# Nhìn mày thảm hại vcl", "# Cay cú là dấu hiệu thất bại", "# Đéo có cửa đâu", "# Mày chỉ là hạt cát thôi", "# Tuổi tôm đòi đú", "# Gõ phím bằng chân à em", "# Bố mày đứng đây từ chiều", "# Mày là cái thá gì", "# Đừng để bố mày nóng", "# Ngu thì chết bệnh tật gì", "# Nhìn lại gương đi", "# Mày tuổi gì mà đòi cân", "# Bố cho mày nát máy luôn", "# Thông báo nổ liên tục nhé", "# Khóc đi con", "# Mày định chạy đi đâu", "# Cửa nào cho mày", "# Đừng có mà láo nhé", "# Bố mày vả vỡ mồm", "# Mày là đồ rác rưởi", "# Cút ngay cho khuất mắt"]

T1 = os.getenv("TOKEN_1")
CID = os.getenv("CHANNEL_ID")
UID = os.getenv("TARGET_ID")

# Tạo Session để bắn cực nhanh
session = requests.Session()
session.headers.update({"Authorization": T1, "Content-Type": "application/json"})
url = f"https://discord.com/api/v9/channels/{CID}/messages"

def bullet():
    """Hàm bắn 1 tin nhắn"""
    try:
        payload = {"content": f"{random.choice(NGON_T)} <@{UID}>"}
        r = session.post(url, json=payload, timeout=5)
        if r.status_code == 200:
            print("✅")
        elif r.status_code == 429:
            print("⚠️ Discord chặn tốc độ, tự động chờ...")
    except Exception as e:
        print(f"🆘 Lỗi: {e}")

# Thiết lập lịch bắn: Cứ mỗi 0.5 giây bắn 1 phát (Tốc độ này cực mượt trên Render)
sched = BackgroundScheduler(daemon=True)
sched.add_job(bullet, 'interval', seconds=0.5)
sched.start()

if __name__ == "__main__":
    # Chạy Flask ở luồng chính để Render thấy bot vẫn đang "Live"
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
