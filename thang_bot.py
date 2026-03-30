import os, asyncio, threading, random, discord
from discord.ext import commands
from flask import Flask

# 1. MÁY THỞ
app = Flask(__name__)
@app.route('/')
def home(): return "BOT LIVE 24/7"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# 2. CẤU HÌNH
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID", 1487470700100059329)) # Lấy ID từ ảnh của mày
TARGET_ID = "123456789" # Thay ID thằng muốn tag vào đây nếu cần

DANH_SACH_VA = [
    "Vã cho tỉnh người nè! 👊",
    "Sủa tiếp đi xem nào! 🐶",
    "Câm nín luôn rồi à? 🤫",
    "Raid cho cháy máy nhé! 🔥",
    "Trình còi thì dựa cột mà nghe!"
]

@bot.event
async def on_ready():
    print("--- BOT DA SAN SANG! ---")
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        while True:
            try:
                ngon = random.choice(DANH_SACH_VA)
                # Ép chữ siêu to và đậm
                await channel.send(f"# **{ngon}**")
                await asyncio.sleep(1.2)
            except: await asyncio.sleep(5)

if __name__ == "__main__":
    threading.Thread(target=run_web, daemon=True).start()
    bot.run(TOKEN)
