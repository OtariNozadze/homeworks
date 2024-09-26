import time
import asyncio

async def first_function():
    print("Start First Function")
    await asyncio.sleep(2)
    print("End First Function")

async def second_function():
    print("Start Secend Function")
    await asyncio.sleep(5)
    print("End Secend Function")

async def main():
    start_time = time.time()

    func_1 = asyncio.create_task(first_function())
    func_2 = asyncio.create_task(second_function())

    await func_1
    await func_2
    

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"elapsed time: {elapsed_time:.2f}")

if __name__ == '__main__':
    asyncio.run(main())


