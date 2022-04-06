import pandas as pd
import Utilse as ut
import itertools
import discovery as dc
import time

starttime = time.time()
filename = '2.csv'
#thresord = int(input())
thresord = [5,1,3,4]
#thresord = [0.3,0.3,0.3,0.3]
#thresord = [0.1,0.1,0.1,0.1]
file = pd.read_csv(filename)
df = pd.DataFrame(file)
title = ut.getAttrbutes(filename)
for i in range(file.shape[0]):
    row = file.loc[i]
    attr = []
    for j in range(0, len(title)):
        attr.append(row[title[j]])
'''
l1 = []
print(title)
for i in range(len(df['AGE'])):
    l1.append(i)
dict1 = dict.fromkeys(l1)
for i in range(len(df['AGE'])):
    dict1[i] = df['AGE'][i]
sort1 = sorted(dict1.items(), key = lambda x:x[1])
s = sort1
#print(s)
'''
'''
pl,pr are pointers first they are all point at the first item,then pr move to right every step
until the value above sigma the the pl move to next item
'''
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
            if  judge < thresord:
                #print(s[pl][1],s[pr][1])
                #print(s[pl][0], s[pr][0])
                if s[pr][0] not in maxcluster:
                    maxcluster.append(s[pr][0])
                maxcluster.append(s[pl][0])
    #if maxmalobjects != []:
    maxmalobjects.append(maxcluster)
    #ut.diff(maxmalobjects, maxcluster)

#print(maxmalobjects)
x = ut.diff(maxmalobjects)
#print(x)

create hash table C
'''

C = []
for i in range(len(title)):
    w = ut.maxclsuster(filename,title[i],thresord[i])
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
def depq(l:list):
    if len(l) > 0:
        return True
for i in range(len(lcp)):
    if len(lcp[i].name) == 1:
        singlenode.append(lcp[i])
    else:
        lattice.append(lcp[i])
origindd = []
for i in range(len(lattice)):
    for j in range(len(singlenode)):
        if singlenode[j].name[0] not in lattice[i].name and lattice[i].name != []:
            #print(singlenode[j].name,lattice[i].name)
            e = ut.chaji(lattice[i].items,singlenode[j].items)
            if depq(e) == True:
                origindd.append(dc.DD(singlenode[j].name,lattice[i].name))
'''                
a = [[1, 2], [2, 4]]
b = [[1, 2]]
c = ut.chaji(b,a)
print(c)
'''
print(origindd)
endtime = time.time()
print(endtime-starttime)