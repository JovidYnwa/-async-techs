import asyncio
from datetime import datetime
from multiprocessing.connection import wait
import time


# def make_smth():
#     time.sleep(2)

#The way of calling normal function
# make_smth()
start_time = datetime.now()
print("start time equals to ", start_time)
async def async_func_one():
    print('hello moto')
    await asyncio.sleep(3)
    print("End of first asynct func")

async def async_func_two():
    print('mercedec benz the best or nothing')
    await asyncio.sleep(6)
    print("End of second async func")


#Calling asynfunction first way
# asyncio.run(make_smth_one())
# asyncio.run(make_smth_two())

#Calling async func second way
async def main():
    task1 = asyncio.create_task(async_func_one())
    task2 = asyncio.create_task(async_func_two())
    await task1
    await task2


asyncio.run(main())

print('compilation time equals to ', datetime.now() - start_time)