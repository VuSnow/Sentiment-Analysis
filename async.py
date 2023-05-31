import asyncio

async def process_item(item):
    # Perform some asynchronous operation with the item
    await asyncio.sleep(10)  # Simulating an asynchronous operation
    print(f"Processed item: {item}")

async def main():
    items = [1, 2, 3, 4, 5]

    # Create a list of coroutines
    coroutines = [process_item(item) for item in items]

    # Execute the coroutines concurrently
    await asyncio.gather(*coroutines)

# Run the main function in an event loop
asyncio.run(main())
