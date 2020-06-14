#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------
# File      : minheap
# DateTime  : 2020/6/10 0010 20:58
# Author    : Chen Ji
# Email     : fzls.zju@gmail.com
# -------------------------------
import time
# 用于实现排行的最小堆
from heapq import heapify, heappush, heappushpop
from multiprocessing import Queue


class MinHeap:
    def __init__(self, top_n):
        self.h = []
        self.length = top_n
        heapify(self.h)

    def add(self, element):
        if len(self.h) < self.length:
            heappush(self.h, element)
        else:
            heappushpop(self.h, element)

    def getTop(self):
        return sorted(self.h, reverse=True)


class MinHeapWithQueue:
    def __init__(self, name: str, minheap: MinHeap, minheap_queue: Queue):
        self.name = name
        self.minheap = minheap
        self.minheap_queue = minheap_queue

        self.start_time = time.time()
        self.processed_result_count = 0

    def process_results_per_second(self) -> float:
        return float(self.processed_result_count) / (time.time() - self.start_time + 0.0001)

    def remaining_time(self) -> float:
        rt = 0.0
        if self.processed_result_count == 0:
            # 啥都没处理的时候，预估剩余一天时间
            rt = 86400.0
        else:
            # 否则预估剩余时间=当前已处理速度*当前结果队列大小
            rt = (time.time() - self.start_time) / float(self.processed_result_count) * self.minheap_queue.qsize()

        return rt
