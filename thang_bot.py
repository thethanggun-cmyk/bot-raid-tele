import os, asyncio, threading, random
import discord
from discord.ext import commands
from flask import Flask

# 1. MÁY THỞ RENDER (GIỮ BOT LIVE 24/7)
app = Flask(__name__)
@app.route('/')
def home(): return "BOT DISCORD #MAX_SIZE IS LIVE"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# 2. CẤU HÌNH BOT
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# THÔNG TIN LẤY TỪ RENDER SETTINGS
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID", 0))
TARGET_USER_ID = os.getenv("TARGET_USER_ID", "") 

# 3. DANH SÁCH NGÔN (MÀY CHỈ CẦN GHI CHỮ, BOT TỰ THÊM # VÀ **)
DANH_SACH_VA = [
    "Vã cho tỉnh người nè! 👊",
    "Chưa chừa hả bưởi? 🍋",
    "Sủa tiếp đi xem nào! 🐶",
    "Câm nín luôn rồi à? 🤫",
    "Raid cho cháy máy nhé! 🔥",
    "Tầm này thì đỡ bằng nồi! 🥘",
    "Bot Thế Thắng đang chiếm đóng cái box này!!!",
    "Khóc đi đừng ngại ngùng! 😭",
    "Sân chơi này là của tao! 😎",
    "Gáy to lên xem nào! 🐔",
    "Nhìn cái gì mà nhìn? 👁️",
    "Trình còi thì dựa cột mà nghe!",
    "Một vả là bay màu nhé con trai!",
    "Box này giờ là địa bàn của bot tao!",
    "Câm mồm vào cho thiên hạ thái bình!",
    "Có gan thì đừng có chạy nhé!",
    "Tuổi gì mà đòi so găng? 🥊",
    "Chắc đang cay lắm đây! 🌶️",
    "Thôi, về nhà bú tí mẹ đi con!",
    "Raid đến khi nào sập server mới thôi!",
    "Đừng múa rìu qua mắt thợ nhé!",
    "Cút ngay cho khuất mắt tao!",
    "Game này tao làm chủ rồi!",
    "Nhìn tin nhắn nhảy mà hoa mắt chưa?",
    "Đang làm gì đấy? Đợi bị vã à? 😂"
]

@bot.event
async def on_ready():
    print(f'--- BOT {bot.user} ĐÃ ONLINE - CHẾ ĐỘ CHỮ TO ---')
    channel = bot.get_channel(CHANNEL_ID)
    
    if channel:
        print(f"Đang xả đạn vào kênh: {CHANNEL_ID}")
        while True:
            try:
                # Bốc ngẫu nhiên 1 câu
                cau_chui = random.choice(DANH_SACH_VA)
                
                # TỰ ĐỘNG ÉP ĐỊNH DẠNG # **NỘI DUNG** (CHỮ TO + ĐẬM)
                ngon_sieu_to = f"# **{cau_chui}**"
                
                # Nếu có ID mục tiêu thì tag nó vào đầu
                if TARGET_USER_ID:
                    noidung_gui = f"<@{TARGET_USER_ID}> {ngon_sieu_to}"
                else:
                    noidung_gui = ngon_sieu_to
                
                await channel.send(noidung_gui)
                print(f"Đã vã siêu to: {cau_chui}")
                
                # Tốc độ 1.2 giây (vừa đủ gắt, vừa an toàn)
                await asyncio.sleep(1.2) 
            except Exception as e:
                print(f"Lỗi: {e}")
                await asyncio.sleep(5)
    else:
        print("LỖI: Không tìm thấy Channel ID! Kiểm tra lại bên Render Settings.")

if __name__ == "__main__":
    threading.Thread(target=run_web, daemon=True).start()
    bot.run(TOKEN)
