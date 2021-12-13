#  Now try a few Emacs/Python things yourself:
#
#  First: Have Emacs properly reformat the code
#
#  Second: Evaluate the entire buffer (run it in Python)
#
#  Third:  Copy the last line (which prints factorial(7))
#          and paste another copy of it at the end of the file.
#          Changed the new copy of the line to print the factorial of 9
#          instead of the factorial of 7.
#
#  Fourth: Evaluate just the newly copied line (run it in Python)
#          Reminder: set the mark to begin selection


def fact(n):
    if(n<=0):
        return 1
    return n*fact(n-1)

print("The factorial of 3 is "+str(fact(3)))

print("The factorial of 7 is "+str(fact(7)))



