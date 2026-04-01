import asyncio, aiohttp, random, os, threading
from flask import Flask

app = Flask('')
@app.route('/')
def home(): return "SMILE_V2_ONLINE"

def run_web():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

TOKEN = os.getenv("USER_TOKEN")
CH_IDS = os.getenv("CHANNEL_ID", "").split(",")
TAG_ID = os.getenv("TAG_ID", "")

# --- KHO ĐẠN 50+ CÂU KÈM ĐÚNG 2 CÁI CƯỜI KHẨY ---
SMILE = "=))) =)))"
DAN_DUOC = [
    f"Sủa mạnh lên con trai! 🐶 {SMILE}", f"Cay không em ơi? Cay thì khóc đi! {SMILE}", 
    f"Trình còi biến đi cho sạch mắt bố! {SMILE}", f"Bố mày chấp cả họ nhà mày luôn! {SMILE}", 
    f"Gáy to lên xem nào, sao im thế? {SMILE}", f"Nhìn cái gì? Cút về bú tí mẹ đi! {SMILE}",
    f"Loại mày chỉ xứng đáng làm nền cho bố thôi! {SMILE}", f"Nghiệp tụ vành môi đấy con ạ! {SMILE}",
    f"Sống sao cho người ta nể, đừng để người ta khinh! {SMILE}", f"Đừng có giả vờ không thấy nhé! {SMILE}",
    f"Tin nhắn nhảy nát máy chưa con trai? {SMILE}", f"Bố mày gõ nát cái inbox của mày luôn! {SMILE}",
    f"Sợ quá khóa máy rồi à? Nhát thế! {SMILE}", f"Trốn đâu cho thoát hả mày? {SMILE}",
    f"Check tin nhắn đi, quà của bố đấy! 📩 {SMILE}", f"Mày nghĩ mày là ai mà đòi chơi với bố? {SMILE}",
    f"Loại rác rưởi như mày thì chỉ có thế thôi! {SMILE}", f"Đừng để bố mày phải cáu nhé! {SMILE}",
    f"Càng sủa càng thấy mày ngu ra! {SMILE}", f"Ngu có đào tạo hay tự nhiên thế? {SMILE}",
    f"Mặt thì hãm, tính thì dở, đúng là cực phẩm! {SMILE}", f"Bố mày rảnh lắm, vã mày cả năm! {SMILE}",
    f"Cay đỏ dái chưa con trai? {SMILE}", f"Đừng có tốn công rep, bố dùng bot mà! {SMILE}",
    f"Chào con trai, bố lại đến thăm mày đây! {SMILE}", f"Thấy thông báo nhảy có run tay không? {SMILE}",
    f"Bố mày là nhất, mày là bét, rõ chưa? {SMILE}", f"Cứ sủa tiếp đi, bố đang nghe đây! {SMILE}",
    f"Trình độ thì thấp mà thái độ thì lồi lõm! {SMILE}", f"Về học lại cách làm người đi! {SMILE}",
    f"Nhìn mày diễn xiếc bố thấy buồn cười vcl! {SMILE}", f"Thằng hề của năm đây rồi! {SMILE}",
    f"Mày có gì ngoài cái mồm không? {SMILE}", f"Im lặng là vàng, mày im là nhục! {SMILE}",
    f"Bố mày vã cho tỉnh người ra nhé! {SMILE}", f"Chết lặng luôn rồi à? {SMILE}",
    f"Tội nghiệp, chắc đang run bần bật! {SMILE}", f"Đừng cố tỏ ra mình ổn, nhìn hèn lắm! {SMILE}",
    f"Bố mày thích thì bố mày vã thôi! {SMILE}", f"Thành phố này không có chỗ cho mày! {SMILE}",
    f"Mày là cái thá gì đòi đứng chung với bố? {SMILE}", f"Bớt ảo tưởng sức mạnh đi con ạ! {SMILE}",
    f"Càng nói càng thấy cái độ ngu vô tận! {SMILE}", f"Thôi, cút đi cho nước nó trong! {SMILE}",
    f"Bố mày tiễn mày một đoạn cho nhanh! {SMILE}", f"Lên đường bình an, đừng quay lại! {SMILE}",
    f"Bố mày gõ phím nhanh hơn mày thở! {SMILE}", f"Thấy tốc độ chưa? Sợ chưa? {SMILE}",
    f"Vã phát nào thấm phát đấy, sướng nhé! {SMILE}", f"Tận hưởng sự hành hạ của bố mày đi! {SMILE}",
    f"Mày chỉ là hạt cát trong sa mạc của bố! {SMILE}", f"Game là dễ, vã mày còn dễ hơn! {SMILE}",
    f"Cạn lời rồi à? Gáy tiếp đi! {SMILE}", f"Bố chờ mày từ sáng đến giờ đấy! {SMILE}"
]

async def fire(session, channel_id):
    target = channel_id.strip()
    headers = {"Authorization": TOKEN, "Content-Type": "application/json"}
    mention = f"<@{TAG_ID}> " if TAG_ID else ""
    
    while True:
        try:
            content = f"# {mention}{random.choice(DAN_DUOC)}"
            async with session.post(
                f"https://discord.com/api/v9/channels/{target}/messages",
                headers=headers,
                json={"content": content},
                timeout=5
            ) as r:
                if r.status == 429:
                    data = await r.json()
                    await asyncio.sleep(data.get('retry_after', 0.5))
                else:
                    await asyncio.sleep(0.08) # Tốc độ xả kịch kim
        except:
            await asyncio.sleep(0.2)

async def main():
    connector = aiohttp.TCPConnector(limit=50)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        for ch_id in CH_IDS:
            for _ in range(3): 
                tasks.append(fire(session, ch_id))
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    threading.Thread(target=run_web, daemon=True).start()
    print("--- ĐANG VÃ BẢN SMILE GỌN ---")
    try:
        asyncio.run(main())
    except:
        pass
