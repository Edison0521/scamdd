import pandas as pd
import difflib
import itertools
import math
import numpy as np

def calculate_delta(arr, confidence):
    n = len(arr)
    removals = n - round(n * confidence)
    best_delta = arr[-1] - arr[0]

    # removing outliers in such a way that minimize delta:
    for i in range(removals + 1):
         best_delta = min(best_delta, arr[-(removals - i + 1)] - arr[i])

    return best_delta

def is_nan(nan):
    return nan != nan

def attributes(filename,n):
    datas = pd.read_csv(filename,usecols=[n])
    return datas[n].tolist()

def splitstr(s: str):
    temp1 = []
    for litter in s:
        temp1.append(litter)
    return temp1

def DDsimilars(l1,l2):
    t = l1
    #print(l1,l2)
    if type(l1) and type(l2) in [np.int, np.int32, np.int64]:
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
def similars(sigma : float,l1,l2):
    t = l1
    #print(l1,l2)
    if type(l1) and type(l2) == float :
        m = abs(l1 - l2)
        if m <= sigma:
            return True
    if type(t) and type(l2) == str:
        temp0 = splitstr(l1)
        temp1 = splitstr(l2)
        if len(temp0) > len(temp1):
            tempA = temp0
            tempB = temp1
        else:
            tempA = temp1
            tempB = temp0

        for i in range(len(tempB)):
            if tempB[i] in tempA:
                tempA.remove(tempB[i])

        if len(tempA) <= sigma:
            return True

def createRHS(pairlist: list):
    l = []
    for i in range(len(pairlist)):
        l.append(pairlist[i].pairlist)
    return l

def getAttrbutes(filename: str):
    attrs = pd.read_csv(filename, header=None)
    sx = []
    df = pd.DataFrame(attrs)
    for i in range(0, len(df.loc[0])):
        sx.append(df.loc[0][i])
    return sx

def addthresord(title: list):
    list = []
    for i in range(len(title)):
        temp = []
        print("Please enter how many segments you want to divide the " + title[i] + " into:")
        m = int(input())
        for j in range(0, m):
            print("Please enter the allowed range：")
            sigma = float(input())
            temp.append(sigma)
        list.append(temp)
    print(list)
    return list
def addthresords(title: list):
    list = []
    for i in range(len(title)):
        temp = []
        #print("Please enter how many segments you want to divide the " + title[i] + " into:")
        m = 1
        for j in range(0, m):
            print("Please enter the allowed distance of：",title[i])
            sigma = float(input())
            temp.append(sigma)
        list.append(temp)
    print(list)
    return list


def additems(k:int,sigma,l:list):
    temp = []
    #k = 1
    for i in range(len(l)):
        for j in range(len(l)):
            if i < j:
                if is_nan(l[i]) ==False:
                    if is_nan(l[j]) ==False:
                        if similars(sigma, l[i], l[j]):
                            templ = []
                            templ.append(i+1)
                            templ.append(j+1)
                            temp.append(templ)

    if len(temp) < k:
        return []
    return temp
def diff(l1:list):
    l1 = [x for x in l1 if x]
    temp = l1.copy()
    #print(l1)
    for i in range(len(l1)):
        for j in range(len(l1)):
            if j > i:
                #print(l1[i],l1[j])
                if set(l1[j]).issubset(set(l1[i])):
                    if l1[j] in temp:
                        temp.remove(l1[j])
    return temp

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
                #print(type(judge))
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
    x = diff(maxmalobjects)
    return x

def itertools_chain(a):
    l =  list(itertools.chain.from_iterable(a))
    for i in range(len(l)):
        for j in range(len(l[i])):
            l[i] = list(l[i])
    return l


def jiaoji(listA, listB):
    # Intersection

    retB = list(set(listA).intersection(set(listB)))

    return retB
def bingji(listA,listB):
    # Intersection
    retC = [i for i in listB if i in listA]
    return retC
def chaji(listA,listB):
    #difference
    retE = [i for i in listB if i not in listA]
    return retE

def quchong(l1):
    #duplicate removal
    t = l1[:]
    for i in l1:
        while t.count(i) > 1:
            del t[t.index(i)]
    # order
    t.sort(key=l1.index)
    return t

def spilt(l:list):
    for i in range(len(l)):
        for j in range(len(l[i])):
            x = list(itertools.combinations(l[i][j],2))
            l[i][j] = x
    for i in range(len(l)):
        l[i] = itertools_chain(l[i])
    return l

def detect(rhs:list,cond:list):
    '''

    :param rhs:RHS
    :param cond: The itemsets wait for detect
    :return: if whole the items are in the RHS then return
    '''
    c = rhs.copy()
    for i in range(len(cond)):
        if cond[i] in rhs:
            c.remove(cond[i])
    return c
