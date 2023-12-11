#!/usr/bin/env python3
""" create tasks """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """list of values"""
    returned_value = [task_wait_random(max_delay) for i in range(n)]
    new_list = []
    for i in asyncio.as_completed(returned_value):
        new_list.append(await i)
    return new_list
