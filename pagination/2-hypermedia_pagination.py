#!/usr/bin/env python3
"""
Implement a get_hyper method that takes the same arguments (and defaults)
as get_page and returns a dictionary containing the following key-value pairs:
"""

from typing import List
import math
import csv
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """
    comment
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """comment
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        comment
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        self.dataset()
        start_index, end_index = index_range(page, page_size)
        return self.__dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        comment
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        # ceiling division: division that rounds up to the nearest integer
        total_pages = (total_items + page_size - 1) // page_size

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }