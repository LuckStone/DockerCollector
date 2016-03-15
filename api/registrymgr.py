# -*- coding: utf-8 -*-
# Copyright (c) 20016-2016 The Cloudsoar.
# See LICENSE for details.


from frame.authen import ring8
from mongoimpl.registry.repositorydbimpl import RepositoryDBImpl


class RegistryMgr(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    @ring8
    def repositorys(self, namespace=''):
        return RepositoryDBImpl.instance().list_repository(namespace)
    
    @ring8
    def info(self):
        return RepositoryDBImpl.instance().exec_db_script('overview')
        