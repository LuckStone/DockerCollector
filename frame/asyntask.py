# -*- coding: utf-8 -*-
# Copyright (c) 20016-2016 The Cloudsoar.
# See LICENSE for details.
from frame.task import Task




"""
实现轮询的逻辑，
支持异步的任务需求
"""

class AsynTask(Task):
    CALLING = 1
    WAIT_RESULT = 2
    
    def __init__(self,task_info):
        #Log(4,"AsynTask __init__,task_id is [%s],obj[%s]"%(task_id,id(self)))
        #self.task_id = task_id
        super(AsynTask, self).__init__(task_info)
        self.__act = AsynTask.CALLING

        
    def launch_task(self):
        if self.is_timeout():
            return Result(self.task_id, TASK_TIMEOUT_ERR, "Time out")
        
        if self.is_waiting():
            return self.update_task_state()
        else:
            return self.start_task()
            
    def process_launch_result(self,launch_result):
        if self.is_waiting():
            self.parse_update_result(launch_result)
        else:
            self.parse_start_result(launch_result)
        if self.is_finished():
            return launch_result
        self.delay()
        self.process()
        
    def parse_update_result(self,task_result):
        '''
        # 这个函数要检查更新的返回结果，判断任务是否成功        
        '''
        if task_result.success:
            self.set_success()
        else:
            self.set_fail(task_result.message, task_result.result)
            
    def parse_start_result(self,task_result):
        '''
        # 这个函数要检查启动的返回结果，判断任务是否成功        
        '''
        if task_result.success:
            self.set_waiting()
        else:
            self.set_fail(task_result.message, task_result.result)
            
    def start_task(self):
        """
        # 创建任务
        """
  
    def update_task_state(self):
        """
        # 更新任务状态
        """
        
    def is_waiting(self):
        return self.__act == AsynTask.WAIT_RESULT
    
    def set_waiting(self):
        self.__act = AsynTask.WAIT_RESULT
        
    
    def snapshot(self):
        snap = super(AsynTask, self).snapshot()
        snap["__act"] = self.__act
        return snap            
        
        
        
        
        
        
        
        
    