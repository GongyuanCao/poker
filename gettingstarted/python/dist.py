import random


def d(n, sidecount):
    """Rolls n dice, each of which has sidecount sides

      The param n is an int which specifies the number of dice.
      The param sidecount is an int which specifies the number of sides on each
      die.
      The return value is an int which is the total result of the roll
    """
    total = 0
    for i in range(0, n):
        #  Roll one die and add it to the total
        total += random.randint(1, sidecount)
        pass
    return total


def histogram(f, n):
    """Computes a histogram of the result of calling f() n times.
    The param f is a function which takes no arguments and returns a value.
    The param n is the number of times to call the function.
    The return value is a dictionary mapping return values of f() to the
    number of times they were observed.
    """
    results = {}
    for i in range(0, n):
        curr = f()
        if (curr in results):
            #  if we have already seen the value, increment the count
            results[curr] = results[curr] + 1
            pass
        else:
            #  otherwise, this is the first one
            results[curr] = 1
        pass
    return results


def printHistogram(hist):
    """Prints out a histogram in order from smallest to largest
    The param hist is the histogram (dictionary) which maps each value to the
    number of times it was observed. E.g., the return value of the histogram
    function.  Note that while histogram accepts functions of any return type,
    This function requires the keys in the dictionary to be orderable.
    This function returns no value.  It prints the results.
    """
    lo = None
    hi = None
    total = 0
    #  compute minimum value, maximium value, and total observations
    for k in hist:
        if (lo is None or k < lo):
            lo = k
            pass
        if (hi is None or k > hi):
            hi = k
            pass
        total = total + hist[k]
        pass
    #  the cumulative fraction seen so far
    cumulative = 0
    for i in range(lo, hi + 1):
        if (i in hist):
            curr = hist[i] / total
            cumulative = cumulative + curr
            pass
        else:
            curr = 0.0
            pass
        #  E.g.
        #  20: 6.829400% (cumulative: 35.280000%)
        print("{:3d}: {:%} (cumulative: {:%})".format(i, curr, cumulative))
        pass
    pass
