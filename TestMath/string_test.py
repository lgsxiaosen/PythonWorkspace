#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 
    @create 2018-01-26 10:06
"""

a = """system-view,
            switchto context %(name)s,
            system-view,
            ip vpn-instance mgmt,
            route-distinguisher 10000:1,
            interface GigabitEthernet1/0/0,
            ip binding vpn-instance mgmt,
            ip address %(ip1)s 24,
            interface GigabitEthernet2/0/0,
            ip binding vpn-instance mgmt,
            ip address %(ip2)s 24,
            security-zone name dci,
            import interface Reth1,
            security-zone name inside,
            import interface Reth2,"""

b = """system-view,
            switchto context %(name)s,
            system-view,
            ip vpn-instance mgmt,
            route-distinguisher 10000:1,
            interface GigabitEthernet1/0/0,
            ip binding vpn-instance mgmt,
            ip address %(ip1)s 24,
            interface GigabitEthernet2/0/0,
            ip binding vpn-instance mgmt,
            ip address ip2s 24,
            security-zone name dci,
            import interface Reth1,
            security-zone name inside,
            import interface Reth2,"""

if "%(ip2)" in a:
    print "a_ip2"

if "%(ip2)" in b:
    print "b_ip2"

