# Pagination

Paginating a dataset of popular baby names three ways: simple index-based
pages, hypermedia pages carrying their own navigation metadata, and
deletion-resilient pages that stay correct even when rows disappear between
two requests.

## Requirements

- Ubuntu 20.04 LTS, `python3` (3.9), `pycodestyle` 2.5.*
- All files start with `#!/usr/bin/env python3` and end with a new line
- All modules, classes and functions are documented and type-annotated
- The dataset file `Popular_Baby_Names.csv` must sit next to these scripts

## Files

| File | Description |
| --- | --- |
| `0-simple_helper_function.py` | `index_range(page, page_size)` — start/end indexes for a page |
| `1-simple_pagination.py` | `Server.get_page()` — returns the rows of a page |
| `2-hypermedia_pagination.py` | `Server.get_hyper()` — page plus `next_page`, `prev_page`, `total_pages` |
| `3-hypermedia_del_pagination.py` | `Server.get_hyper_index()` — resilient to deleted rows |

## Why deletion-resilient pagination matters

Classic pagination uses an offset. If rows are deleted between two requests,
everything shifts up and the user silently skips items. Indexing the dataset
by a stable position and walking forward from the requested index means a
deleted row is simply skipped, and no remaining row is ever missed.
