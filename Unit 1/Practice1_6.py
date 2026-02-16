# 6. Define a procedure histogram() that takes a list of integers and prints a
# histogram to the screen. For example, histogram([4, 9, 7]) should print
# the following:
# ****
# *********
# *******


def histo(lst):
    for i in lst:
        print("*" * i)

lst=[5,9,1]
histo(lst)