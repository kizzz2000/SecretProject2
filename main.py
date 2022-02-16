import pygame
import sys

x = 0
y = 0


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load("1.png"))
        self.sprites.append(pygame.image.load("2.png"))
        self.sprites.append(pygame.image.load("3.png"))
        self.sprites.append(pygame.image.load("4.png"))
        self.sprites.append(pygame.image.load("5.png"))
        self.sprites.append(pygame.image.load("6.png"))
        self.sprites.append(pygame.image.load("7.png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def animate(self):
        self.is_animating = True

    def update(self):
        if self.is_animating == True:
            self.current_sprite += 0.25

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.sprites[int(self.current_sprite)]






#General setup
pygame.init()
clock = pygame.time.Clock()

#Game screen
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Sprite Animation")

#Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(100,100)
moving_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



        if event.type == pygame.KEYDOWN:
            player.animate()


    #drawing
    screen.fill((0,0,0))
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()
    clock.tick(60)