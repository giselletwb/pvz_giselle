import pygame

class Peashooter(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.current_image_index = 0
        self.count = 0

        for i in range(18):
            loc = 'resources/graphics/Plants/SunFlower/SunFlower' + str(i) + '.png'
            img = pygame.image.load(loc)
            self.images.append(img)

        self.image = self.images[self.current_image_index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (260, 270)


    def switch_image(self):
        self.image = self.images[self.current_image_index]

        if self.current_image_index == len(self.images) - 1:
            self.current_image_index = 0
        else:
            self.current_image_index += 1

    def update(self, elapsed_time):



        if self.count >= 5:

           self.switch_image()
           self.count = 0
        else:
            self.count += 1
