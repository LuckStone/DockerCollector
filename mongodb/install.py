#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 20016-2016 The Cloudsoar.
# See LICENSE for details.

from mongodb.dbconst import ID, COMMODITY_TABLE, PRODUCTION_ORDER_TABLE, \
    PRODUCTION_TASK_TABLE, MAIN_DB_NAME, STOCK_TABLE, SYNCTASK, CONFIG_TABLE, \
    VM_INSTANCE_TABLE, VM_TEMPLATE_TABLE, PRODUCTION_PLAN_TABLE, TEMPLATE_PART_TABLE, \
    RESOURCE_TABLE, SALE_PLAN_TABLE, CITRIX_SERVER_TABLE, LOCATION_TABLE, \
    EXTENSION_TABLE, USER_TABLE, TASK_TABLE, MODEL_TABLE, OPERATE_TABLE, \
    SUB_TASK_TABLE, VM_TABLE, PART_PACKAGE_TABLE, WORKBENCH_TABLE, RPCBOX_TABLE, \
    BOX_ENTITY_TABLE, RPC_REQ_TABLE, IDENTITY_TABLE
from mongodb.dbmgr import DBMgr
from frame.Logger import SysLog
import getopt
import imp
import os
import sys

"""
initialize database ,create table and insert some system info
"""

class CommonDB(object):
    def __init__(self,db_name,tables):
        self.db = db_name
        self.table_list = tables
        self.dbMgr = DBMgr.instance()
        
    def init_identity_table(self,id_key = None):
        if id_key is None:
            id_key = self.db
                    
        try:            
            arr = self.dbMgr.get_all_record(self.db,IDENTITY_TABLE)
            if len(arr) < 1:
                raise Exception("no record")
        except Exception,e:                   
            SysLog(1,"CommonDB.init_identity_table [%s], Create identity field,as [%s]"%(self.db,str(e)))
            self.add_identity_key(id_key)
        else:
            SysLog(1,"CommonDB.init_identity_table [%s] Create identity field success"%self.db)
            
    def clear_db(self):
        ret = True
        arr = self.dbMgr.get_all_table()
        if self.db in arr:
            try:
                self.dbMgr.drop_db(self.db)
            except Exception,e:
                SysLog(1,"CommonDB.init_db [%s] fail [%s]"%(self.db,str(e)))
                return False
                
        SysLog(1,"CommonDB.clear_db [%s], success"%self.db)
                
        return ret
    
    
    def clean_data(self,cn_list):
        for collection in cn_list:
            self.dbMgr.remove_all(self.db,collection)
    
    
    def add_identity_key(self,id_key,pre_txt = None):
        try:
            arr = self.dbMgr.get_records(self.db,IDENTITY_TABLE,{ID:id_key})
        except Exception,e:
            SysLog(1,"CommonDB.add_identity_key fail,[%s]"%str(e))
            return False
        else:
            if len(arr) > 0:
                return True
            
        record = {ID:id_key,"next":1000}
        if pre_txt is not None:
            record["pre"] = pre_txt
            
        try:
            self.dbMgr.insert_record(self.db,IDENTITY_TABLE,record)
        except Exception,e:
            SysLog(1,"CommonDB.add_identity_key fail,[%s]"%str(e))
            return False
        return True
    
    def del_identity_key(self,id_key):
        try:
            self.dbMgr.delete_record(self.db,IDENTITY_TABLE,{ID:id_key})
        except Exception,e:
            SysLog(1,"CommonDB.del_identity_key fail,[%s]"%str(e))
            return False
        return True

    def insert_record(self,cn,record): 
        return self.dbMgr.insert_records(self.db,cn,record)
    
    def insert_records(self,cn,records):
        for r in records:
            self.dbMgr.insert_record(self.db,cn,r)
        return len(records)
    
    def create_js(self,func_name,func_body):
        return self.dbMgr.create_js(self.db,func_name,func_body)
    
    def loadJs(self,file_path):    
        try:
            fd = open(file_path,"r")
            jsStr = fd.read()
            fd.close()
        except Exception,e:
            SysLog(1,"loadJs [%s] fail. as [%s]"%(file_path,str(e)))
            return False
        else:
            return jsStr
        
    def parse_js(self,js_str):
        index = js_str.find("function")
        if index == -1:
            return
        func_name = js_str[0:index]
        eIndex = func_name.find("=")
        if eIndex == -1:
            return 
        func_name = func_name[0:eIndex]
        
        func_body = js_str[index:]
        self.create_js(func_name.strip(), func_body)
        
    def auto_load_js(self):
        workdir = os.path.dirname(os.path.abspath(__file__))
        workdir = os.path.join(workdir,"javascript")
        workdir = os.path.join(workdir,self.db)
        dirs = os.listdir(workdir)
        for file_name in dirs:
            file_path = os.path.join(workdir,file_name)
            if os.path.isfile(file_path) and file_path.endswith(".js") :
                jsStr = self.loadJs(file_path)
                self.parse_js(jsStr)
            else:
                SysLog(3,"%s is not a js file"%file_path)
                
    def auto_import_data(self):
        workroot = os.path.dirname(os.path.abspath(__file__))
        datapath = os.path.join(workroot,"export")
        fullpath = os.path.join(datapath,"%s.py"%self.db)
        
        mod = self.load_from_file(fullpath)
        
        data = getattr(mod,"data",[])
        for t in data:
            ret = self.insert_records(t, data[t])
            SysLog(1,"CommonDB.auto_import_data success, insert [%d] record into %s"%(ret,t))
    
    def load_from_file(self,filepath):
        mod_name,file_ext = os.path.splitext(os.path.split(filepath)[-1])
        if file_ext.lower() == '.py':
            py_module = imp.load_source(mod_name, filepath)
        elif file_ext.lower() == '.pyc':
            py_module = imp.load_compiled(mod_name, filepath)
                
        return py_module

    def setup(self):
        self.clear_db()
        self.init_identity_table()
        for table_name,prefix in self.table_list.iteritems():
            self.add_identity_key(table_name,prefix)
        self.auto_import_data()
        #self.auto_load_js()
        

