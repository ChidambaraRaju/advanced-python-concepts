import asyncio
from concurrent.futures import ProcessPoolExecutor

def encrypt(data): # runs in a separate process
    return f"🔒 {data[::-1]}"

async def main(): # runs in the main process
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, encrypt, "credit_card_1234")
        print(f"{result}")

if __name__ == "__main__":
    asyncio.run(main())