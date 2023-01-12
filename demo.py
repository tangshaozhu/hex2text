import sys
from hex2text import get_data_from_hex

data = get_data_from_hex('demo.txt', 2, 10)

if len(sys.argv) == 1: 
    for d in data:
        print(d)
else:
    with open(sys.argv[1], 'w') as f:
        for d in data:
            f.write(d)
            f.write('\n')
