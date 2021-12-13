# You will want this import for Step 4
from operator import itemgetter

def countWords(counts, line):
    # You should write this function in Step 1,
    words = line.split()
    for i in words:
        i = i.strip('-?.!,[]—:;"\'')
        i = i.lower()
        if i in counts.keys():
            counts[i] += 1
            pass
        if i not in counts.keys():
            counts[i] = 1
            pass
        pass
    # and improve it in Step 2
    return counts

def printResults(counts):
    # You will replace this code in Step 3 and 4
    ans = []
    for key, value in counts.items():
        ans.append((key, value))
        pass
    ans = sorted(ans, key=lambda ans: ans[0])
    for i in ans:
        print('{0} : {1}'.format(i[0], i[1]))
        pass
    pass


# You do not need to modify this function.
# It will call your countWords and printResults functions
def countFile(fname):
    counts = {}
    with open(fname) as f:
        for line in f:
            countWords(counts, line)
            pass
        pass
    printResults(counts)
    pass

def main():
    countFile("/usr/local/p3ws/words/caesar.txt")
    pass

if __name__ == '__main__':
    main()
    pass
