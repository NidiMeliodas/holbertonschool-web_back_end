#!/usr/bin/env python3
"""
Implement a get_hyper_index method with two integer arguments: index with a
None default value and page_size with default value of 10.

The method should return a dictionary with the following key-value pairs:
index: the current start index of the return page. That is the index of
the first item in the current page. For example if requesting page 3 with
page_size 20, and no data was removed from the dataset, the current index
should be 60.
next_index: the next index to query with. That should be the index of the
first item after the last item on the current page.
page_size: the current page size
data: the actual page of the dataset
"""

import csv
import math
from typing import List, Dict


class Server:
    """
    comment
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        comment
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        comment
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset
            self.__indexed_dataset = {
                i: truncated_dataset[i] for i in range(len(truncated_dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        comment
        """
        total_items = len(self.dataset())
        assert index in range(0, total_items)
        data = []
        indexed_data = self.indexed_dataset()
        for key, value in indexed_data.items():
            if len(data) <= page_size:
                data.append(value)
            else:
                break
        next_index = index + len(data)

        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }