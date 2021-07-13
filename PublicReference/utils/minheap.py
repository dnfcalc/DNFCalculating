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

# 工作进程与主进程的数据传输配置
# 批量向主进程传输计算结果（已本地预处理过）的大小
batch_size = 100
# 倍增阶段的临界批量大小
batch_stage_double_upper_bound = 6400
# 累加阶段每次增加的批量大小
batch_linear_increase_size = 100
# 预期数据传输队列的最大大小
expected_qsize = 100


class MinHeap:
    def __init__(self, top_n, batch_size):
        self.h = []
        self.length = top_n
        heapify(self.h)

        self.processed_result_count = 0
        self.batch_size = batch_size

    def add(self, element):
        if len(self.h) < self.length:
            heappush(self.h, element)
        else:
            heappushpop(self.h, element)

    def getTop(self):
        return sorted(self.h, reverse=True)

    def merge(self, other):
        """
        合并另一个堆
        @type other MinHeap
        """
        for elem in other.h:
            self.add(elem)
        self.processed_result_count += other.processed_result_count
        self.batch_size = other.batch_size

    def reset(self):
        self.h = []
        heapify(self.h)

        self.processed_result_count = 0

    def update_batch_size(self):
        if self.batch_size < batch_stage_double_upper_bound:
            self.batch_size *= 2
        else:
            self.batch_size += batch_linear_increase_size


class MinHeapWithQueue:
    def __init__(self, name: str, minheap: MinHeap, minheap_queue: Queue):
        self.name = name
        self.minheap = minheap
        self.minheap_queue = minheap_queue

        self.start_time = time.time()

    def process_results_per_second(self) -> float:
        return float(self.minheap.processed_result_count) / (
            time.time() - self.start_time + 1e-6)
