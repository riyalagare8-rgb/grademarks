import sys

if len(sys.argv) != 6:
    print("Please provide exactly 5 subject marks as command-line arguments.")
    sys.exit(1)

try:
    
    marks = [int(mark) for mark in sys.argv[1:6]]
    
