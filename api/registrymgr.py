# -*- coding: utf-8 -*-
# Copyright (c) 20016-2016 The Cloudsoar.
# See LICENSE for details.


from frame.authen import ring8
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
    def repositories(self, namespace=''):
        return RepositoryDBImpl.instance().list_repository(namespace.strip())
    
    @ring8
    def info(self):
        return RepositoryDBImpl.instance().exec_db_script('overview')
        
    @ring8    
    def namespaces(self):
        return NamespaceDBImpl.instance().read_record_list()
    
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
    
    
    