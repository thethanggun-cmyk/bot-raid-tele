import os, threading, time, requests, random
from flask import Flask

# --- WEB SERVER GIỮ RENDER SỐNG ---
app = Flask('')
@app.route('/')
def home(): return "NGON_T_40_PLUS_READY"

def run_web():
    try: app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
    except: pass

# --- DANH SÁCH 40 CÂU NGÔN T (CHỮ TO #) ---
NGON_T = [
    "# Sủa tiếp đi con chó con", "# Cay lòi mắt chưa con", "# Bố mày chấp cả họ mày",
    "# Nhục chưa con trai", "# Cháy máy chưa em ơi", "# Đợi đấy bố chưa xong đâu",
    "# Trình còi đừng ra gió", "# Đú thế đéo nào được", "# Về học lại cách làm người",
    "# Sống lỗi thì ăn vả", "# Tắt máy đi ngủ đi con", "# Nhìn mày thảm hại vcl",
    "# Cay cú là dấu hiệu thất bại", "# Đéo có cửa đâu", "# Mày chỉ là hạt cát thôi",
    "# Tuổi tôm đòi đú", "# Gõ phím bằng chân à em", "# Bố mày đứng đây từ chiều",
    "# Mày là cái thá gì", "# Đừng để bố mày nóng", "# Ngu thì chết bệnh tật gì",
    "# Nhìn lại gương đi", "# Mày tuổi gì mà đòi cân", "# Bố cho mày nát máy luôn",
    "# Thông báo nổ liên tục nhé", "# Khóc đi con", "# Mày định chạy đi đâu",
    "# Cửa nào cho mày", "# Đừng có mà lấc cấc", "# Bố mày vả cho rụng răng",
    "# Sống cho nó tử tế vào", "# Mày là rác rưởi thôi", "# Hít khói đi con",
    "# Cố lên em sắp thắng rồi", "# Mày diễn hài à", "# Nhìn mặt mày là thấy ghét",
    "# Bố mày khinh", "# Đéo ai thèm chấp mày", "# Mày là đồ bỏ đi", "# Cút về máng lợn đi"
]

# --- CẤU HÌNH ---
T1 = os.getenv("TOKEN_1")
T2 = os.getenv("TOKEN_2")
CID = os.getenv("CHANNEL_ID")
UID = os.getenv("TARGET_ID")
DLY = 0.2 # Tốc độ 0.2s/tin

def raid(tk, name):
    session = requests.Session()
    url = f"https://discord.com/api/v9/channels/{CID}/messages"
    headers = {"Authorization": tk, "Content-Type": "application/json"}
    print(f"🚀 [{name}] ĐANG NÃ ĐẠN...")
    
    while True:
        try:
            txt = random.choice(NGON_T)
            # Cấu pháp: # [Câu chửi] <@ID_Mục_Tiêu> | [Mã_Số]
            payload = {
                "content": f"{txt} <@{UID}> | {random.getrandbits(16)}",
                "tts": False
            }
            r = session.post(url, headers=headers, json=payload, timeout=5)
            
            if r.status_code == 200:
                print(f"✅ [{name}] GỬI THÀNH CÔNG")
            elif r.status_code == 429:
                wait = r.json().get('retry_after', 2)
                time.sleep(wait)
            elif r.status_code in [401, 403]:
                print(f"❌ [{name}] TOKEN DIE HOẶC THIẾU QUYỀN")
                break
        except: pass
        time.sleep(DLY)

if __name__ == "__main__":
    threading.Thread(target=run_web, daemon=True).start()
    if T1: threading.Thread(target=raid, args=(T1, "TK1"), daemon=True).start()
    if T2: threading.Thread(target=raid, args=(T2, "TK2"), daemon=True).start()
    while True: time.sleep(10)
