import pygame

pygame.init()

largeur = 1920
hauteur = 1080

fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("B-Warfare")
pygame.display.set_icon(pygame.image.load('assets/fond.jpg'))


running = True

fond = pygame.image.load('assets/fond.jpg')

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
