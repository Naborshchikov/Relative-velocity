#!/usr/bin/env python
# coding: utf-8

# In[12]:


"""Relative velocity""" 
from prettytable import PrettyTable
Initial_conditions = [[1, 'Project implemented in Python', 'ver. 3.7.6 \n'],
                      [2, 'ID - Anaconda', 'ver. 2020 02 \n'],
                      [3, '(1-v**2/c**2)**(1/2)', "From Einstein's Theory of Relativity\n"],
                      [4, 'c', 'speed of light \n'],
                      [5, 'v', 'speed \n'],
                      [6, 'v = dr/dt if θ and φ equal to zero', 'spherical coordinate system \n'],
                      [7, 'v1 = dr1/dt1', 'for the onlooker \n'],
                      [8, 'v2 = dr2/dt1', 'for the object of the onlooker \n'],
                      [9, 'r1', 'for the onlooker \n'],
                      [10, 'r2', 'for the object of the onlooker \n'],
                      [11, 'k = r2/r1', 'the ratio of the radii of the \n'
                       'observer and the object of observation \n'],
                      [12, 'dr2/dr1 = dkr1/dr1 = k', 'at the conclusion of the equation \n'],
                      [13, '(1-(1/k)**2 * v**2/c**2)**(1/2)', "author's conclusion \n"]]
table1 = PrettyTable(['#', 'Description', 'Link to source/ comments'])

for rec in Initial_conditions:
    table1.add_row(rec)
print(table1)
# speed of light in vacuum
c = 299792458
print('r1 - this is the radius of the first object relative to which the second object is viewed')
r1 = int(input("input r1 in meters:"))
print('r2 - this is the distance from the center of the first object to the center of the second object')
r2 = int(input("input r2 in meters:"))
v = c*(r2/r1)
print('The maximum speed must be less than', v, 'm/s')

