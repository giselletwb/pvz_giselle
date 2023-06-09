import pygame
from zombie import Zombie
from peashooter import Peashooter
from bullet import Bullet
from sun import Sun


pygame.init()

RES = (1400, 600)
FPS = 60

bg = pygame.image.load('resources/graphics/Items/Background/Background_0.jpg')

screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

# ZOMBIES
zombie = Zombie()

zombie_group = pygame.sprite.Group()
zombie_group.add(zombie)

# PLANTS
peashooter = Peashooter()

plant_group = pygame.sprite.Group()
plant_group.add(peashooter)

# BULLET

bullet_group = pygame.sprite.Group()

# SUN
sun = Sun(600, 0)

sun_group = pygame.sprite.Group()
sun_group.add(sun)

while True:
    clock.tick(FPS)

    elapsed_time = pygame.time.get_ticks()

    #############
    # INPUT
    #############
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    ############
    # UPDATE
    #############

    if peashooter.can_shoot(elapsed_time):
        bullet = Bullet(peashooter.get_mouth_x(), peashooter.get_mouth_y())
        bullet_group.add(bullet)



    zombie.update()
    peashooter.update(elapsed_time)
    bullet_group.update(zombie_group)
    sun_group.update(elapsed_time)

    #############
    # DRAW
    #############
    screen.blit(bg, (0,0))

    zombie_group.draw(screen)

    plant_group.draw(screen)

    bullet_group.draw(screen)

    sun_group.draw(screen)



    pygame.display.update()