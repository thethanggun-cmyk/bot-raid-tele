import discord
import os, asyncio, random, string
from flask import Flask
from threading import Thread

# --- WEB SERVER GIỮ UPTIME ---
app = Flask('')
@app.route('/')
def home(): return "DANG KIEM TRA LOI..."

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# --- 50+ CÂU NGÔN THẤT HỌC ---
MESSAGES = [
    "Mày là cái loại thất học, mở mồm ra là thấy sự ngu dốt!",
    "Trình độ văn hóa thấp kém thì đừng có ra đây gáy với bố!",
    "Mày là bằng chứng sống của việc học chưa hết lớp 1!",
    "Cái loại vô học như mày chỉ đáng làm rác thải xã hội thôi!",
    "Mày gõ phím mà chữ nghĩa lộn xộn như cái đầu thất học của mày!",
    "Mày bị đuổi học từ mẫu giáo đúng không con trai? Nhìn ngu quá!",
    "Loại thất học như mày thì biết cái gì là tư cách?",
    "Học thức không có thì tốt nhất là ngậm mồm vào cho sang!",
    "Nhìn cách mày gõ chữ là biết cả đời chưa đụng vào quyển sách!",
    "Mày là sự sỉ nhục của ngành giáo dục nước nhà!",
    "Mày gáy nữa đi thằng vô học? Sao im thin thít thế?",
    "Bố mày dạy cho mày một bài học về lễ độ này thằng thất học!",
    "Mày là đồ bỏ đi, từ nhân cách đến học thức đều bằng không!",
    "Tiễn thằng thất học như mày về nơi an nghỉ cho sạch Discord!"
]

client = discord.Client()

async def raid_engine():
    print("--- [BUOC 1] DANG KHOI DONG ENGINE ---")
    await client.wait_until_ready()
    print(f"--- [BUOC 2] DA DANG NHAP THANH CONG: {client.user} ---")
    
    try:
        # Kiểm tra biến môi trường
        token_env = os.getenv('DISCORD_TOKEN')
        c_id_env = os.getenv('CHANNEL_ID')
        t_id_env = os.getenv('TARGET_USER_ID')

        if not token_env: print("!!! LOI: THIEU DISCORD_TOKEN TRONG TAB ENVIRONMENT !!!")
        if not c_id_env: print("!!! LOI: THIEU CHANNEL_ID TRONG TAB ENVIRONMENT !!!")
        if not t_id_env: print("!!! LOI: THIEU TARGET_USER_ID TRONG TAB ENVIRONMENT !!!")

        channel_id = int(c_id_env.strip())
        target_id = t_id_env.strip()
        
        print(f"--- [BUOC 3] DANG TIM KENH ID: {channel_id} ---")
        channel = await client.fetch_channel(channel_id)
        print(f"--- [BUOC 4] DA TIM THAY KENH: {channel.name}. BAT DAU RAID! ---")
        
        while True:
            try:
                msg = random.choice(MESSAGES)
                hidden = "\u200b" * random.randint(1, 10)
                content = f"# {msg} \n<@{target_id}>{hidden}"
                
                await channel.send(content)
                print(f"-> [OK] Da va: {msg[:15]}...")
            except discord.Forbidden:
                print("!!! LOI: ACC KHONG CO QUYEN NHAN TIN TRONG KENH NAY (BI BAN HOAC BI CAM) !!!")
            except Exception as e:
                print(f"!!! LOI GUI TIN NHAN: {e} !!!")
                await asyncio.sleep(2)
            
            await asyncio.sleep(0.35)
            
    except Exception as e:
        print(f"!!! LOI NGHIEM TRONG: {e} !!!")

@client.event
async def on_ready():
    client.loop.create_task(raid_engine())

if __name__ == "__main__":
    Thread(target=run_web).start()
    token = os.getenv('DISCORD_TOKEN', '').strip()
    print("--- [BUOC 0] DANG DANG NHAP VOI TOKEN ---")
    try:
        client.run(token, bot=False)
    except Exception as e:
        print(f"!!! LOI DANG NHAP: {e} !!!")
