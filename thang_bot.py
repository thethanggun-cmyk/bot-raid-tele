import threading, random, requests, time, os
from flask import Flask

# 1. TẠO MÁY THỞ ĐỂ TREO TRÊN RENDER 24/7
app = Flask('')
@app.route('/')
def home(): return "ACC_USER_RAID_0.2S_RUNNING"
def run_web():
    # Render yêu cầu port phải linh hoạt
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# 2. THÔNG TIN TÀI KHOẢN VÀ KÊNH (ĐÃ NẠP SẴN)
TOKEN = "MTQ4NzQwMTU0NzQ4OTg2OTkzNg.G4TFsN.WvBGba5obVzXXxUn2PhtXTjdiStRz3aNCl1Ryw"
CH_ID = "1487470700100059329"

# KHO NGÔN SIÊU GẮT - VÃ CHO TỈNH
NGON = [
    "Vã cho tỉnh người nè! 👊", "Sủa tiếp đi xem nào! 🐶", "Câm nín luôn rồi à? 🤫",
    "Trình còi thì dựa cột mà nghe!", "Raid cho cháy máy nhé! 🔥", "Chưa chừa hả bưởi? 🍋",
    "Sân chơi này là của tao! 😎", "Nhìn cái gì mà nhìn? 👁️", "Càng sủa càng thấy ngu!",
    "Bố mày chấp cả họ nhà mày luôn!", "Câm họng lại không tao vả lệch hàm!",
    "Dậy mà đi kiếm tiền mua thuốc trị cay đi!", "Về nhà bú tí mẹ đi con!", "Tuổi gì mà đòi so găng? 🥊",
    "Chắc đang cay lắm đây! 🌶️", "Đừng múa rìu qua mắt thợ!", "Game này tao làm chủ rồi!",
    "Nhìn tin nhắn nhảy hoa mắt chưa?", "Cút ngay cho khuất mắt tao!", "Gáy to lên xem nào! 🐔",
    "Thằng nhóc ác này láo thật!", "Tao vã cho không trượt phát nào!", "Khóc đi đừng ngại ngùng! 😭"
]

def raid():
    print("--- ĐANG VÃ CHANNEL 1487470700100059329 ---")
    # Headers giả lập trình duyệt để tránh bị Discord quét sớm
    headers = {
        "Authorization": TOKEN,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    while True:
        try:
            ngon = random.choice(NGON)
            payload = {"content": f"# **{ngon}**"}
            
            # Gửi tin nhắn qua API v9
            r = requests.post(f"https://discord.com/api/v9/channels/{CH_ID}/messages", headers=headers, json=payload)
            
            if r.status_code == 429: # Bị giới hạn tốc độ (Rate Limit)
                wait = r.json().get('retry_after', 5)
                print(f"Spam quá nhanh, nghỉ {wait}s để lách luật...")
                time.sleep(wait)
            elif r.status_code == 401:
                print("LỖI: Token acc đã bị văng hoặc sai!")
                break
            elif r.status_code == 403:
                print("LỖI: Acc không có quyền nhắn tin trong kênh này!")
                break
            else:
                print(f"Đã vã: {ngon}")
            
            # TỐC ĐỘ 0.2S (5 TIN/GIÂY)
            time.sleep(0.2)
            
        except Exception as e:
            print(f"Lỗi hệ thống: {e}")
            time.sleep(1)

if __name__ == "__main__":
    # Chạy máy thở ở luồng phụ
    threading.Thread(target=run_web, daemon=True).start()
    # Chạy raid ở luồng chính
    raid()
