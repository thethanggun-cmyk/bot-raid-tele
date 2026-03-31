import threading, random, requests, time, os
from flask import Flask

app = Flask('')
@app.route('/')
def home(): return "RAID_50_READY"

def run_web():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

TOKEN = os.getenv("USER_TOKEN")
CH_ID = os.getenv("CHANNEL_ID")
TAG_ID = os.getenv("TAG_ID")

# KHO ĐẠN 50+ CÂU CHỌN LỌC
DAN_DUOC = [
    "Vã cho tỉnh người chưa con trai? 👊", "Sủa tiếp đi xem nào! 🐶", "Câm nín luôn rồi à? 👀",
    "Raid cho cháy máy nhé! 🔥", "Trình còi thì dựa cột mà nghe!", "Cay lắm đúng không? 🌶️",
    "Nhìn tin nhắn nhảy hoa mắt chưa?", "Bố mày chấp cả họ nhà mày!", "Cút ngay cho khuất mắt tao!",
    "Gáy to lên xem nào! 🐔", "Thằng nhóc ác này láo thật!", "Khóc đi đừng ngại ngùng! 😭",
    "Dậy mà đi kiếm tiền mua thuốc trị cay đi!", "Trình độ có hạn mà khốn nạn có thừa!", 
    "Não ngắn thì đừng có múa phím!", "Tao vả cho không trượt phát nào!", "Càng sủa càng thấy ngu!", 
    "Tuổi gì mà đòi so găng? 🥊", "Nhìn cái bản mặt hãm tài chưa?", "Bố mày là nỗi khiếp sợ của mày!", 
    "Cay cú phát điên lên đi!", "Loại mày chỉ xứng đáng làm nền thôi!", "Học cách làm người trước đi!", 
    "Cái loại mạt hạng như mày!", "Nhìn tao diễn xiếc trên phím này!", "Nghỉ tay uống tí nước đi con!", 
    "Sợ quá nên chạy mất dép rồi à?", "Đừng có thách thức giới hạn của tao!", "Bố mày đang rảnh, chiều mày tới bến!", 
    "Tắt máy đi ngủ đi, gáy gì tầm này!", "Tao là cơn ác mộng của mày tối nay!", "Quỳ xuống xin lỗi đi thì tao tha!", 
    "Đã ngu còn hay đánh đu với đời!", "Nhục nhã chưa con trai cưng?", "Để tao dạy cho mày biết thế nào là lễ độ!", 
    "Tao gõ phím nhanh hơn mày thở đấy!", "Mày không thoát được đâu con trai!", "Cay đỏ dái rồi chứ gì?", 
    "Tao vã cho méo mồm bây giờ!", "Đừng có mà lấc cấc với đại ca!", "Mày là cái thá gì mà đòi gáy?", 
    "Bố mày cười vào mặt mày một cái này!", "Hít thở sâu vào cho đỡ cay!", "Mày là con kiến còn tao là xe lu!", 
    "Cảm giác bị áp đảo thấy sao hả con?", "Mày là cái rốn của sự ngu dốt!", "Sủa mạnh lên, tao chưa nghe rõ!", 
    "Tầm này thì cứu sao được nữa!", "Mày là định nghĩa của sự thất bại!", "Tao tiễn mày về nơi xa lắm nhé!", 
    "Chết lặng luôn rồi hả con?", "Đừng có mà cố đấm ăn xôi!", "Mày không thấy nhục à?", 
    "Mơ đi con, kiếp sau nhé!", "Biến đi cho sạch chỗ này!", "Mày là kẻ thua cuộc vĩnh viễn!"
]

def raid():
    if not TOKEN or not CH_ID:
        print("LỖI: Thiếu TOKEN hoặc CHANNEL_ID!")
        return

    headers = {"Authorization": TOKEN, "Content-Type": "application/json"}
    mention = f"<@{TAG_ID}> " if TAG_ID else ""
    pool = DAN_DUOC.copy()
    random.shuffle(pool)
    
    print(f"--- ĐANG VÃ CHANNEL {CH_ID} ---")
    
    while True:
        try:
            if not pool:
                pool = DAN_DUOC.copy()
                random.shuffle(pool)
            
            content = f"# {mention}{pool.pop()}"
            r = requests.post(f"https://discord.com/api/v9/channels/{CH_ID}/messages", headers=headers, json={"content": content})
            
            if r.status_code == 429:
                time.sleep(r.json().get('retry_after', 5))
            elif r.status_code == 401:
                print("LỖI: Token văng!")
                break
            else:
                print(f"Đã vã: {content}")
            
            time.sleep(0.2)
        except Exception as e:
            print(f"Lỗi: {e}")
            time.sleep(1)

if __name__ == "__main__":
    threading.Thread(target=run_web, daemon=True).start()
    raid()
