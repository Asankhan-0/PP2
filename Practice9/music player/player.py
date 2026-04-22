import pygame
import os

pygame.init()
pygame.mixer.init()
sc = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Music Player")
font = pygame.font.SysFont("Arial", 24)
playlist = os.listdir("music")
index = 0

def start():
    pygame.mixer.music.load(os.path.join("music", playlist[index]))
    pygame.mixer.music.play()

if playlist:
    start()

running = True
while running:
    sc.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pygame.mixer.music.unpause()
            if event.key == pygame.K_s:
                pygame.mixer.music.pause()
            if event.key == pygame.K_n:
                index = (index + 1) % len(playlist)
                start_song()
            if event.key == pygame.K_b:
                index = (index - 1) % len(playlist)
                start_song()
            if event.key == pygame.K_q:
                running = False

    if playlist:
        name = font.render(f"Track: {playlist[index]}", True, (255, 255, 255))
        sc.blit(name, (50, 100))
        instr = font.render("P: Play | S: Pause | N: Next | B: Back | Q: Quit", True, (100, 100, 100))
        sc.blit(instr, (50, 200))
    else:
        sc.blit(font.render("No files in music/", True, (255, 0, 0)), (50, 100))

    pygame.display.flip()
pygame.quit()