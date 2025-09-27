# AsyncIO in Python

## What is AsyncIO?
`asyncio` is a Python library used to write **concurrent code using the async/await syntax**.  
It allows you to handle **I/O-bound** and **high-level structured network code** more efficiently without creating multiple threads or processes.

Instead of blocking the program while waiting for slow operations (like reading from a file, making an API call, or querying a database), `asyncio` lets your program **do other work in the meantime**.

---

## How AsyncIO Works (Behind the Scenes)
- AsyncIO is built on top of an **event loop**.
- The event loop is responsible for:
  1. **Scheduling tasks** (coroutines).
  2. **Switching between tasks** when one is waiting (e.g., for I/O).
  3. **Resuming tasks** when the waiting operation is done.

### Flow of Execution
1. You define coroutines using `async def`.
2. You run them with the event loop using `asyncio.run()` or `await`.
3. When a coroutine hits an `await` (like `await asyncio.sleep(1)`), control is handed back to the event loop.
4. The event loop can then run another coroutine while the first one is "waiting".
5. Once the waiting is over, the coroutine resumes from where it paused.

👉 This switching is **cooperative** (tasks yield control explicitly with `await`), not automatic like in threading.

---

## AsyncIO vs Threading vs Multiprocessing

| Feature | AsyncIO | Threading | Multiprocessing |
|---------|---------|-----------|-----------------|
| **Type of tasks best suited for** | I/O-bound (e.g., web requests, DB queries, file I/O) | I/O-bound (but with blocking calls) | CPU-bound (e.g., heavy calculations, ML training) |
| **Execution model** | Single-threaded, event loop, cooperative multitasking | Multiple threads within one process | Multiple processes, each with its own Python interpreter |
| **Context switching** | Very cheap (no OS overhead, just switching coroutines) | Costly (OS schedules threads) | Costliest (process creation, inter-process communication) |
| **Parallelism** | Concurrency, but not true parallelism (still one thread running tasks) | Limited by GIL (not true parallelism for CPU tasks) | True parallelism (each process has its own GIL) |
| **Memory usage** | Light (all coroutines share same memory) | Moderate (threads share memory but need locks) | Heavy (each process has its own memory space) |
| **Synchronization** | Not much needed (single-threaded) | Needs locks/semaphores for shared state | Uses IPC (queues, pipes, shared memory) |
| **Ease of debugging** | Easier (deterministic switching with `await`) | Harder (race conditions, deadlocks) | Harder (IPC issues, higher overhead) |

---