import os, time, requests, random, threading
from flask import Flask

app = Flask('')
@app.route('/')
def home(): return "BOT_DANG_XU_DEP_DOI_THU"

# --- BỘ NGÔN T ---
NGON_T = ["# Sủa tiếp đi con chó con", "# Cay lòi mắt chưa con", "# Bố mày chấp cả họ mày", "# Nhục chưa con trai", "# Cháy máy chưa em ơi", "# Đợi đấy bố chưa xong đâu", "# Trình còi đừng ra gió", "# Đú thế đéo nào được", "# Về học lại cách làm người", "# Sống lỗi thì ăn vả", "# Tắt máy đi ngủ đi con", "# Nhìn mày thảm hại vcl", "# Cay cú là dấu hiệu thất bại", "# Đéo có cửa đâu", "# Mày chỉ là hạt cát thôi", "# Tuổi tôm đòi đú", "# Gõ phím bằng chân à em", "# Bố mày đứng đây từ chiều", "# Mày là cái thá gì", "# Đừng để bố mày nóng", "# Ngu thì chết bệnh tật gì", "# Nhìn lại gương đi", "# Mày tuổi gì mà đòi cân", "# Bố cho mày nát máy luôn", "# Thông báo nổ liên tục nhé", "# Khóc đi con", "# Mày định chạy đi đâu", "# Cửa nào cho mày", "# Đừng có mà láo nhé", "# Bố mày vả vỡ mồm", "# Mày là đồ rác rưởi", "# Cút ngay cho khuất mắt"]

T1 = os.getenv("TOKEN_1")
CID = os.getenv("CHANNEL_ID")
UID = os.getenv("TARGET_ID")

def raid():
    # Dùng Session để giữ kết nối cực chắc, đạn bay không bị trễ
    s = requests.Session()
    s.headers.update({
        "Authorization": T1,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    })
    url = f"https://discord.com/api/v9/channels/{CID}/messages"
    
    print("🚀 ĐANG KHAI HỎA RÀO RÀO...")
    
    while True:
        try:
            # Chọn câu ngẫu nhiên + Tag tên
            payload = {"content": f"{random.choice(NGON_T)} <@{UID}>"}
            
            # Gửi tin nhắn
            r = s.post(url, json=payload, timeout=5)
            
            if r.status_code == 200:
                print("✅")
            elif r.status_code == 429:
                # Nếu dính Rate Limit, nghỉ đúng số giây Discord yêu cầu rồi nã tiếp
                retry_after = r.json().get('retry_after', 1)
                print(f"⚠️ Nghỉ {retry_after}s...")
                time.sleep(retry_after + 0.1)
            elif r.status_code in [401, 403]:
                print("❌ Token hỏng hoặc không có quyền vào kênh")
                break
            else:
                print(f"🆘 Lỗi: {r.status_code}")
                
        except Exception as e:
            print(f"🆘 Lỗi kết nối: {e}")
            time.sleep(1)
            
        # Tốc độ 0.3s - Đây là mức "vàng" để nã liên tục mà không bị treo Render
        time.sleep(0.3)

if __name__ == "__main__":
    # Luồng giữ Web sống cho Render
    t = threading.Thread(target=lambda: app.run(host='0.0.0.0', port=10000))
    t.daemon = True
    t.start()
    
    # Chạy lệnh Raid ngay lập tức
    raid()
