import os, threading, time, httpx, random
from flask import Flask

app = Flask('')
@app.route('/')
def home(): return "NGON_T_READY"

# --- CONFIG ---
T1 = os.getenv("TOKEN_1")
T2 = os.getenv("TOKEN_2")
CID = os.getenv("CHANNEL_ID")
UID = os.getenv("TARGET_ID")

NGON_40 = [
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

def raid_engine(token, name):
    if not token:
        print(f"⚠️ {name}: KHÔNG CÓ TOKEN TRONG ENVIRONMENT!")
        return

    # Sử dụng HTTP/2 để tăng tốc và ổn định
    client = httpx.Client(http2=True, headers={"Authorization": token, "Content-Type": "application/json"})
    url = f"https://discord.com/api/v9/channels/{CID}/messages"
    
    print(f"🚀 {name}: ĐANG KẾT NỐI ĐẾN KÊNH {CID}...")

    while True:
        try:
            content = f"{random.choice(NGON_40)} <@{UID}> | {random.getrandbits(16)}"
            response = client.post(url, json={"content": content, "tts": False}, timeout=10)
            
            # ÉP HIỆN LOG DÙ THÀNH CÔNG HAY THẤT BẠI
            if response.status_code == 200:
                print(f"✅ {name}: ĐÃ BẮN THÀNH CÔNG!")
            elif response.status_code == 429:
                wait = response.json().get('retry_after', 2)
                print(f"⚠️ {name}: BỊ CHẶN TỐC ĐỘ, NGHỈ {wait}S")
                time.sleep(wait)
            else:
                print(f"❌ {name}: LỖI {response.status_code} - {response.text}")
        
        except Exception as e:
            print(f"🆘 {name}: LỖI KẾT NỐI: {e}")
        
        time.sleep(0.4) # Delay 0.4 cho ổn định, tránh bay acc quá nhanh

if __name__ == "__main__":
    # Luồng Web Server
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=10000), daemon=True).start()
    
    # Kích hoạt Raid
    time.sleep(3)
    t1 = threading.Thread(target=raid_engine, args=(T1, "TK1"))
    t2 = threading.Thread(target=raid_engine, args=(T2, "TK2"))
    
    t1.start()
    t2.start()
    t1.join()
    t2.join()
