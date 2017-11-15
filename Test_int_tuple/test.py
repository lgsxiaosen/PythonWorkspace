# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 2017-10-23
    
"""


a = ([1, 2, 3], 1)
print a


b = [[1, 2, 3], 1]
c = tuple(b)
print c


def trunc(value):
    rep = repr(value)
    lenrep = len(rep)
    if lenrep > 3:
        segment_length = 3 // 2
        rep = (
            rep[0:segment_length] +
            (" ... (%d characters truncated) ... "
             % (lenrep - 3)) +
            rep[-segment_length:]
        )
    return rep
di_ = {"id_": 1, "lis_": [1, 2, 3]}
for k, v in di_.items():
    if type(v) is dict:
        ee = "{%s}" % (", ".join("%r: %s" % (key, trunc(value))for key, value in v.items()))
    elif type(v) is tuple:
        ee = "(%s%s)" % (
            ", ".join(trunc(value) for value in v),
            "," if len(v) == 1 else ""
        )
    else:
        ee = "[%s]" % (
            ", ".join(trunc(value) for value in v)
        )

print ee


