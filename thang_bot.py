import os, asyncio, threading, random, discord
from flask import Flask

# 1. MÁY THỞ ĐỂ TREO RENDER 24/7
app = Flask('')
@app.route('/')
def home(): return "BOT RAID SUPER SPEED 0.2s"
def run(): app.run(host='0.0.0.0', port=10000)

# 2. CẤU HÌNH BOT
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

TK = os.getenv("DISCORD_TOKEN")
CH_ID = int(os.getenv("CHANNEL_ID", 1487470700100059329))

# 3. KHO ĐẠN NGÔN (TỰ ĐỘNG ÉP CHỮ TO + ĐẬM)
NGON_LIST = [
    "Vã cho tỉnh người nè! 👊", "Sủa tiếp đi xem nào! 🐶", "Câm nín luôn rồi à? 🤫",
    "Trình còi thì dựa cột mà nghe!", "Raid cho cháy máy nhé! 🔥", "Chưa chừa hả bưởi? 🍋",
    "Sân chơi này là của tao! 😎", "Nhìn cái gì mà nhìn? 👁️", "Một vả là bay màu nhé!",
    "Box này giờ là địa bàn của tao!", "Câm mồm vào cho thiên hạ thái bình!",
    "Tuổi gì mà đòi so găng? 🥊", "Chắc đang cay lắm đây! 🌶️", "Về nhà bú tí mẹ đi con!",
    "Đừng múa rìu qua mắt thợ!", "Game này tao làm chủ rồi!", "Nhìn tin nhắn nhảy hoa mắt chưa?",
    "Đang làm gì đấy? Đợi bị vã à? 😂", "Cút ngay cho khuất mắt tao!", "Gáy to lên xem nào! 🐔",
    "Thằng nhóc ác này láo thật!", "Bố mày chấp cả họ nhà mày luôn!", "Câm họng lại không tao vả lệch hàm!",
    "Trình độ này chỉ đáng xách dép!", "Càng sủa càng thấy ngu!", "Bớt cái thói gáy bẩn đi con!",
    "Tao vã cho không trượt phát nào!", "Khóc đi đừng ngại ngùng! 😭", "Mày là cái thá gì mà đòi chơi?",
    "Não phẳng thì đừng có ra gió!", "Đã bảo rồi, đừng đùa với lửa!", "Nhìn mày trông thảm hại quá!",
    "Sủa mạnh lên, tao chưa nghe rõ!", "Đúng là đồ vô dụng!", "Về tập thêm vài năm nữa đi!",
    "Tao đứng đây từ chiều, sao chưa thấy gáy?", "Định chạy làng à con trai?", "Đừng để tao phải dùng biện pháp mạnh!",
    "Cứ tiếp tục đi, bot tao rảnh lắm!", "Tốc độ này đã đủ phê chưa?", "Chuẩn bị sập server chưa con?",
    "Mày chỉ là con tép trên bàn tiệc!", "Đừng cố tỏ ra nguy hiểm!", "Tao chấp mày cả lò luôn đấy!",
    "Câm như hến rồi à? Tội nghiệp thế!", "Dậy mà đi kiếm tiền mua thuốc trị cay đi!"
]

@bot.event
async def on_ready():
    print(f"--- BOT {bot.user} ĐANG VÃ VỚI TỐC ĐỘ 0.2S ---")
    c = bot.get_channel(CH_ID)
    if c:
        while True:
            try:
                # Ép định dạng chữ siêu to và đậm
                msg = f"# **{random.choice(NGON_LIST)}**"
                await c.send(msg)
                
                # TỐC ĐỘ BÀN THỜ: 0.2 GIÂY
                await asyncio.sleep(0.2) 
            except discord.errors.HTTPException as e:
                if e.status == 429: # Bị Discord chặn vì nhanh quá
                    print("Bị Rate Limit rồi, nghỉ 5s...")
                    await asyncio.sleep(5)
            except Exception as e:
                print(f"Lỗi: {e}")
                await asyncio.sleep(2)

if __name__ == "__main__":
    threading.Thread(target=run).start()
    bot.run(TK)
