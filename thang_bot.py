import threading, random, requests, time, os
from flask import Flask

app = Flask('')
@app.rowte('/')
def home(): return "SUPER_RAID_100_READY"

def run_web():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

# LẤY BIẾN TỪ RENDER ENVIRONMENT
TOKEN = os.getenv("USER_TOKEN")
CH_ID = os.getenv("CHANNEL_ID")
TAG_ID = os.getenv("TAG_ID")

# KHO NGÔN "VÃ" 100+ CÂU - XOAY VÒNG CỰC GẮT
DAN_DUOC = [
    "Vã cho tỉnh người chưa con trai? 👊", "Sủa tiếp đi xem nào! 🐶", "Câm nín luôn rồi à? 👀",
    "Raid cho cháy máy nhé! 🔥", "Trình còi thì dựa cột mà nghe!", "Cay lắm đúng không? 🌶️",
    "Nhìn tin nhắn nhảy hoa mắt chưa?", "Bố mày chấp cả họ nhà mày!", "Cút ngay cho khuất mắt tao!",
    "Gáy to lên xem nào! 🐔", "Thằng nhóc ác này láo thật!", "Khóc đi đừng ngại ngùng! 😭",
    "Game này tao làm chủ rồi!", "Dậy mà đi kiếm tiền mua thuốc trị cay đi!", "Bú tí mẹ xong chưa?",
    "Trình độ có hạn mà khốn nạn có thừa!", "Não ngắn thì đừng có múa phím!", "Tao vả cho không trượt phát nào!",
    "Càng sủa càng thấy ngu!", "Tuổi gì mà đòi so găng? 🥊", "Nhìn cái bản mặt hãm tài chưa?",
    "Bố mày là nỗi khiếp sợ của mày!", "Chạy đâu cho thoát khỏi trận mưa tin nhắn?", "Cay cú phát điên lên đi!",
    "Loại mày chỉ xứng đáng làm nền thôi!", "Học cách làm người trước khi học cách gáy!", "Đừng để tao phải ra tay gắt hơn!",
    "Cái loại mạt hạng như mày!", "Nhìn tao diễn xiếc trên phím này!", "Mày có bao nhiêu acc bố mày vã hết!",
    "Nghỉ tay uống tí nước cho đỡ khô cổ đi con!", "Sợ quá nên chạy mất dép rồi à?", "Đừng có thách thức giới hạn của tao!",
    "Bố mày đang rảnh, chiều mày tới bến!", "Mày nghĩ mày là ai ở cái server này?", "Tắt máy đi ngủ đi, gáy gì tầm này!",
    "Mẹ mày gọi về ăn cơm kìa, đừng ở đây gáy nữa!", "Tao là cơn ác mộng của mày tối nay!", "Quỳ xuống xin lỗi đi thì tao tha!",
    "Đã ngu còn hay đánh đu với đời!", "Cái trình của mày chỉ đến thế thôi à?", "Nhục nhã chưa con trai cưng?",
    "Để tao dạy cho mày biết thế nào là lễ độ!", "Nhìn tin nhắn mà thấy run rẩy chưa?", "Tao gõ phím nhanh hơn mày thở đấy!",
    "Loại mày chỉ làm trò hề cho thiên hạ thôi!", "Mày không thoát được đâu con trai!", "Cay đỏ dái rồi chứ gì?",
    "Tao vã cho méo mồm bây giờ!", "Đừng có mà lấc cấc với đại ca!", "Mày là cái thá gì mà đòi gáy?",
    "Nhìn mày thảm hại thực sự đấy!", "Bố mày cười vào mặt mày một cái này!", "Cố gắng lên, sắp chạm tới gót chân tao rồi!",
    "Mày có thấy sự bất lực hiện rõ trên mặt không?", "Hít thở sâu vào cho đỡ cay!", "Tao mà dừng thì mày mới được sống nhé!",
    "Mày là con kiến còn tao là xe lu!", "Cảm giác bị áp đảo thấy sao hả con?", "Tao gõ phím bằng chân cũng hơn mày!",
    "Đừng để tao phải dùng đến 1% công lực!", "Mày là cái rốn của sự ngu dốt!", "Mày sinh ra để làm bao cát cho tao à?",
    "Khóc to lên, tao thích nghe tiếng khóc của mày!", "Sủa mạnh lên, tao chưa nghe rõ!", "Mày càng gáy tao càng vã gắt!",
    "Tầm này thì cứu sao được nữa!", "Mày là định nghĩa của sự thất bại!", "Đừng có mà láo nháo với bố!",
    "Tao chấp mày gọi thêm cả lò nhà mày vào đấy!", "Mày có thấy run sợ trước sức mạnh này không?", "Mày là rác rưởi của cái server này!",
    "Tao tiễn mày về nơi xa lắm nhé!", "Chết lặng luôn rồi hả con?", "Đừng có mà cố đấm ăn xôi!",
    "Mày là minh chứng cho việc ngu không có giới hạn!", "Tao chửi mày mà tao còn thấy ngại cho mày!", "Mày không thấy nhục à?",
    "Nhìn mày tấu hài vui phết đấy!", "Tiếp tục đi, tao đang xem mày diễn này!", "Mày nghĩ mày thắng được tao sao?",
    "Mơ đi con, kiếp sau nhé!", "Tao là bức tường thành mày không bao giờ vượt qua!", "Mày chỉ là hạt cát trong sa mạc của tao thôi!",
    "Đừng có mà múa rìu qua mắt thợ!", "Mày là cái bóng của tao thôi con ạ!", "Hết thuốc chữa rồi, về vườn đi!",
    "Tao sẽ cho mày biết thế nào là địa ngục!", "Mày đang đối đầu với ai mày biết không?", "Tao là ông nội của mày đấy!",
    "Mày là đứa trẻ lạc lối trong trận chiến này!", "Nhìn mày xanh mặt rồi kìa!", "Bố mày vã cho một phát là bay màu luôn!",
    "Mày không đủ tư cách để nói chuyện với tao!", "Biến đi cho sạch chỗ này!", "Mày là vết nhơ của xã hội!",
    "Tao sẽ làm cho mày phải hối hận vì đã sinh ra!", "Mày là kẻ thua cuộc vĩnh viễn!", "Đừng có mà mơ tưởng hão huyền!"
]

