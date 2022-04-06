import pandas as pd
import Utilse as ut
from itertools import product
import discovery as dc
import time
import itertools

filename = '2.csv'
#thresord = int(input())
thresord = [5,1,3,4]
#thresord = [0.3,0.3,0.3,0.3]
file = pd.read_csv(filename)
df = pd.DataFrame(file)
title = ut.getAttrbutes(filename)
for i in range(file.shape[0]):
    row = file.loc[i]
    attr = []
    for j in range(0, len(title)):
        attr.append(row[title[j]])
'''
LCP contains every items
'''
lcp = []
for i in range(len(title)):
    pairs = dc.LCP(title[i],df[title[i]].tolist())
    lcp.append(pairs)
def maxclsuster(file,clomname,thresord):
    df = pd.DataFrame(pd.read_csv(file))
    l1 = []
    for i in range(len(df[clomname])):
        l1.append(i)
    dict1 = dict.fromkeys(l1)
    for i in range(len(df[clomname])):
        dict1[i] = df[clomname][i]
    sort1 = sorted(dict1.items(), key=lambda x: x[1])
    s = sort1
    # print(s)
    '''
    pl,pr are pointers first they are all point at the first item,then pr move to right every step
    until the value above sigma the the pl move to next item
    '''
    maxmalobjects = []
    i = 0
    for i in range(len(s)):
        maxcluster = []
        for j in range(len(s)):
            if j > i:
                pr = i
                pl = j
                judge = s[pl][1] - s[pr][1]
                if judge < thresord:
                    # print(s[pl][1],s[pr][1])
                    # print(s[pl][0], s[pr][0])
                    if s[pr][0] not in maxcluster:
                        maxcluster.append(s[pr][0])
                    maxcluster.append(s[pl][0])
        # if maxmalobjects != []:
        maxmalobjects.append(maxcluster)
        # ut.diff(maxmalobjects, maxcluster)

    # print(maxmalobjects)
    x = ut.diff(maxmalobjects)
    return x
C = []
for i in range(len(title)):
    w = maxclsuster(filename,title[i],thresord[i])
    C.append(w)
nlcp = []
for i in range(len(title)):
    lcp = dc.LCP(title[i],C[i])
    nlcp.append(lcp)
print(nlcp)
'''
for level 1 this algorithm compute the items with other's difference
'''

omgias = []
for i in range(len(nlcp)):
    for j in range(len(nlcp)):
        if j != i:
            t = 0

