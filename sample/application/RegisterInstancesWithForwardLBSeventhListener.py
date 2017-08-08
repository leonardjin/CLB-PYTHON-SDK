#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../..")
from src.QcloudApi.qcloudapi import QcloudApi

action = 'RegisterInstancesWithForwardLBSeventhListener'  # 绑定云服务器到应用型负载均衡七层监听器的转发规则上

"""
loadBalancerId  必传 负载均衡ID
listenerId      必传 监听器ID
locationIds     非必传 转发规则ID，默认全部
domain          非必传 转发规则域名，默认不做为过滤条件
url             非必传 转发规则路径，默认不做为过滤条件
backends.n.instanceId 必传 解绑的机器的instanceId
backends.n.port       必传 解绑的机器的端口
backends.n.weight     非必传 机器端口的权重，默认10

"""
region = 'gz'
params = {
    'loadBalancerId': "lb-0c4ypb1m",
    'listenerId': "lbl-68za8mki",
    'locationIds.0': "loc-1sgvoq0w",
    'backends.0.instanceId': "ins-db973yni",
    'backends.0.port': 10036,
    'backends.0.weight': 10036,
    # 'backends.1.instanceId':"ins-mt3sfc3q",
    # 'backends.1.port':8020,
}

try:
    service = QcloudApi(region=region)
    print service.generateUrl(action, params)
    print service.call(action, params)
except Exception, e:
    print 'exception:', e
