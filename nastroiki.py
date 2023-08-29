import math
width = 1200
height = 600
FOV = math.pi/3
HALF_FOV = FOV/2
block_size = 100
rays =300
delta_angle = FOV / rays
dist = rays/(2*math.tan(HALF_FOV))
proj_coeff = dist * block_size

step_angle =FOV/rays
texture_width = 1200
texture_height = 1200
texture_scale = texture_width // block_size
half_width = width/2
half_height = height/2
player_pos = (half_width,half_height)
distance_to_screen = (width / 2) / math.tan(HALF_FOV)
scale = width // rays
max_depth = 600
wall_color = (170, 170, 170)
dark_color = (00, 0, 0)
player_angle = 0
FPS = 60
