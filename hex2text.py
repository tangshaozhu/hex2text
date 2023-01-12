def _get_num_str(hexstr, width, base=10):
    if base not in [2, 8, 10, 16]:
        raise Exception("width value must be 1, 2, 4 or 8")
    bytes = []
    bytenum = width
    for i in range(width)[::-1]:
        bytes.append(hexstr[i*2:i*2+2])
    num_str = ''.join(bytes)
    if base == 16:
        return num_str
    num = int(num_str, 16)
    if base == 2:
        return bin(num)
    if base == 8:
        return oct(num)
    if base == 10:
        return str(num)


def get_data_from_hex(file, width, base):
    if width not in [1, 2, 4, 8]:
        raise Exception("width value must be 1, 2, 4 or 8")
    data = []
    with open(file, 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if i >= 1:
                datasize = int(line[1:3], 16)
                typesize = datasize // width
                offset = 9
                for j in range(typesize):
                    data.append(_get_num_str(line[offset:], width, base))
                    offset = offset + width * 2
    return data
