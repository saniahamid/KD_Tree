# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 19:31:26 2018

@author: nexts

This code implements KD tree on randomly generated data points

"""
from random import random
import collections
import itertools
import math

Node = collections.namedtuple("Node", 'point axis label left right')



        
def build_tree(objects, axis=0):

    if not objects:
        return None

    objects.sort(key=lambda o: o[0][axis])
    median_idx = len(objects) // 2
    median_point, median_label = objects[median_idx]

    next_axis = (axis + 1) % 2
    return Node(median_point, axis, median_label,
                build_tree(objects[:median_idx], next_axis),
                build_tree(objects[median_idx + 1:], next_axis))

                                           
        
        #print(key)
#        def build_tree(objects,axis=0):
#            if not objects:
#                return None
            
    
    
k = 2
npoints = 10
lookups = 1000
eps = 1e-8

points = [(tuple(random() for _ in range(k)), i) for i in range(npoints)]


tree = build_tree(points,0)
print(tree)