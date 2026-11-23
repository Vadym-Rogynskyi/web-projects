import asyncio
from playwright.async_api import async_playwright
items={"counting-house":"counting-house/","first-paycheck-simulator":"web-projects/first-paycheck-simulator/","pace-gap-planner":"web-projects/pace-gap-planner/","road-to-the-10k":"web-projects/road-to-the-10k/","ten-kilometres-down":"web-projects/ten-kilometres-down/","web-projects":"web-projects/","apex-market-pulse":"apex-market-pulse/","atmos":"atmos-3d-weather/"}
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
        pg=await b.new_page(viewport={"width":1280,"height":800})
        for k,u in items.items():
            try: await pg.goto("http://127.0.0.1:8765/"+u,wait_until="load",timeout=15000)
            except Exception as e: print(k,'load',str(e)[:60])
            await pg.wait_for_timeout(3000); await pg.screenshot(path=f"/home/claude/shots/{k}.png"); print(k)
        await b.close()
asyncio.run(main())
