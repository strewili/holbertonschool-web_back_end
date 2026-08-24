# Python - Variable Annotations

Type annotations in Python 3: adding type hints to function parameters,
return values and module-level variables, working with complex types from the
`typing` module, and duck typing an iterable object.

Annotations do not change how the code runs — Python stays dynamically typed.
They document intent and let tools like `mypy` catch type errors before the
code is ever executed.

## Learning objectives

- Type annotations in Python 3
- How to use type annotations to specify function signatures and variable types
- Duck typing
- How to validate code with `mypy`

## Requirements

- Ubuntu 20.04 LTS, `python3` (version 3.9)
- All files start with `#!/usr/bin/env python3` and end with a new line
- All files are executable
- Code follows `pycodestyle` (version 2.5.*)
- Every module and every function carries a real documentation sentence

## Files

| File | Description |
| --- | --- |
| `0-add.py` | `add(a: float, b: float) -> float` — sum of two floats |
| `1-concat.py` | `concat(str1: str, str2: str) -> str` — concatenates two strings |
| `2-floor.py` | `floor(n: float) -> int` — floor of a float |
| `3-to_str.py` | `to_str(n: float) -> str` — string representation of a float |
| `4-define_variables.py` | Annotated module-level variables |
| `5-sum_list.py` | `sum_list(input_list: List[float]) -> float` |
| `6-sum_mixed_list.py` | `sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float` |
| `7-to_kv.py` | `to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]` |
| `8-make_multiplier.py` | `make_multiplier(multiplier: float) -> Callable[[float], float]` |
| `9-element_length.py` | Duck-typed iterable annotated with `Iterable`/`Sequence` |

## Usage

```
./0-main.py
```

Or inspect the annotations directly:

```
python3 -c "print(__import__('0-add').add.__annotations__)"
```
