# -*- coding: utf-8 -*-
# Copyright (c) 20016-2016 The Cloudsoar.
# See LICENSE for details.
"""
Implement Order data manage
"""

import threading

from common.guard import LockGuard
from common.util import NowMilli, Result
from frame.Logger import Log
from mongodb.dbbase import DBBase
from mongodb.dbconst import MAIN_DB_NAME, TAG_TABLE, ID


class TagDBImpl(DBBase):
    db = MAIN_DB_NAME
    collection = TAG_TABLE
    __lock = threading.Lock()
    
    @classmethod
    def instance(cls):
        '''
        Limits application to single instance
        '''
        with LockGuard(cls.__lock):
            if not hasattr(cls, "_instance"):
                cls._instance = cls()
        return cls._instance
    
    
    def __init__(self):
        DBBase.__init__(self, self.db, self.collection)
        
    def upsert_tags(self, repository, tags):
        rlt = self.read_record_list({'repository':repository},fields=['tag_name'])
        if not rlt.success:
            Log(1, 'upsert_tags.read_record_list fail,as[%s]'%(rlt.message))
            return rlt
        
        local_tags = []
        new_tags = []
        lost_tags = []
        for tag in rlt.content:
            local_tags.append(tag['tag_name'])
            if tag['tag_name'] not in tags:
                lost_tags.append(tag[ID])
        
        for tag in tags:
            if tag not in local_tags:
                new_tags.append({'repository':repository, 'delete':0, 'pull_num':0, 'create_time':NowMilli(),'tag_name':tag,'alias':''})

                
        if len(new_tags) > 0:
            rlt = self.batch_insert(new_tags)
            if rlt.success:
                Log(3, 'upsert_tags insert [%d] new record'%(rlt.content) )
            else:
                Log(1, 'upsert_tags insert record fail,as[%s]'%(rlt.message) )
        
        if len(lost_tags) > 0:
            rlt = self.updates({ID:{'$in':lost_tags}}, {'delete':NowMilli()})
            if rlt.success:
                Log(3, 'upsert_tags update [%d] old record'%(rlt.content) )
            else:
                Log(1, 'upsert_tags update record fail,as[%s]'%(rlt.message) )
                
        return Result(len(new_tags) + len(lost_tags))
        
        
            
            
            
            
            
            
            
            
            
            
            
        