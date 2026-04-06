import os, threading, time, requests, random
from flask import Flask

# --- WEB SERVER GIỮ RENDER ---
app = Flask('')
@app.route('/')
def home(): return "NGON_T_BIG_TEXT_ACTIVE"

def run_web():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

# --- DANH SÁCH 60 CÂU NGÔN T (CHỮ TO) ---
# Dùng dấu # ở đầu để biến thành chữ to trong Discord
VAN_MAU = [
    "# Sủa tiếp đi con chó con", "# Thoát thế đéo nào được", "# Gõ nhanh lên em ơi", 
    "# Mẹ mày gánh còng lưng", "# Cay lòi mắt chưa con", "# Nghiệp quật đấy em", 
    "# Trình còi đừng ra gió", "# Đú thế đéo nào được", "# Bố mày chấp cả họ mày", 
    "# Về học lại cách làm người", "# Sống lỗi thì ăn vả", "# Tắt máy đi ngủ đi con", 
    "# Nhìn mày thảm hại vcl", "# Cay cú là dấu hiệu thất bại", "# Đéo có cửa đâu", 
    "# Mày chỉ là hạt cát thôi", "# Tuổi tôm đòi đú", "# Gõ phím bằng chân à em", 
    "# Nhục chưa con trai", "# Bố mày đứng đây từ chiều", "# Mày là cái thá gì", 
    "# Đừng để bố mày nóng", "# Ngu thì chết bệnh tật gì", "# Nhìn lại gương đi", 
    "# Mày tuổi gì mà đòi cân", "# Bố cho mày nát máy luôn", "# Cháy máy chưa em ơi", 
    "# Thông báo nổ liên tục nhé", "# Khóc đi con", "# Đợi đấy bố chưa xong đâu", 
    "# Mày định chạy đi đâu", "# Cửa nào cho mày", "# Đừng có mà lấc cấc", 
    "# Bố mày vả cho rụng răng", "# Sống cho nó tử tế vào", "# Mày là rác rưởi thôi", 
    "# Hít khói đi con", "# Cố lên em sắp thắng rồi", "# Mày diễn hài à", 
    "# Nhìn mặt mày là thấy ghét", "# Bố mày khinh", "# Đéo ai thèm chấp mày", 
    "# Mày là đồ bỏ đi", "# Cút về máng lợn đi", "# Hổ báo trường mẫu giáo", 
    "# Mày ăn gì mà ngu thế", "# Bố mày chấp hết", "# Nổ máy chưa con trai", 
    "# Cay nồng nặc luôn", "# Đã bảo là đừng đú rồi", "# Trình mày chỉ đến thế", 
    "# Nhìn lại bản thân đi", "# Sủa to lên bố xem", "# Mày là cái loại gì", 
    "# Đừng có mà tinh tướng", "# Bố mày cân tất", "# Nhục mặt chưa con", 
    "# Về bú tí mẹ đi em", "# Đừng để bố mày ra tay", "# Mày chỉ là thằng hề"
]

# --- CẤU HÌNH ---
T1 = os.getenv("TOKEN_1")
T2 = os.getenv("TOKEN_2")
CID = os.getenv("CHANNEL_ID")
UID = os.getenv("TARGET_ID")
DLY = 0.2 # Tốc độ 0.2s

def raid(tk, tag):
    session = requests.Session()
    url = f"https://discord.com/api/v9/channels/{CID}/messages"
    headers = {"Authorization": tk, "Content-Type": "application/json"}
    
    while True:
        try:
            # Chọn ngẫu nhiên 1 câu trong 60 câu
            cau_chui = random.choice(VAN_MAU)
            # Cấu pháp: # <@ID> [Câu chửi] [Mã số]
            payload = {
                "content": f"{cau_chui} <@{UID}> | {random.getrandbits(16)}",
                "tts": False
            }
            r = session.post(url, headers=headers, json=payload, timeout=3)
            
            if r.status_code == 429:
                time.sleep(r.json().get('retry_after', 2))
            elif r.status_code in [401, 403]:
                break
        except:
            pass
        time.sleep(DLY)

if __name__ == "__main__":
    threading.Thread(target=run_web, daemon=True).start()
    if T1: threading.Thread(target=raid, args=(T1, "TK1"), daemon=True).start()
    if T2: threading.Thread(target=raid, args=(T2, "TK2"), daemon=True).start()
    while True: time.sleep(60)
