block_size = 64
map_size = 12
sprite_hit = False
map =[
     'WWWWWWWDWWWWWWW',
     'W....W....W...W',
     'W....D....D...W',
     'W....W....W...W',
     'WWWWWW....WWWWW',
     'W....W....W...W',
     'W....D....D...W',
     'W....W....WWWWW',
     'W.WWWW.....S..W',
     'WWWWWWWWWWWWWWWW'
]
block_size += map_size
colorversus = []
world_map = set()
sprite_world_map=set()
for i,col in enumerate(map):
    for j,row in enumerate(col):
        if row == 'W':
            world_map.add((i*block_size,j*block_size))
        if row == 'D':
            world_map.add((i * block_size, j * block_size))
            colorversus.append((i, j))