def raid():
    if not TOKEN or not CH_ID:
        print("LỖI: Thiếu TOKEN hoặc CHANNEL_ID trong Environment!")
        return

    headers = {
        "Authorization": TOKEN,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }
    
    mention = f"<@{TAG_ID}> " if TAG_ID else ""
    
    # Tạo danh sách tạm để không lặp lại cho đến khi hết kho
    current_pool = DAN_DUOC.copy()
    random.shuffle(current_pool)
    
    print(f"--- ĐANG VÃ CHANNEL {CH_ID} VỚI 100+ CÂU CHỬI ---")
    
    while True:
        try:
            if not current_pool:
                current_pool = DAN_DUOC.copy()
                random.shuffle(current_pool)
            
            cau_chui = current_pool.pop()
            content = f"# {mention}{cau_chui}"
            payload = {"content": content}
            
            r = requests.post(f"https://discord.com/api/v9/channels/{CH_ID}/messages", headers=headers, json=payload)
            
            if r.status_code == 429:
                wait = r.json().get('retry_after', 5)
                time.sleep(wait)
            elif r.status_code == 401:
                print("LỖI: Token văng!")
                break
            else:
                print(f"Đã vã: {cau_chui}")
            
            time.sleep(0.2) # Tốc độ 0.2s siêu tốc
            
        except Exception as e:
            print(f"Lỗi: {e}")
            time.sleep(1)

if __name__ == "__main__":
    threading.Thread(target=run_web, daemon=True).start()
    raid()
