import asyncio
from random import randint

async def print_nums(num, delay):
    print(f"function with argument {num} and delay {delay} start")
    await asyncio.sleep(delay)
    print(num)

async def main():
    coroutine_lst = []
    for i in range(1, 11):
        coroutine_lst.append(print_nums(i, randint(1, 5)))
    
    await asyncio.gather(*coroutine_lst)

if __name__ == '__main__':
    asyncio.run(main())

    