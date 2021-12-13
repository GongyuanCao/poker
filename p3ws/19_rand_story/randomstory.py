import re
import random
from collections import defaultdict

def readWordList(thetype):
    words = []
    with open('{0}.txt'.format(thetype)) as f:
        for line in f:
            words.append(line)
            pass
        pass
    nwords = []
    for i in words:
        i = i[:-1]
        nwords.append(i)
        pass
    return nwords

def makedic(types):
    dic = {}
    types = list(types)
    for i in types:
        j = "_{0}".format(i)
        dic[j] = readWordList(i)
        pass
    return dic

def randomWordfortype(dic, atype):
    for key in dic.keys():
        if key == atype:
            rword = random.choice(dic[key])
            pass
        pass
    return rword

def randomStory(myfile, types):
    cat = []
    backcat = {}
    flag = []
    dic = makedic(types)
    with open(myfile) as f:
        for line in f:
            words = line.split()
            for i in words:
                if re.match(r'_\w', i):
                    cat.append(re.findall(r"_\w*", i))
                    pass
                pass
            pass
        pass
    cat = [i for item in cat for i in item]
    catd = defaultdict(list)
    count = {}
    fcount = {}
    for i in range(len(cat)):
        if re.match(r'_[a-z]', cat[i]):
            flag.append("_{0}".format(i))
            #if cat[i] not in catd.keys():
            catd[cat[i]].append(randomWordfortype(dic, cat[i]))
            backcat[flag[-1]] = catd[cat[i]][-1]
            pass
        pass
    for i in range(len(cat)):
        if re.match(r'_[0-9]', cat[i]):
            if cat[i] not in backcat.keys():
                backcat[cat[i]] = backcat[cat[int(cat[i][1:])]]
                pass
            pass
        pass
    print(cat)
    print(catd)
    print(backcat)
    for i in cat:
        fcount[i] = 0
        if i in count.keys():
            count[i] += 1
            pass
        if i not in count.keys():
            count[i] = 1
            pass
        pass
    ans = []
    with open(myfile) as f:
        for line in f:
            if line == None:
                continue
            newl = line
            for i in range(len(cat)):
                if re.match(r'_[a-z]', cat[i]):
                    if re.search(r'{0}'.format(cat[i]), newl):
                        if count[cat[i]] == 1:
                            newl = newl.replace(cat[i], catd[cat[i]][0])
                        #    print(cat[i])
                            pass
                        if count[cat[i]] != 1:
                        #if fcount[cat[i]] == 0:
                            newl = newl.replace(cat[i], catd[cat[i]][fcount[cat[i]]], 1)
                            fcount[cat[i]] += 1
                        #    print(fcount)
                        #    print(newl)
                            pass
                        #else:
                        #    newl = newl.replace(cat[i], catd[cat[i]][fcount[cat[i]]])
                        #    print(fcount)
                        #    print(newl)
                        pass
                    pass
                pass
            for i in range(len(cat)):
                if re.fullmatch(r'_[0-9][0-9]', cat[i]):
                    newl = newl.replace(cat[i], backcat[cat[i]])
                    pass
            for i in range(len(cat)):
                if re.fullmatch(r'_[0-9]', cat[i]):
                    newl = newl.replace(cat[i], backcat[cat[i]])
                    pass
                pass
            ans.append(newl)
            pass
        pass
    ans = "".join(ans)
    return ans

def main():
    print(randomStory('newstory.txt', ['animal', 'food', 'greeting', 'magiccreature', 'place', 'said', 'thing', 'time']))
    pass

if __name__ == "__main__":
    main()
    pass

