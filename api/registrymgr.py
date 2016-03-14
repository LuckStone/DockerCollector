# -*- coding: utf-8 -*-
# Copyright (c) 20016-2016 The Cloudsoar.
# See LICENSE for details.
'''
Created on 2016年3月14日

@author: Cloudsoar
'''
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
    def getrepositorys(self, namespace=''):
        return RepositoryDBImpl.instance().list_repository(namespace)