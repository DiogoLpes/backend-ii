import asyncio

async def task_function(name, delay):
    await asyncio.sleep(delay)
    return f"{name} completed"

async def main():
    tasks = []
    for i in range(3):
        task = asyncio.create_task(task_function(f"Task {i+1}", i+1))
        tasks.append(task)

    results = []
    for task in tasks:
        try:
            result = await asyncio.wait_for(task, timeout=2.0)
            results.append(result)
        except asyncio.TimeoutError:
            print(f"Task {task} timed out")
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                print(f"Task {task} was cancelled")

    print(results)

asyncio.run(main())