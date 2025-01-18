state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    text = ""
    for y in range(4):
        for x in range(4):
            text += chr(matrix[y][x])
    return text

def add_round_key(s, k):
    result = s
    for x in range(4):
        for y in range(4):
            result[x][y] = s[x][y] ^ k[x][y]
    return (result)


print(matrix2bytes(add_round_key(state, round_key)))

