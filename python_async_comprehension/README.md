# Python - Async Comprehension

Asynchronous generators and comprehensions in Python: producing values over
time with `async yield`, collecting them with an `async for` comprehension,
and running several comprehensions in parallel with `asyncio.gather`.

## Learning objectives

- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators

## Requirements

- Ubuntu 20.04 LTS, `python3` (version 3.9)
- All files start with `#!/usr/bin/env python3` and end with a new line
- All files are executable, code follows `pycodestyle` (2.5.*)
- All functions and coroutines are type-annotated and documented

## Files

| File | Description |
| --- | --- |
| `0-async_generator.py` | `async_generator()` — yields 10 random floats, waiting 1s before each |
| `1-async_comprehension.py` | `async_comprehension()` — collects those 10 values with an async comprehension |
| `2-measure_runtime.py` | `measure_runtime()` — runs the comprehension 4 times in parallel and times it |

## Why the runtime is ~10 seconds and not 40

Each `async_comprehension()` takes about 10 seconds because the generator
sleeps one second before each of its ten values. Running four of them with
`asyncio.gather` starts all four at once, and while one is sleeping the event
loop runs the others. The four therefore overlap almost perfectly, so the
total is roughly the duration of a single run — about 10 seconds instead of
4 × 10 = 40.
