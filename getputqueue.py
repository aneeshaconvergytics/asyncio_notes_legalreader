q = asyncio.Queue()

async def get_data (data):
    while True:
        await asyncio.sleep(1)
        await q.put(data[idx,:])
        idx += 1
        #Each row of data is read every second. 

async def run_algorithm ():
    while True:
        data_read = await q.get()
        #I do something here with the read data