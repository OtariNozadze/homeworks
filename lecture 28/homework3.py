
import asyncio

async def squared_num(num):
    return num ** 2

async def even_nums(num):
    if num % 2 == 0:
        return await squared_num(num)

async def main():
    coroutine_tasks = [even_nums(i) for i in range(1, 11)]
    
    result = await asyncio.gather(*coroutine_tasks)
    
    for i in result:
        if i is not None:
            print(i)

if __name__ == '__main__':
    asyncio.run(main())

