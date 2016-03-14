# -*- coding: utf-8 -*-
# Copyright (c) 20016-2016 The Cloudsoar.
# See LICENSE for details.
"""
Implement Order data manage
"""

import threading

from common.guard import LockGuard
from frame.Logger import Log
from mongodb.dbbase import DBBase
from mongodb.dbconst import MAIN_DB_NAME, IMAGE_TABLE, ID


class ImageDBImpl(DBBase):
    db = MAIN_DB_NAME
    collection = IMAGE_TABLE
    __lock = threading.Lock()
    
    @classmethod
    def instance(cls):
        with LockGuard(cls.__lock):
            if not hasattr(cls, "_instance"):
                cls._instance = cls()
        return cls._instance
    
    
    def __init__(self):
        DBBase.__init__(self, self.db, self.collection)
        
    def upsert_image_info(self, image_id, repository):       
        rlt = self.update({ID:image_id}, {'repository':repository}, True)
        if not rlt.success:
            Log(1, 'upsert_image_info[%s]fail,as[%s]'%(repository, rlt.message))
        
            
            
            
            
            
            
            
            
            
            
            
        