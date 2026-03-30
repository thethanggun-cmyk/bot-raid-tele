import os,asyncio,http.server,threading
from pyrogram import Client

def s():
    try:http.server.HTTPServer(("",10000),http.server.BaseHTTPRequestHandler).serve_forever()
    except:pass
threading.Thread(target=s,daemon=True).start()

async def main():
    api_id = int(os.getenv("API_ID"))
    api_hash = os.getenv("API_HASH")
    session = os.getenv("SESSION")
    noidung = os.getenv("NOIDUNG", "Raid!")
    
    app = Client("bot", session_string=session, api_id=api_id, api_hash=api_hash)
    async with app:
        print("BOT_CUA_THE_DA_CHAY_ROI")
        while True:
            try:
                await app.send_message("@lebanqcute", noidung)
                await asyncio.sleep(2)
            except:
                await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(main())
