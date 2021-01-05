#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------
# File      : producer_consumer
# DateTime  : 2020/6/7 0007 12:04
# Author    : Chen Ji
# Email     : fzls.zju@gmail.com
# -------------------------------
import multiprocessing
import traceback

from PublicReference import logger


thread_num = multiprocessing.cpu_count()
thread_task = 4

class ProducerData:
    def __init__(self):
        self.work_queue = None  # type: multiprocessing.JoinableQueue
        self.calc_index = 0
        self.produced_count = 0


producer_data = ProducerData()


def producer(*args):
    producer_data.work_queue.put((producer_data.calc_index, args))

    producer_data.produced_count += 1
    # logger.info("producer put %3dth work into work queue", producer_data.produced_count)


def consumer(work_queue, work_func):
    """
    @type work_queue: multiprocessing.JoinableQueue
    """
    current_process = multiprocessing.current_process()

    # logger.info("work thread={} started, ready to work".format(current_process))
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
            # logger.info("work thread {} processing {}th work".format(current_process, processed_count))

            work_func(*args)
        except BrokenPipeError as error:
            # 这个一般是程序退出的时候发生的，这种情况直接退出
            logger.warning("work thread={} BrokenPipeError quit job".format(current_process))
            continue_wrok = False
        except Exception as error:
            logger.error("work thread {} error={} processed count={}\n detail {}".format(current_process, error, processed_count,traceback.print_exc()))
            # logger.error("work thread {} error={} processed count={}\n".format(current_process, error, processed_count))
        finally:
            work_queue.task_done()

    # logger.info("work thread ={} stopped, processed_count={}".format(current_process, processed_count))
