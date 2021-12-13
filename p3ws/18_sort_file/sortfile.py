def sortFile(myfile):
    with open(myfile) as f:
        s = []
        for line in f:
            s.append(line)
            pass
        s = sorted(s)
        pass
    return s

def main():
    a = sortFile('test.txt')
    print(a)
    pass

if __name__ == '__main__':
    main()
    pass
