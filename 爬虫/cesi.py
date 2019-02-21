import aiohttp
import asyncio


url='http://dev.xiaoxiangyoupin.com:1111/v2/user/gustLogin.json'
async def index(*args):
    async with aiohttp.ClientSession() as session:
        print(args)
        async with session.get(url=args[0][0],params=args[0][1]) as resqu:
            print(resqu.status)
            print(await resqu.text())
data = {'mobile': 18501787063, 'verCode': 888888}
args=(url,data)

task=asyncio.ensure_future(index(args))
loop=asyncio.get_event_loop()
loop.run_until_complete(task)
#print(task)