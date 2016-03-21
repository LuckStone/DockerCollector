# -*- coding: utf-8 -*-
# Copyright (c) 20016-2016 The Cloudsoar.
# See LICENSE for details.


import json

from common.util import Result
from frame.Logger import Log
from frame.authen import ring8
from frame.errcode import INVALID_JSON_DATA_ERR
from mongoimpl.registry.namespacedbimpl import NamespaceDBImpl
from mongoimpl.registry.repositorydbimpl import RepositoryDBImpl
from mongoimpl.registry.tagdbimpl import TagDBImpl


class RegistryMgr(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    @ring8
    def repositories(self, scope='', key=''):
        scope = scope.strip()
        key = key.strip()
        if key != '' and scope == 'usr':
            query = {'user_id':key}
        elif scope:
            query = {'namespace':scope}
        else:
            query = {}

        
        rlt = RepositoryDBImpl.instance().exec_db_script('repositories', query, 10, 0)
        return rlt
        
        
    
    @ring8
    def info(self):
        return RepositoryDBImpl.instance().exec_db_script('overview')
        
    @ring8    
    def namespaces(self):
        return NamespaceDBImpl.instance().read_record_list()
    
    @ring8    
    def namespace(self, namespace):
        return NamespaceDBImpl.instance().read_record(namespace)
    
    @ring8    
    def repository(self, namespace, repo_name=''):
        """
        # 返回仓库的tag列表
        """
        repo_name = repo_name.strip()
        namespace = namespace.strip()
        if repo_name.strip():
            namespace = '%s/%s'%(namespace, repo_name)
        return TagDBImpl.instance().get_tag_list(namespace)
    
    @ring8
    def tag(self, namespace, repo_name, tag_name=''):
        repo_name = repo_name.strip()
        namespace = namespace.strip()
        tag_name = tag_name.strip()
        if tag_name:
            namespace = '%s/%s'%(namespace, repo_name)
        else:
            tag_name = repo_name
        return TagDBImpl.instance().get_tag_info(namespace, tag_name)
    
    
    @ring8    
    def save_namespace(self, post_data):
        try:
            namespace = json.loads(post_data.replace("'", '"'))
        except Exception,e:
            Log(1,"save_account.parse data to json fail,input[%s]"%(post_data))
            return Result('',INVALID_JSON_DATA_ERR,str(e))
        else:
            return NamespaceDBImpl.instance().create_new_nspc(namespace)
    
    
    
    