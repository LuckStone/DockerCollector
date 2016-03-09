# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Copyright (c) 20016-2016 The Cloudsoar.
# See LICENSE for details.
'''
Created on 2016-3-8

@author: Jack
'''

import json

from frame.Logger import Log
from frame.curlclient import CURLClient
from mongoimpl.docker.notifydbimpl import NotifyDBImpl
from mongoimpl.docker.tagdbimpl import TagDBImpl


class RegistryClient(CURLClient):
    '''
    # 实现 Dockers registry的接口
    '''

    def __init__(self):
        '''
        Constructor
        '''
        username = 'registry_username'
        pwd = 'registry_password'
        #domain = GetSysConfig('registry_domain') or '192.168.2.55:5000'
        domain = '192.168.2.55:5000'
        CURLClient.__init__(self, username, pwd, domain)
        

    def load_registry_data(self):
        data = self.listing_repositories(100)
        NotifyDBImpl.instance().upsert_repository(data['repositories'])
        
        for repo in data['repositories']:
            tags = self.listing_image_tags(repo)
            if tags:
                TagDBImpl.instance().upsert_tags(repo, tags['tags'])
            else:
                Log(1, 'load_registry_data.listing_image_tags fail,as[no tags], repository[%s]'%(repo))
        
        
    def listing_repositories( self, num, last=0 ):
        url = "http://" + self.domain + '/v2/_catalog?n=%d&last=%d'%(num, last)
        response = self.do_get(url)
        if response.fail:
            response.log('listing_repositories')
        
        response.log('listing_repositories')
        return json.loads(response.body)
        
    def listing_image_tags(self, repository_name):
        url = "http://" + self.domain + '/v2/%s/tags/list'%(repository_name)
        response = self.do_get(url)
        if response.fail:
            response.log('listing_image_tags')
        response.log('listing_image_tags')
        return json.loads(response.body)
        
    def delete_image(self, repository_name, digest):
        url = "http://" + self.domain + '/v2/%s/manifests/%s'%(repository_name, digest)
        response = self.do_delete(url)
        if response.fail:
            response.log('delete_image')
        response.log('delete_image')
        
        

        
        
            
        
        
        
        