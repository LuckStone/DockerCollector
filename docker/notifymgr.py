# -*- coding: utf-8 -*-
# Copyright (c) 20016-2016 The Cloudsoar.
# See LICENSE for details.
import json

from common.util import Result
from frame.Logger import Log
from frame.authen import ring8
from mongodb.dbconst import MAIN_DB_NAME
from mongoimpl.docker.notifydbimpl import NotifyDBImpl
from __builtin__ import str
from frame.errcode import FAIL
from pyasn1.compat.octets import null


_ALL = "All"

class NotifyMgr(object):
    db = MAIN_DB_NAME
    
    def __init__(self):
        pass

    @ring8
    def Save(self, post_data, *args):
        data = json.loads(post_data)
        if isinstance(data, dict) and 'events' in data:
            for event in data['events']:
                self.save_event(event)
        else:
            Log(1, 'invalid data[%s]'%(post_data))
            return Result('', FAIL, 'invalid data')
    
    def save_event(self, event):
        rlt = NotifyDBImpl.instance().create(event)
        if not rlt.success:
            Log(1, 'save_event[%s]fail,as[%s]'%(str(event), rlt.content))
        
        action = event.get('action','')
        if action == 'pull':
            return self.parse_pull_action(event.get('target',null))
        elif action == 'push':
            return self.parse_push_action(event.get('target',null))
        else:
            Log(1, 'unknow action[%s]'%(action))
            return Result('', FAIL, 'unknow action')
   
        
    def parse_pull_action(self, event):
        pass 
        
        
    def parse_push_action(self, event):
        pass
    
    