#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 20016-2016 The Cloudsoar.
# See LICENSE for details.

from frame.Logger import SysLog
from mongodb import dbconst
from mongodb.dbconst import COMMODITY_TABLE, PRODUCTION_ORDER_TABLE, \
    PRODUCTION_TASK_TABLE, MAIN_DB_NAME, VM_INSTANCE_TABLE, TASK_TABLE, OPERATE_TABLE, SUB_TASK_TABLE, \
    VM_TABLE, PART_PACKAGE_TABLE, WORKBENCH_TABLE, STOCK_TABLE, SYNCTASK
from mongodb.dbmgr import DBMgr
from mongodb.install import CommonDB
import getopt
import sys

"""
initialize database ,create table and insert some system info
"""

        

Tables = {
    COMMODITY_TABLE:"CMO",              # 存放商品详细信息   
    PRODUCTION_ORDER_TABLE:"ORD",       # 存放AP下达的生产订单
    PRODUCTION_TASK_TABLE:"TSK",        # 临时存放生产操作的任务信息 
}

def main():
    ret = DBMgr.instance().isDBRuning()
    if not ret:
        SysLog(1,"setup VFOS fail,database error")
        return 0
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ch", ["clean","help"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    if not len(opts):
        cleanSystem()
        sys.exit()
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-c","--clean"):
            cleanSystem()
            sys.exit()
        


def usage():
    print "-h  --help  show help"
    print "python reset.py -c  [clean run time data.]"
    print "python reset.py -h  [show help]"
    
def resetSystem():
    cloud_db = CommonDB(MAIN_DB_NAME,{})
    cloud_db.setup()
    
    
def cleanSystem():
    table_list = [RPCBOX_TABLE,
                  BOX_ENTITY_TABLE,
                  RPC_REQ_TABLE,
                  VM_INSTANCE_TABLE,
                  #VM_TEMPLATE_TABLE,
                  TASK_TABLE,
                  PRODUCTION_ORDER_TABLE,
                  OPERATE_TABLE,
                  PRODUCTION_TASK_TABLE,
                  SUB_TASK_TABLE,
                  VM_TABLE,
                  SYNCTASK,
                  #SALE_PLAN_TABLE,
                  #PRODUCTION_PLAN_TABLE,
                  STOCK_TABLE,
                  dbconst.SMART_CLONE_TABLE,
                  dbconst.SCHEDULE_TABLE,
                  "jobs",
                  PART_PACKAGE_TABLE,
                  WORKBENCH_TABLE]
    cloud_db = CommonDB(MAIN_DB_NAME,{})
    cloud_db.clean_data(table_list)
    
    # 清除subnet中的非初始数据
    DBMgr.instance().delete_record(MAIN_DB_NAME,SUBNET_TABLE,{"user_id": {"$ne":"system"}}) 


if __name__ == '__main__':
    main()
    
    

