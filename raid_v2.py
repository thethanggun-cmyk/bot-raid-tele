import os, time, requests, random, threading
from concurrent.futures import ThreadPoolExecutor
from flask import Flask

app = Flask('')
@app.route('/')
def home(): return "MAX_FIREPOWER_ACTIVE"

# --- BỘ NGÔN T ---
NGON_T = ["# Sủa tiếp đi con chó con", "# Cay lòi mắt chưa con", "# Bố mày chấp cả họ mày", "# Nhục chưa con trai", "# Cháy máy chưa em ơi", "# Đợi đấy bố chưa xong đâu", "# Trình còi đừng ra gió", "# Đú thế đéo nào được", "# Về học lại cách làm người", "# Sống lỗi thì ăn vả", "# Tắt máy đi ngủ đi con", "# Nhìn mày thảm hại vcl", "# Cay cú là dấu hiệu thất bại", "# Đéo có cửa đâu", "# Mày chỉ là hạt cát thôi", "# Tuổi tôm đòi đú", "# Gõ phím bằng chân à em", "# Bố mày đứng đây từ chiều", "# Mày là cái thá gì", "# Đừng để bố mày nóng", "# Ngu thì chết bệnh tật gì", "# Nhìn lại gương đi", "# Mày tuổi gì mà đòi cân", "# Bố cho mày nát máy luôn", "# Thông báo nổ liên tục nhé", "# Khóc đi con", "# Mày định chạy đi đâu", "# Cửa nào cho mày", "# Đừng có mà láo nhé", "# Bố mày vả vỡ mồm", "# Mày là đồ rác rưởi", "# Cút ngay cho khuất mắt"]

T1 = os.getenv("TOKEN_1")
CID = os.getenv("CHANNEL_ID")
UID = os.getenv("TARGET_ID")

# Thiết lập Session để nã cho nhanh
s = requests.Session()
s.headers.update({"Authorization": T1, "Content-Type": "application/json"})
url = f"https://discord.com/api/v9/channels/{CID}/messages"

def bullet():
    """Hàm bắn 1 viên đạn"""
    try:
        payload = {"content": f"{random.choice(NGON_T)} <@{UID}>"}
        r = s.post(url, json=payload, timeout=3)
        if r.status_code == 200:
            print("✅")
        elif r.status_code == 429:
            # Nếu bị Discord chặn thì nghỉ đúng số giây nó yêu cầu
            wait = r.json().get('retry_after', 1)
            time.sleep(wait)
    except:
        pass

def raid_executor():
    """Vòng lặp nã đạn liên tục với 5 họng súng"""
    print("🚀 ĐANG XẢ ĐẠN TỐC ĐỘ BÀN THỜ...")
    # Tạo 5 luồng bắn cùng lúc để nhân 5 tốc độ
    with ThreadPoolExecutor(max_workers=5) as executor:
        while True:
            executor.submit(bullet)
            # Khoảng nghỉ cực ngắn giữa các đợt bắn
            time.sleep(0.1)

if __name__ == "__main__":
    # Luồng giữ Render không bị sập
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=10000), daemon=True).start()
    # Khai hỏa
    raid_executor()
