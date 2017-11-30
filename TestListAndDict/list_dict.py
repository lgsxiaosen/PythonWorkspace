# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 2017-10-27
    
"""
import time

from datetime import datetime

a = {
            'Logic_Pool' : u'逻辑资源池',
            'Logic_Server' : u'逻辑服务器',
            'Volume':  u'磁盘卷',
            'IP_Segment':u'IP段',
            'IP':u'IP地址',
            'VPC':u'VPC',
            'Subnet':  u'子网',
            'FW_Policy': u'防火墙策略',
            'LB_Policy': u'负载均衡策略',
            'Backup_policy': u'备份策略',
            'Bigeye_policy': u'监控策略',
            'Zabbix': u"性能监控",
            'VPN': u'VPN',
            'VPN_Policy': u'VPN策略',
            'PM_Cluster': u'物理集群',
            'PUBLIC_IP': u'公网IP',
            'PM': u'物理机',
            'SECURITY_SERVICES': u'安全服务项',
            'VM': u'虚机',
            'PM_Resource': u'物理机资源',
            "PAAS_VM":u"paas虚机",
            'Backup': u'备份',
            # paas平台资源类型
            "ApacheCluster": u'Apache集群',
            "J2EEContainer": u'J2EE容器',
            "TodeSNCluster": u'Tode单节点集群',
            "TodeMPCluster": u'TodeMP集群',
            "SpecialMQ": u'专用MQ',
            "JCFPsCluster": u'JCF小规模集群',
            "JCFAsCluster": u'JCF大规模集群',
            "RedisCluster": u'Redis资源',
            "ZKCluster": u'ZK',
            "SIHCluster": u'SIH',
            "S2HOST": u'S2服务器',
            "S3HOST": u'S3服务器',
            "DBaaS": u'DBaaS实例',
            "TodeLargeScaleMPCluster": u'Tode大规模MP集群',
            'DBschema': u'数据库用户',
'Logic_Poo2l' : u'逻辑资源池',
            'Lo2gic_Server' : u'逻辑服务器',
            'Vo2lume':  u'磁盘卷',
            'IP2_Segment':u'IP段',
            'IP2':u'IP地址',
            'VPC2':u'VPC',
            'Sub2net':  u'子网',
            'FW_2Policy': u'防火墙策略',
            'LB2_Policy': u'负载均衡策略',
            'Ba2ckup_policy': u'备份策略',
            'Bi2geye_policy': u'监控策略',
            'Za2bbix': u"性能监控",
            'VP2N': u'VPN',
            'VPN_2Policy': u'VPN策略',
            'PM_C2luster': u'物理集群',
            'PUB2LIC_IP': u'公网IP',
            'PM2': u'物理机',
            'SEC2URITY_SERVICES': u'安全服务项',
            'VM2': u'虚机',
            'PM_2Resource': u'物理机资源',
            "PA2AS_VM":u"paas虚机",
            'B2ackup': u'备份',
            # paas平台资源类型
            "ApacheCl2uster": u'Apache集群',
            "J2EECont2ainer": u'J2EE容器',
            "TodeSNCl2uster": u'Tode单节点集群',
            "TodeMPCl2uster": u'TodeMP集群',
            "SpecialM2Q": u'专用MQ',
            "JCFPsClus2ter": u'JCF小规模集群',
            "JCFAsClu2ster": u'JCF大规模集群',
            "RedisCl2uster": u'Redis资源',
            "ZKClus2ter": u'ZK',
            "SIHCl2uster": u'SIH',
            "S2HO2ST": u'S2服务器',
            "S3H2OST": u'S3服务器',
            "DB2aaS": u'DBaaS实例',
            "T2odeLargeScaleMPCluster": u'Tode大规模MP集群',
            '2DBschema': u'数据库用户',
'Logic_Poo1l' : u'逻辑资源池',
            'Logi1c_Server' : u'逻辑服务器',
            'Vol1u1me':  u'磁盘卷',
            'IP1_Segment':u'IP段',
            'IP1':u'IP地址',
            'VP1C':u'VPC',
            'Sub1net':  u'子网',
            'FW_Po1licy': u'防火墙策略',
            'LB_Po1licy': u'负载均衡策略',
            'Back1up_policy': u'备份策略',
            'Big1eye_policy': u'监控策略',
            'Za1bbix': u"性能监控",
            'VP1N': u'VPN',
            'V11PN_Policy': u'VPN策略',
            '1PM_Cluster': u'物理集群',
            'P1UBLIC_IP': u'公网IP',
            'P1M': u'物理机',
            'SEC1URITY_SERVICES': u'安全服务项',
            'VM1': u'虚机',
            'PM1_Resource': u'物理机资源',
            "P1AAS_VM":u"paas虚机",
            '1Backup': u'备份',
            # paas平台资源类型
            "ApacheCluste1r": u'Apache集群',
            "J2EEContain1er": u'J2EE容器',
            "TodeSNCluster1": u'Tode单节点集群',
            "TodeMPClus1ter": u'TodeMP集群',
            "SpecialMQ1": u'专用MQ',
            "JCFPsClu1ster": u'JCF小规模集群',
            "JCFAsCl1uster": u'JCF大规模集群',
            "RedisC1luster": u'Redis资源',
            "ZKClu1ster": u'ZK',
            "SIHC1luster": u'SIH',
            "S2H1OST": u'S2服务器',
            "S31HOST": u'S3服务器',
            "D1BaaS": u'DBaaS实例',
            "1TodeLargeScaleMPCluster": u'Tode大规模MP集群',
            '1DBschema': u'数据库用户',
                }

start1 = datetime.now()
print start1
b = [{'resource_type_en': k, 'resource_type_ch': v} for k, v in a.items()]
end1 = datetime.now()
print end1
print b
print end1-start1
resource_types = []
start2 = time.time()
for k, v in a.items():
    data = {"resource_type_en": k, "resource_type_ch": v}
    resource_types.append(data)
end2 = time.time()
print resource_types
print end2-start2

