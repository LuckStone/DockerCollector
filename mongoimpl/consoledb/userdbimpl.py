# -*- coding: utf-8 -*-
# Copyright (c) 20016-2016 The Cloudsoar.
# See LICENSE for details.

from common.guard import LockGuard
from mongodb.dbbase import DBBase
from mongodb.dbconst import MAIN_DB_NAME, ID, USER_TABLE
import threading

"""
实现用户信息相关的数据库操作
"""

a = ["access_uuid","security_key","level","description","createTime","name","state","login_name","login_pass"]

USER_RECORD_PREFIX = "USR"   # 订单记录ID的前缀

class UserDBImpl(DBBase):
    db = MAIN_DB_NAME
    collection = USER_TABLE
    __lock = threading.Lock()
    
    @classmethod
    def instance(cls):
        with LockGuard(cls.__lock):
            if not hasattr(cls, "_instance"):
                cls._instance = cls()

        return cls._instance
    
    def __init__(self):
        DBBase.__init__(self, self.db, self.collection)
        
    def create_user_record(self,user_info):
        if ID not in user_info:
            user_info[ID] = self.get_record_id(USER_RECORD_PREFIX)
        
        return self.insert(user_info)
    
        
    def update_user(self,_id,vm_info):
        return self.update({ID:_id},vm_info)
    
    def read_user_info(self,access_uuid):
        rlt = self.read_record_list({"access_uuid":access_uuid})
        if rlt.success and len(rlt.content):
            return rlt.content[0]
        else:
            return None
    
    def delete_user(self,access_uuid):
        return self.remove({"access_uuid":access_uuid})
        
     

        
        
        
        
    