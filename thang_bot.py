import os, asyncio, threading
import discord
from discord.ext import commands
from flask import Flask

# 1. MÁY THỞ CHO RENDER
app = Flask(__name__)
@app.route('/')
def home(): return "DISCORD BOT IS LIVE"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# 2. CẤU HÌNH BOT DISCORD
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Thông tin từ Render Settings
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID", 0)) # ID của kênh muốn spam
NOIDUNG = os.getenv("NOIDUNG", "RAID DISCORD!!!")

@bot.event
async def on_ready():
    print(f'--- BOT {bot.user} ĐÃ ONLINE ---')
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        while True:
            try:
                await channel.send(NOIDUNG)
                print(f"Đã vã Discord: {NOIDUNG}")
                await asyncio.sleep(1) # Tốc độ 1 giây/tin
            except Exception as e:
                print(f"Lỗi gửi tin: {e}")
                await asyncio.sleep(5)
    else:
        print("LỖI: Không tìm thấy Channel ID. Hãy kiểm tra lại!")

if __name__ == "__main__":
    threading.Thread(target=run_web, daemon=True).start()
    bot.run(TOKEN)
