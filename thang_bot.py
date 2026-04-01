import threading, random, requests, time, os
from flask import Flask

# --- GIỮ CHO RENDER LUÔN CHẠY ---
app = Flask('')
@app.route('/')
def home(): return "TURBO_RAID_V5_ONLINE"

def run_web():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

# --- CẤU HÌNH BIẾN MÔI TRƯỜNG ---
TOKEN = os.getenv("USER_TOKEN")
# Mày có thể nhập 1 hoặc nhiều ID cách nhau bằng dấu phẩy ở Render
CH_IDS = os.getenv("CHANNEL_ID", "").split(",") 
TAG_ID = os.getenv("TAG_ID", "")

# --- KHO ĐẠN DƯỢC 50+ CÂU CHỬI KHỊA ---
DAN_DUOC = [
    "Sủa mạnh lên con trai! 🐶", "Cay không em ơi? Cay thì khóc đi!", 
    "Trình còi biến đi cho sạch mắt bố!", "Bố mày chấp cả họ nhà mày luôn!", 
    "Gáy to lên xem nào, sao im thin thít thế?", "Nhìn cái gì? Cút về bú tí mẹ đi!",
    "Loại mày chỉ xứng đáng làm nền cho bố thôi!", "Nghiệp tụ vành môi đấy con ạ!",
    "Sống sao cho người ta nể, chứ đừng để người ta khinh!", "Đừng có giả vờ không thấy nhé!",
    "Tin nhắn nhảy nát máy chưa con trai?", "Bố mày gõ nát cái inbox của mày luôn!",
    "Sợ quá khóa máy rồi à? Nhát thế!", "Trốn đâu cho thoát hả mày?",
    "Check tin nhắn đi, quà của bố đấy! 📩", "Mày nghĩ mày là ai mà đòi chơi với bố?",
    "Loại rác rưởi như mày thì chỉ có thế thôi!", "Đừng để bố mày phải cáu nhé!",
    "Càng sủa càng thấy mày ngu ra!", "Ngu có đào tạo hay tự nhiên thế?",
    "Mặt thì hãm, tính thì dở, đúng là cực phẩm!", "Bố mày rảnh lắm, treo bot vã mày cả năm!",
    "Cay đỏ dái chưa con trai?", "Đừng có tốn công rep, bố mày dùng bot mà!",
    "Chào con trai, bố lại đến thăm mày đây!", "Thấy thông báo nhảy có run tay không?",
    "Bố mày là nhất, mày là bét, rõ chưa?", "Cứ sủa tiếp đi, bố đang nghe đây!",
    "Trình độ thì thấp mà thái độ thì lồi lõm!", "Về học lại cách làm người đi rồi hãy gáy!",
    "Nhìn mày diễn xiếc bố thấy buồn cười vcl!", "Thằng hề của năm đây rồi!",
    "Mày có gì ngoài cái mồm không?", "Im lặng là vàng, nhưng mày im là nhục!",
    "Bố mày vã cho tỉnh người ra nhé!", "Chết lặng luôn rồi à?",
    "Tội nghiệp, chắc đang run bần bật ở đầu dây bên kia!", "Đừng cố tỏ ra mình ổn, nhìn hèn lắm!",
    "Bố mày thích thì bố mày vã thôi, ý kiến gì?", "Thành phố này chật chội, nhưng không có chỗ cho mày!",
    "Mày là cái thá gì mà đòi đứng chung hàng với bố?", "Bớt ảo tưởng sức mạnh đi con ạ!",
    "Càng nói càng thấy cái độ ngu của mày nó vô tận!", "Thôi, cút đi cho nước nó trong!",
    "Bố mày tiễn mày một đoạn cho nhanh nhé!", "Lên đường bình an, đừng quay lại đây!",
    "Bố mày gõ phím nhanh hơn mày thở đấy!", "Thấy tốc độ chưa? Sợ chưa?",
    "Vã phát nào thấm phát đấy, sướng nhé!", "Cứ tận hưởng sự hành hạ của bố mày đi!",
    "Mày chỉ là hạt cát trong sa mạc của bố thôi!", "Game là dễ, vã mày còn dễ hơn!",
    "Cạn lời rồi à? Sao không gáy tiếp đi?", "Bố chờ mày từ sáng đến giờ đấy!"
]

def vax_turbo():
    headers = {"Authorization": TOKEN, "Content-Type": "application/json"}
    mention = f"<@{TAG_ID}> " if TAG_ID else ""
    
    while True:
        for channel_id in CH_IDS:
            target = channel_id.strip()
            if not target: continue
            
            try:
                # Thêm số ngẫu nhiên để Discord không chặn tin nhắn trùng lặp
                content = f"{mention}{random.choice(DAN_DUOC)} #{random.randint(100, 999)}"
                
                r = requests.post(
                    f"https://discord.com/api/v9/channels/{target}/messages", 
                    headers=headers, 
                    json={"content": content},
                    timeout=5
                )
                
                if r.status_code == 429:
                    retry = r.json().get('retry_after', 2)
                    print(f"Bị giới hạn! Nghỉ {retry}s...")
                    time.sleep(retry)
                elif r.status_code == 200 or r.status_code == 201:
                    print(f"Đã vã vào {target}: {content}")
                else:
                    print(f"Lỗi {r.status_code} tại {target}")
                
            except Exception as e:
                print(f"Lỗi hệ thống: {e}")
                time.sleep(1)
        
        # Tốc độ nghỉ giữa các lượt xả (0.1s là cực nhanh rồi)
        time.sleep(0.1)

if __name__ == "__main__":
    # Chạy Web giữ server
    threading.Thread(target=run_web, daemon=True).start()
    
    # Chạy 3 luồng vã song song (Turbo)
    print("--- HỆ THỐNG TURBO RAID ĐANG KHỞI ĐỘNG ---")
    for i in range(3):
        threading.Thread(target=vax_turbo, daemon=True).start()
    
    # Giữ script không tắt
    while True:
        time.sleep(10)
