# -*- coding: utf-8 -*-
# Copyright (c) 20016-2016 The Cloudsoar.
# See LICENSE for details.
import json

from frame.authen import ring8
from mongodb.dbconst import MAIN_DB_NAME
from mongoimpl.docker.notifydbimpl import NotifyDBImpl


_ALL = "All"

class NotifyMgr(object):
    db = MAIN_DB_NAME
    
    def __init__(self):
        pass

    @ring8
    def Save(self,post_data,*args):
        return NotifyDBImpl.instance().create(json.loads(post_data))
    
   
        
        
        
        
    
    
    