import numpy as np
import difflib
import math
import pandas as pd
import Utilse as ut
import time
import discovery as dc

def DDsimilars(l1,l2):
    t = l1
    #print(l1,l2)
    if type(l1) and type(l2) in [np.int, np.int32, np.int64,np.float, np.float32, np.float64]:
        #print(2)
        m = abs(l1 - l2)
        return m
    else:
        #print(1)
        d = difflib.SequenceMatcher(None, l1,l2).quick_ratio()
        max_num = max(len(l1),len(l2)) * d
        min_num = min(len(l1),len(l2)) * d
        #print(max_num,min_num)
        m = math.ceil(max_num-min_num)
        return m

def maxclsuster(file,clomname,confidence):
    df = pd.DataFrame(pd.read_csv(file))
    l1 = []
    for i in range(len(df[clomname])):
        l1.append(i)
    dict1 = dict.fromkeys(l1)
    for i in range(len(df[clomname])):
        dict1[i] = df[clomname][i]
    sort1 = sorted(dict1.items(), key=lambda x: x[1])
    s = sort1
    #print(s)
    l2 = df[clomname].tolist()
    #print(type(l2[0]))
    if type(l2[0]) != str:
        tt = ut.calculate_delta(l2,confidence)
        print("The best delta of "+str(clomname)+" is "+str(abs(tt)))
        thresord = abs(tt)
        maxmalobjects = []
        #print(s)
        for i in range(len(s)):
            maxcluster = []
            for j in range(len(s)):
                if j > i:
                    pr = i
                    pl = j
                    judge = s[pl][1] - s[pr][1]
                    #print(type(s[pr][1]))
                    judge = DDsimilars(s[pl][1],s[pr][1])
                    #print(type(judge))
                    if judge < thresord:
                        # print(s[pl][1],s[pr][1])
                        # print(s[pl][0], s[pr][0])
                        if s[pr][0] not in maxcluster:
                            maxcluster.append(s[pr][0])
                        maxcluster.append(s[pl][0])
            #print(maxcluster)
            #print(len(maxcluster))
            # if maxmalobjects != []:
            if len(maxcluster) != 0:
                if s[maxcluster[len(maxcluster)-1]][1] - s[maxcluster[0]][1] != 0:
                    #print(s[maxcluster[len(maxcluster)-1]][0],s[maxcluster[0]][0])
                    #print(s[maxcluster[len(maxcluster)-1]][1],s[maxcluster[0]][1])
                    nmaxcluster = maxcluster
                    #print("aaa")
                    #print(nmaxcluster)
                    maxmalobjects.append(maxcluster)

            # ut.diff(maxmalobjects, maxcluster)

        # print(maxmalobjects)
        x = ut.diff(maxmalobjects)
        return x
    else:
        '''
        This section is a comparison of the character variable gap
        '''
        #print(l2)
        lattrs = ut.quchong(l2)
        templ = [] #store different similars

        x = 0
        return x

filename = '2.csv'
file = pd.read_csv(filename)
df = pd.DataFrame(file)
title = ut.getAttrbutes(filename)
for i in range(file.shape[0]):
    row = file.loc[i]
    attr = []
    for j in range(0, len(title)):
        attr.append(row[title[j]])


#con = 0.6
print("please input the confidence:")
con = float(input())
starttime = time.time()
#w = maxclsuster(filename,title[4],con)
#print(w)
C = []
for i in range(len(title)):
    w = maxclsuster(filename,title[i],con)
    C.append(w)
    #print(w)

C = ut.spilt(C)

for i in range(len(C)):
    C[i] = ut.quchong(C[i])

'''
建立LHS格
'''
templ = []
k = pow(2,len(C)) - 1
for i in range(k):
    templ.append(i)
lhsC = dict.fromkeys(templ)

def createl(C):
    temp = []
    for i in range(len(C)):
        for j in range(len(C)):
            if j > i:
                #print(C[i],C[j])
                u = ut.bingji(C[i],C[j])
                temp.append(u)
                '''
    if len(temp) != 1:
        createl(temp)
        '''
    return temp
tmp = []
for i in range(len(title)):
    tmp.append(dc.LCP(title[i],C[i]))
f = createl(C)
for i in range(len(C)):
    for j in range(len(C[i])):
        C[i][j] = sorted(C[i][j])

#print(f[0],C[2])
'''
uu = ut.detect(C[2],f[0])
if (len(uu)) > 2:
    print(title[0]+str(thresord[0])+' '+title[1]+str(thresord[1])+'---->'+title[2]+str(thresord[2]))
endtime = time.time()
print(endtime-starttime)
'''
#print(lcp)
def get_sub_set(nums):
    sub_sets = [[]]
    for x in nums:
        sub_sets.extend([item + [x] for item in sub_sets])
    return sub_sets
p1 = get_sub_set(title)
#print(p1)
p2 = get_sub_set(C)
#print(p2)
lcp = []
for i in range(len(p1)):
    lcp.append(dc.LCP(p1[i],p2[i]))
for i in range(len(lcp)):
    if len(lcp[i].name) >= 2:
        #print(lcp[i].name)
        t = ut.bingji(lcp[i].items[0],lcp[i].items[1])
        #print(t)
        lcp[i].items = t
        #print(lcp[i].items)

#print(lcp)
singlenode = []
lattice = []
'''
def depq(l:list):
    if len(l[0]) > 1:
        return True
'''

for i in range(len(lcp)):
    if len(lcp[i].name) == 1:
        singlenode.append(lcp[i])
    else:
        lattice.append(lcp[i])
#print(lattice)
origindd = []
for i in range(len(lattice)):
    for j in range(len(singlenode)):
        if singlenode[j].name[0] not in lattice[i].name and lattice[i].name and lattice[i].items != []:
            #print(singlenode[j].name,lattice[i].name)
            e = ut.chaji(lattice[i].items,singlenode[j].items)
            #print(e)
            if e[0] != []:
                origindd.append(dc.DD(singlenode[j].name,lattice[i].name))
'''                
a = [[1, 2], [2, 4]]
b = [[1, 2]]
c = ut.chaji(b,a)
'''
endtime = time.time()
for i in range(len(origindd)):
    print(origindd[i])
print(endtime-starttime)