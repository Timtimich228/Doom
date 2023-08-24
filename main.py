import pygame
import pygame.mixer_music
from nastroiki import *
from player import Player
from map import *
from music import *
pygame.init()
game_active = False
screen = pygame.display.set_mode((width,height))
pygame.mouse.set_visible(False)
pygame.display.set_caption('Wolfenstein 3d')
ammo = 8
text_fontss = pygame.font.Font('font/Pixeltype (1).ttf',70)
text_fontss2 = pygame.font.Font('font/Pixeltype (1).ttf',40)
text_fontss3 = pygame.font.Font('font/Pixeltype (1).ttf',50)
start_text = text_fontss.render('Start Game',False,'white')
fon2 = pygame.image.load('images/wallpaperflare.com_wallpaper.jpg').convert_alpha()
fon2 = pygame.transform.scale(fon2,(width,height))
start_text2 = text_fontss.render('Exit',False,'white')
start_text3 = text_fontss.render('Press key "W" to continue',False,'white')
start_text4 = text_fontss2.render('Episode 1: Escape from Wolfenstein',False,'white')
start_text5 = text_fontss.render('........',False,'black')
superstar_text = text_fontss3.render('LEVEL: 1',False,'white')
superstar_text2 = text_fontss3.render('SCORE:',False,'white')
superstar_text3 = text_fontss3.render('LIVES: 1',False,'white')
superstar_text4 = text_fontss3.render('HEALTH:',False,'white')
superstar_text5 = text_fontss3.render(f'AMMO:{ammo}',False,'white')
superstar_image = pygame.image.load('images/pngwing.com2.png').convert_alpha()
superstar_image = pygame.transform.scale(superstar_image,(190,140))
superstar_image2 = pygame.image.load('images/Pistol.png').convert_alpha()
superstar_image2 = pygame.transform.scale(superstar_image2,(190,140))
superstar_image3 = pygame.image.load('images/pngwing.com2.png').convert_alpha()
superstar_image3 = pygame.transform.scale(superstar_image3,(190,140))
logo = pygame.image.load('images/Daco_4257309.png').convert_alpha()
logo = pygame.transform.scale(logo,(700,150))
pistol = pygame.image.load('images/pngwing.com.png').convert_alpha()
pistol = pygame.transform.scale(pistol,(100,100))
gun1 = pygame.image.load('images/gun_0.png').convert_alpha()
gun1 = pygame.transform.scale(gun1,(400,400))
gun2 = pygame.image.load('images/gun_1.png').convert_alpha()
gun2 = pygame.transform.scale(gun2,(400,400))
gun3 = pygame.image.load('images/gun_2.png').convert_alpha()
gun3 = pygame.transform.scale(gun3,(400,400))
knife = pygame.image.load('images/Knife.png').convert_alpha()
knife = pygame.transform.scale(knife,(190,130))
real_knife = pygame.image.load('images/Jagknife.png').convert_alpha()
real_knife = pygame.transform.scale(real_knife,(400,400))
texture_atlas = pygame.image.load('images/1375.png').convert_alpha()
texture_rectangles = {
    'texture1': pygame.Rect(200, 200, 50, 50),
}
texture_name = 'texture1'
wall_texture = texture_atlas.subsurface(texture_rectangles[texture_name])
wall_texture = pygame.transform.scale(wall_texture,(2,2))
move_texture = False
guns_anima = [gun2,gun3]
sprites_of_gun = None
for i in guns_anima:
    sprites_of_gun = i
pygame.time.set_timer(pygame.USEREVENT, 10000)
clock = pygame.time.Clock()
text_font = pygame.font.Font(None,24)
exit_game = False
startus2 = False
letsgo = False
player = Player()
play_music = False
pistolTrue = False
stringus_music = False
pistolFalse = False
noj = False
gun_animation = False
knife_animation = False
rust = True
nachalo = False
fon = False
def ray_casting():
    global move_texture
    for ray in range(rays):
        start_lines = player.angle - HALF_FOV + ray * step_angle
        distance_to_wall = 0
        cos_player_angle = math.cos(start_lines)
        sin_player_angle = math.sin(start_lines)
        color_set = False
        texture = None
        hit_wall = False
        while not hit_wall and distance_to_wall < max_depth:
            distance_to_wall += 1
            target_x = player.x - cos_player_angle * distance_to_wall
            target_y = player.y + sin_player_angle * distance_to_wall
            col = int(target_x / block_size)
            row = int(target_y / block_size)

            if (col * block_size, row * block_size) in world_map:
                hit_wall = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                    move_texture = True
        if hit_wall:
            if color_set:
                texture = wall_texture
            else:
                color = '#2905B9'
            if (col, row) in colorversus:
                color = 'white'
            ray_angle = start_lines - player.angle
            distance_to_wall = distance_to_wall * math.cos(ray_angle)
            wall_height = (block_size / distance_to_wall) * (distance_to_screen / 2)
            wall_top = (height / 2) - (wall_height / 2)
            pygame.draw.rect(screen, color, (ray * scale, wall_top, scale, wall_height))


