from nastroiki import block_size


map = [
    '111111111111',
    '1..........1',
    '1...1...1..1',
    '11111...1111',
    '1..........1',
    '11111...1111',
    '1.2........1',
    '112112112111'
]

world_map = {}
for j, row in enumerate(map):
    for i, char in enumerate(row):
        if char == '1':
            world_map[(i * block_size, j * block_size)] = '1'
        elif char == '2':
            world_map[(i * block_size, j * block_size)] = '2'





