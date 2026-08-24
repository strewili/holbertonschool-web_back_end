# Python - Async

Asynchronous programming in Python with `asyncio`: writing coroutines with
`async`/`await`, running many of them concurrently, wrapping them in tasks,
and measuring the runtime to prove the concurrency is real.

## Learning objectives

- `async` and `await` syntax
- How to execute an async program with `asyncio`
- How to run concurrent coroutines
- How to create `asyncio` tasks
- How to use the `random` module

## Requirements

- Ubuntu 20.04 LTS, `python3` (version 3.9)
- All files start with `#!/usr/bin/env python3` and end with a new line
- All files are executable, code follows `pycodestyle` (2.5.*)
- All functions and coroutines are type-annotated and documented

## Files

| File | Description |
| --- | --- |
| `0-basic_async_syntax.py` | `wait_random(max_delay=10)` — waits a random delay and returns it |
| `1-concurrent_coroutines.py` | `wait_n(n, max_delay)` — spawns `wait_random` n times, returns delays in ascending order |
| `2-measure_runtime.py` | `measure_time(n, max_delay)` — average runtime of `wait_n` |
| `3-tasks.py` | `task_wait_random(max_delay)` — returns an `asyncio.Task` |
| `4-tasks.py` | `task_wait_n(n, max_delay)` — same as `wait_n` but using tasks |

## Note on ordering

`wait_n` returns a sorted list without ever calling `sort()`. The delays come
out in ascending order naturally because `asyncio.as_completed` yields each
coroutine as it finishes, and the shortest delay always finishes first.