while True:
    screen.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                fon = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    move_texture = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    menu_toogle = pygame.mixer_music.play()
                    start_text = text_fontss.render('Start Game', False, 'black')
                    start_text2 = text_fontss.render('Exit', False, 'white')
                    pistolTrue = True
                    pistolFalse = False
                    exit_game = False
                    startus2 = True
                if event.key == pygame.K_SPACE:
                    if startus2:
                        nachalo = True
                if event.key == pygame.K_UP:
                    if nachalo:
                        menu_toogle = pygame.mixer_music.play()
                        start_text4 = text_fontss2.render('Episode 1: Escape from Wolfenstein', False, 'black')
                        letsgo = True
                if event.key == pygame.K_SPACE:
                    if letsgo:
                        game_active = True
                        stringus_music = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:

                    menu_toogle = pygame.mixer_music.play()
                    start_text = text_fontss.render('Start Game', False, 'white')
                    start_text2 = text_fontss.render('Exit', False, 'black')
                    pistolTrue = False
                    pistolFalse = True
                    exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if exit_game:
                        quit()
            if rust:
                if event.key == pygame.K_f:
                    pistol_music.play()
                    gun_animation = True
            if noj:
                if event.key == pygame.K_f:
                    knife_animation = True

    if game_active:
        if stringus_music:
            menu_toogle = None
            fon_music2.stop()
            start_game_music = pygame.mixer_music.play()
        player.move()
        pygame.draw.rect(screen, (40,40,40), (0, 0, width, half_height))
        pygame.draw.rect(screen, (90,90,90), (0, half_height, width, half_height))
        point = pygame.draw.rect(screen, 'red', (half_width, half_height, 5, 5))
        ray_casting()
        pygame.draw.rect(screen, 'blue', (0,470, width, 250))
        screen.blit(superstar_text,(30,500))
        pygame.draw.rect(screen, 'white', (160, 470, 2, 200))
        screen.blit(superstar_text2, (180, 500))
        pygame.draw.rect(screen, 'white', (320, 470, 2, 200))
        screen.blit(superstar_text3, (340, 500))
        pygame.draw.rect(screen, 'white', (500, 470, 2, 200))
        screen.blit(superstar_image,(490,465))
        pygame.draw.rect(screen, 'white', (665, 470, 2, 200))
        screen.blit(superstar_text4, (670, 500))
        pygame.draw.rect(screen, 'white', (820, 470, 2, 200))
        screen.blit(superstar_text5, (830, 500))
        pygame.draw.rect(screen, 'white', (940, 470, 2, 200))
        pygame.draw.rect(screen, 'white', (960, 470, 2, 200))
        screen.blit(superstar_image2,(980,470))

        pygame.draw.rect(screen, 'gray', (0, 470,1200, 5))
        point = pygame.draw.rect(screen, 'red', (half_width, half_height, 5, 5))
        if gun_animation:
            screen.blit(gun2,(400,70))
            screen.blit(gun3, (400, 70))
            ammo -= 1
            superstar_text5 = text_fontss3.render(f'AMMO:{ammo}', False, 'white')
            pygame.draw.rect(screen,'red',(595,300,20,20))
            gun_animation = False
        else:
            screen.blit(gun1,(400,70))
        if ammo <= 0:
            gun1 = pygame.transform.scale(gun1, (0, 0))
            screen.blit(knife, (980, 480))
            screen.blit(real_knife, (420,70))
            superstar_text5 = text_fontss3.render(f'AMMO: 0', False, 'white')
            gun_animation = False
            rust = False
            noj = True
            if knife_animation:

                knife_music.set_volume(0.4)
                knife_music.play()
                real_knife = pygame.transform.scale(real_knife, (400, 410))
                pygame.draw.rect(screen, 'red', (610, 300, 10, 10))
                screen.blit(real_knife,((420,50)))
                knife_animation = False
            else:
                screen.blit(real_knife, (420, 70))
        fps2 = clock.get_fps()
        text_fps = text_font.render(f'FPS:{int(fps2)}', False, 'green')
        screen.blit(text_fps,(0,0))
        pygame.display.flip()
        clock.tick(FPS)
    elif nachalo:
        screen.fill('red')
        pygame.draw.rect(screen, (70, 70, 70), (300, 100, 650, 400))
        screen.blit(logo, (half_width - 350, 0))
        screen.blit(start_text4, (half_width-200, 200))
        screen.blit(start_text5, (half_width - 200, 210))
        screen.blit(start_text5, (half_width - 200, 240))
        screen.blit(start_text5, (half_width - 200, 270))
        pygame.display.flip()
    else:
        if fon:
            fon_music.stop()
            fon_music2.set_volume(0.1)
            fon_music2.play()
            screen.fill('red')
            pygame.draw.rect(screen,(70,70,70),(300,100,650,400))
            screen.blit(logo, (half_width-350, 0))
            screen.blit(start_text,(half_width-90,200))
            screen.blit(start_text2, (half_width - 90, 300))
            if pistolTrue:
                screen.blit(pistol, (400, 160))
            if pistolFalse:
                screen.blit(pistol, (400, 270))
            pygame.display.flip()

        else:
            screen.blit(fon2,(0,0))
            screen.blit(start_text3,(half_width,500))
            pygame.display.flip()
            play_music = True
            fon_music.set_volume(0.1)
            fon_music.play()
