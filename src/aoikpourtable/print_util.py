# coding: utf-8
#


import sys


#
def print_stderr(msg):
    # Write message
    sys.stderr.write(msg)

    # Write newline
    sys.stderr.write('\n')
