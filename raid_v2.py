import os, time, requests, random, multiprocessing
from flask import Flask

app = Flask('')
@app.route('/')
def home(): return "OK"

# --- 70 CÂU NGÔN ---
NGON_T = ["# Sủa tiếp đi con chó con", "# Cay lòi mắt chưa con", "# Bố mày chấp cả họ mày", "# Nhục chưa con trai", "# Cháy máy chưa em ơi", "# Đợi đấy bố chưa xong đâu", "# Trình còi đừng ra gió", "# Đú thế đéo nào được", "# Về học lại cách làm người", "# Sống lỗi thì ăn vả", "# Tắt máy đi ngủ đi con", "# Nhìn mày thảm hại vcl", "# Cay cú là dấu hiệu thất bại", "# Đéo có cửa đâu", "# Mày chỉ là hạt cát thôi", "# Tuổi tôm đòi đú", "# Gõ phím bằng chân à em", "# Bố mày đứng đây từ chiều", "# Mày là cái thá gì", "# Đừng để bố mày nóng", "# Ngu thì chết bệnh tật gì", "# Nhìn lại gương đi", "# Mày tuổi gì mà đòi cân", "# Bố cho mày nát máy luôn", "# Thông báo nổ liên tục nhé", "# Khóc đi con", "# Mày định chạy đi đâu", "# Cửa nào cho mày", "# Đừng có mà lấc cấc", "# Bố mày vả cho rụng răng", "# Sống cho nó tử tế vào", "# Mày là rác rưởi thôi", "# Hít khói đi con", "# Cố lên em sắp thắng rồi", "# Mày diễn hài à", "# Nhìn mặt mày là thấy ghét", "# Bố mày khinh", "# Đéo ai thèm chấp mày", "# Mày là đồ bỏ đi", "# Cút về máng lợn đi", "# Trình mày tuổi gì", "# Sủa to lên bố nghe", "# Nhục nhã ê chề chưa", "# Khóc lóc cái gì", "# Bố mày cân tất nhé", "# Đừng có mà tinh tướng", "# Về bú tí mẹ đi con", "# Nhìn mày hài vcl", "# Cay nồng nặc luôn", "# Sủa tiếp bố xem nào", "# Đã bảo đừng đú rồi", "# Mày là cái loại gì", "# Cửa nào cho mày đú", "# Não mày để trang trí à", "# Nhìn mặt là thấy ngu", "# Bố khinh loại mày", "# Sống sao cho nó sạch", "# Đừng để bố mày ra tay", "# Mày chỉ là thằng hề", "# Hổ báo với ai", "# Nhục mặt cha mẹ mày", "# Về chuồng đi con lợn", "# Gõ phím nhanh lên em", "# Sắp sập nguồn chưa", "# Thông báo nổ banh xác", "# Đừng có mà láo nhé", "# Bố mày vả vỡ mồm", "# Mày là đồ rác rưởi", "# Cút ngay cho khuất mắt", "# Đừng để bố mày cáu", "# Trình mày chỉ thế thôi", "# Hết thuốc chữa rồi em"]

def start_raid():
    # Lấy biến trực tiếp trong hàm để tránh lỗi
    t = os.getenv("TOKEN_1")
    c = os.getenv("CHANNEL_ID")
    u = os.getenv("TARGET_ID")
    
    s = requests.Session()
    s.headers.update({"Authorization": t, "Content-Type": "application/json"})
    url = f"https://discord.com/api/v9/channels/{c}/messages"
    
    print("🔥 LUỒNG RAID ĐÃ KÍCH HOẠT!")
    while True:
        try:
            payload = {"content": f"{random.choice(NGON_T)} <@{u}> | {random.getrandbits(16)}"}
            r = s.post(url, json=payload, timeout=5)
            if r.status_code == 200:
                print("✅")
            elif r.status_code == 429:
                time.sleep(r.json().get('retry_after', 1))
            else:
                print(f"❌ {r.status_code}")
        except: pass
        time.sleep(0.2)

if __name__ == "__main__":
    # Chạy Web Server
    p1 = multiprocessing.Process(target=lambda: app.run(host='0.0.0.0', port=10000))
    p1.start()
    
    # Chạy Raid ngay lập tức
    start_raid()
