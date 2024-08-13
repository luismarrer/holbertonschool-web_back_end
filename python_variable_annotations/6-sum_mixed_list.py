#!/usr/bin/env python3

from typing import List, Union

def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    add = 0.0
    for num in mxd_list:
        add += num
    return add
