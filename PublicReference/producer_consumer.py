#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------
# File      : producer_consumer
# DateTime  : 2020/6/7 0007 12:04
# Author    : Chen Ji
# Email     : fzls.zju@gmail.com
# -------------------------------
import multiprocessing

from PublicReference import logger


工作线程数 = multiprocessing.cpu_count()
每个工作线程应处理的任务数 = 4
串行搜索的层数 = 2 # 散件模式下，前两层串行搜索
批量传回的结果数 = 100 # 出于性能考虑，将结果按该数目批量通过队列传回主线程

class ProducerData:
    def __init__(self):
        self.work_queue = None  # type: multiprocessing.JoinableQueue
        self.calc_index = 0
        self.produced_count = 0


producer_data = ProducerData()


def producer(*args):
    producer_data.work_queue.put((producer_data.calc_index, args))

    producer_data.produced_count += 1
    logger.info("producer put %3dth work into work queue", producer_data.produced_count)


def consumer(work_queue, work_func):
    """
    @type work_queue: multiprocessing.JoinableQueue
    """
    current_process = multiprocessing.current_process()

    logger.info("work thread={} started, ready to work".format(current_process))
    current_calc_index = 0
    processed_count = 0
    continue_wrok = True
    while continue_wrok:
        try:
            calc_index, args = work_queue.get()
            if calc_index != current_calc_index:
                current_calc_index = calc_index
                processed_count = 0
            processed_count += 1
            logger.info("work thread {} processing {}th work".format(current_process, processed_count))

            work_func(*args)
        except BrokenPipeError as error:
            # 这个一般是程序退出的时候发生的，这种情况直接退出
            logger.warning("work thread={} BrokenPipeError quit job".format(current_process))
            continue_wrok = False
        except Exception as error:
            args_list = []
            if 'args' in locals():
                args_list = [arg.__dict__ for arg in args]
            logger.error("work thread {} error={} processed count={}, args_list={}".format(current_process, error, processed_count, args_list))
        finally:
            work_queue.task_done()

    logger.info("work thread ={} stopped, processed_count={}".format(current_process, processed_count))
