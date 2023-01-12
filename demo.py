import sys
from hex2text import get_data_from_hex

data = get_data_from_hex('demo.txt', 2, 10)
for i, d in enumerate(data):
    print(i, d)
