import pygame
from pygame.locals import *
import random
import os

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 864
screen_height = 936
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird Comes to UJ!')

# Game variables
ground_scroll = 0
scroll_speed = 4
background_scroll = 0
bg_scroll_speed = 0.1
flying = False
game_over = False
pipe_gap = 150
pipe_frequency = 1500
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0
high_score = 0
score_timer = pygame.time.get_ticks()
fade_out_alpha = 255

# Load blocky font
try:
    font_path = 'public/PressStart2P.ttf'  # Add font here
    font = pygame.font.Font(font_path, 30)
except:
    font = pygame.font.SysFont('Arial', 30)

# Load images
bg = pygame.image.load('public/bg.png')
ground_img = pygame.image.load('public/ground.png')
restart_img = pygame.image.load('public/restart.png')
welcome_img = pygame.image.load('public/welcome.png').convert_alpha()
bubble_img = pygame.image.load('public/bubble.png').convert_alpha()

# Button
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        screen.blit(self.image, self.rect)
        return action

# Bird
class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = [pygame.image.load(f'public/bird{n}.png') for n in range(1, 4)]
        self.index = 0
        self.counter = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.clicked = False

    def update(self):
        if flying:
            self.vel += 0.5
            self.vel = min(self.vel, 8)
            if self.rect.bottom < 768:
                self.rect.y += int(self.vel)

        if not game_over:
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                self.vel = -10
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            self.counter += 1
            if self.counter > 10:
                self.counter = 0
                self.index = (self.index + 1) % len(self.images)

            self.image = pygame.transform.rotate(self.images[self.index], self.vel * -1.5)
        else:
            self.image = pygame.transform.rotate(self.images[self.index], -25)

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('public/pipe.png')
        self.rect = self.image.get_rect()
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - pipe_gap // 2]
        else:
            self.rect.topleft = [x, y + pipe_gap // 2]

    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
            self.kill()

# Groups
bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()
flappy = Bird(100, screen_height // 2)
bird_group.add(flappy)
button = Button(screen_width // 2 - 70, screen_height // 2 - 50, restart_img)

# Main loop
run = True
show_welcome = True
while run:
    clock.tick(fps)

    # Draw background
    screen.blit(bg, (background_scroll, 0))
    bird_group.draw(screen)
    bird_group.update()
    pipe_group.draw(screen)
    screen.blit(ground_img, (ground_scroll, 768))

    # Show welcome screen before start
    if show_welcome:
        screen.blit(welcome_img, (screen_width // 2 - welcome_img.get_width() // 2, 200))
        screen.blit(bubble_img, (flappy.rect.centerx - bubble_img.get_width() // 2, flappy.rect.top - 100))

        if flying and fade_out_alpha > 0:
            fade_out_alpha -= 10
            welcome_img.set_alpha(fade_out_alpha)
            bubble_img.set_alpha(fade_out_alpha)
        if fade_out_alpha <= 0:
            show_welcome = False

    # Score meter
    if flying and not game_over:
        if pygame.time.get_ticks() - score_timer >= 1000:
            score += 1
            score_timer = pygame.time.get_ticks()
        score_text = font.render(f'{score}m', True, (255, 255, 255))
        screen.blit(score_text, (screen_width - 150, 30))

    # Collision
    if flappy.rect.bottom >= 768 or flappy.rect.top <= 0:
        game_over = True
    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False):
        game_over = True

    if flying and not game_over:
        if pygame.time.get_ticks() - last_pipe > pipe_frequency:
            pipe_height = random.randint(-100, 100)
            pipe_group.add(Pipe(screen_width, screen_height // 2 + pipe_height, 1))
            pipe_group.add(Pipe(screen_width, screen_height // 2 + pipe_height, -1))
            last_pipe = pygame.time.get_ticks()

        ground_scroll = (ground_scroll - scroll_speed) % 36
        background_scroll = (background_scroll - bg_scroll_speed) % 26
        pipe_group.update()

    if game_over:
        if game_over:
            final_score_text = font.render(f'You travelled {score}m to get to Class', True, (255, 255, 255))
            screen.blit(final_score_text, (screen_width // 2 - final_score_text.get_width() // 2, screen_height // 2 - 120))
        if button.draw():
            game_over = False
            flying = False
            score = 0
            score_timer = pygame.time.get_ticks()
            pipe_group.empty()
            flappy.rect.center = (100, screen_height // 2)
            flappy.vel = 0
            fade_out_alpha = 255
            show_welcome = True

    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type == MOUSEBUTTONDOWN and not flying and not game_over:
            flying = True
            score_timer = pygame.time.get_ticks()

    pygame.display.update()

pygame.quit()