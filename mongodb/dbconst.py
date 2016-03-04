# -*- coding: utf-8 -*-
# Copyright (c) 20016-2016 The Cloudsoar.
# See LICENSE for details.


MAIN_DB_NAME   = "cloudvisor"
ID             = "_id"


IDENTITY_TABLE         = "identity"


VM_INSTANCE_TABLE      = "VMInstance"        # 存放产品实例信息
VM_BACKUP_TABLE        = "VMBackup"          # 存放产品实例的备份信息， VM销毁之后需要将VM的信息保存到另外的表中
VM_TEMPLATE_TABLE      = "VMTemplate"        # 存放模板信息
STOCK_TABLE            = "Template_VM"       # 存放模板与VM的关联信息
STOCK_INFO             = "StockStatistics"   # 库存统计信息
PRODUCTION_PLAN_TABLE  = "ProductionPlan"    # 存放备货方案信息
TEMPLATE_PART_TABLE    = "TemplatePart"      # 模板配件信息
RESOURCE_TABLE         = "Resource"          # 存放系统资源信息
SALE_PLAN_TABLE        = "SalePlan"          # 存放销售方案信息
PLAN_PART_TABLE        = "CmoRelation"       # 存放(主产品与配件)关系信息
STANDARD_PART_TABLE    = "StandardPart"      # 存放配件规格信息
CITRIX_SERVER_TABLE    = "CitrixServer"      # 存放Citrix服务器信息
LOCATION_TABLE         = "Location"          # 存放地址信息
IDC_TABLE              = "IDC"               # 存放idc信息
ZONE_TABLE             = "Zone"              # 存放zone信息
CITY_TABLE             = "City"              # 存放城市信息

EXTENSION_TABLE = "extension"                # 保存扩展服务信息
USER_TABLE             = "user"              # 存放用户信息
TASK_TABLE             = "task"
COMMODITY_TABLE        = "commodity"
MODEL_TABLE = "model"                        # 存放型号信息
PRODUCTION_ORDER_TABLE = "ProductionOrder"   # 存放订单的信息
OPERATE_TABLE = "Operate"                    # 存放操作的记录
PRODUCTION_TASK_TABLE  = "ProductionTask"    # 存放生产操作任务的过程信息 
SUB_TASK_TABLE         = "SubTask"           # 存放子任务，子任务是任务计划的一部分， 不能单独恢复 
VM_TABLE               = "vm"                # 存放vm信息
PART_PACKAGE_TABLE     = "Parts"             # 存放配件（组合）信息
WORKBENCH_TABLE        = "Workbench"         # 存放订单处理的中间过程信息
SMART_CLONE_TABLE      = "SmartClone"        # 存放SmartClone的信息
BACKUP_TABLE           = "Backup"            # 存放backup和restore的信息

SYNCTASK               = "SyncTask"


TRAFFIC_SET_TABLE    = "traffic_set_meal"    # 存放流量套餐信息
NETWORK_TRAFFIC_TABLE= "network_traffic"     # 流量统计计费

UNKNOWN_NAME = "unknown name"
USER_TABLE             = "User"
BROADBAND_TABLE        = "Broadband"    # 存放宽带的信息
CLOUD_TABLE            = "Cloud"        # 存放私有云的信息
ROOT_OPTION_TABLE      = "rootoption"   # 
SUBNET_TABLE           = "Subnet"       # 
IP_INFO_TABLE          = "IPInfo"       # 
VLAN_TABLE             = "VLan"         # 
EXTENSION_TABLE        = "Extention"    # 存放CCP等外部服务信息
HOST_TABLE             = "Host"         # 存放主机
FIREWALL_TABLE         = "Firewall"     # 存放防火墙信息
DHCP_TABLE             = "DHCPSrv"      # 存放dhcp服务器信息
SWITCH_TABLE           = "Switch"       # 存放交换机信息
SWITCH_ACL_TABLE       = "SwitchACL"    # 存放交换机的Access ctrol list信息
ACL_RULE_TABLE         = "ACLRule"      # 存放交换机的ACL使用的Rule规则信息
WORKBENCH_TABLE        = "Workbench"    # 存放订单处理的中间过程信息
SCHEDULE_TABLE         = "Schedule"     # 调度任务信息
SCHEDULE_JOB_TABLE     = "jobs"         # Scheduler 库使用的私有的数据表
OPERATE_TABLE          = "OperateLog"   # 存放操作的日志，操作可以对应一组任务，也可以是一次即时的操作
TASK_TABLE             = "Task"         # 存放任务的运行时信息
SUB_TASK_TABLE         = "SubTask"      # 存放子任务，子任务是任务计划的一部分， 不能单独恢复 
CONFIG_TABLE           = "Configure"    # 存放支持修改的配置项
TRAFFIC_TABLE          = "Traffic"      # 流量范围定义
NETWORK_AGENT_TABLE    = "Agent"        # Network Agent 信息

#zone信息表
ZONE_TABLE             = "Zone"

#产品实例表
PRODUCT_TABLE          = "Product"      # 产品实例表

#策略记录表
NAT_TABLE              = "Nat"          #映射策略
ROUTE_TABLE            = "Route"        #路由策略 



# 数据库表的后缀
FLOW_TASK_SUFFIX = "Flow"  # 流量统计相关的任务数据库表的后缀