Tables = {
    COMMODITY_TABLE:"CMO",              # 存放商品详细信息   
    PRODUCTION_ORDER_TABLE:"ORD",       # 存放AP下达的生产订单
    PRODUCTION_TASK_TABLE:"TSK",        # 临时存放生产操作的任务信息 
    STOCK_TABLE:"STK",                  # 库存信息，存备货方案与vm实例关联信息
    SYNCTASK:None,
    CONFIG_TABLE:None,                  # 存放支持修改的配置项
    VM_INSTANCE_TABLE:None,             # 存放产品实例信息
    VM_TEMPLATE_TABLE:None,             # 存放模板信息
    PRODUCTION_PLAN_TABLE:None,         # 存放备货方案信息
    TEMPLATE_PART_TABLE:None,           # 模板配件信息
    RESOURCE_TABLE:None,                # 存放系统资源信息
    SALE_PLAN_TABLE:None,                   # 存放产品价格信息
    CITRIX_SERVER_TABLE:None,           # 存放Citrix服务器信息
    LOCATION_TABLE:None,                # 存放地址信息
    
    EXTENSION_TABLE:None,               # 保存扩展服务信息
    USER_TABLE:None,                    # 存放用户信息
    TASK_TABLE:None,             
    COMMODITY_TABLE:None,        
    MODEL_TABLE:None,                   # 存放型号信息
    PRODUCTION_ORDER_TABLE:None,        # 存放订单的信息
    OPERATE_TABLE:None,                 # 存放操作的记录
    PRODUCTION_TASK_TABLE:None,         # 存放生产操作任务的过程信息 
    SUB_TASK_TABLE:None,                # 存放子任务，子任务是任务计划的一部分， 不能单独恢复 
    VM_TABLE:None,                      # 存放vm信息
    PART_PACKAGE_TABLE:None,            # 存放配件（组合）信息
    WORKBENCH_TABLE:None,               # 存放订单处理的中间过程信息

    RPCBOX_TABLE:None,       
    BOX_ENTITY_TABLE:None,  
    RPC_REQ_TABLE:None,       
}

def main():
    ret = DBMgr.instance().isDBRuning()
    if not ret:
        SysLog(1,"setup VFOS fail,database error")
        return 0
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ilsh", ["install","loadData","loadScript","help"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    if not len(opts):
        usage()
        sys.exit()
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-i","--install"):
            install()
            sys.exit()
        elif opt in ("-l","--loadData"):
            loadData()
            sys.exit()
        elif opt in ("-s","--loadScript"):
            loadScript()
            sys.exit()
        


def usage():
    print "-h  --help  show help"
    print "python install.py -i  [new install,it will clear user data.]"
    print "python install.py -l  [reset the prepare data,won't delete user data.]"
    print "python install.py -h  [show help]"
    
def install():
    cloud_db = CommonDB(MAIN_DB_NAME,Tables)
    cloud_db.setup()
    
    
def loadData():
    cloud_db = CommonDB(MAIN_DB_NAME,{})
    cloud_db.auto_import_data()

def loadScript():
    cloud_db = CommonDB(MAIN_DB_NAME,{})
    cloud_db.auto_load_js()

if __name__ == '__main__':
    main()

