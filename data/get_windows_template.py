#!/usr/bin/env python

def get_windows(seq: str, windowsize: int, stepsize: int) -> list:
    """Given a string, windowsize (int) and step size (int),
    returns a list of windows of the windowsize.
    E.g. "TACTGG", 3, 2 => ["TAC", "CTG"]
    """
    pass        #pass is a keyword in Python we can use as a placeholder
                #before we finish writing our code, replace it with your
                #own code to complete the function

seq = "ACGGTAGACCT"
print(get_windows(seq, 3, 1))

assert get_windows(seq, 3, 1) == ['ACG', 'CGG', 'GGT', 'GTA', 'TAG', 'AGA', 'GAC', 'ACC', 'CCT'], \
    "Does not pass windowsize 3, stepsize 1 test"
assert get_windows(seq, 3, 3) == ['ACG', 'GTA', 'GAC'], "Does not pass windowsize 3, stepsize 3 test"
assert get_windows(seq, 3, 5) == ['ACG', 'AGA']
assert get_windows(seq, 5, 2) == ['ACGGT', 'GGTAG', 'TAGAC', 'GACCT']
assert get_windows(seq, 3, 3)[-1] != 'T', "Function returns partial windows"
print("All tests passed")