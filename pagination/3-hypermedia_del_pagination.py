#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination."""
import csv
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialise the server with empty dataset caches."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Return the cached dataset, loading it from the CSV if needed."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Return the dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return a page that stays correct even if rows were deleted."""
        indexed = self.indexed_dataset()
        assert index is None or isinstance(index, int)
        if index is None:
            index = 0
        assert 0 <= index < len(indexed)

        data = []
        current = index
        while len(data) < page_size and current < len(indexed):
            row = indexed.get(current)
            if row is not None:
                data.append(row)
            current += 1

        return {
            'index': index,
            'next_index': current,
            'page_size': len(data),
            'data': data,
        }
