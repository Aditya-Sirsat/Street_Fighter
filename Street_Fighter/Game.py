import pygame
import time
import random
pygame.font.init()

WIDTH,HEIGHT = 1000,800
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Game")

BG = pygame.transform.scale(pygame.image.load("Street_Fighter\\assets\images\\background\\background.jpg"),(WIDTH,HEIGHT))

PLAYER_WIDTH = 50
PLAYER_HEIGHT= 70
PLAYER_VELOCITY=10
FONT= pygame.font.SysFont("Joker",30)

def draw(player,elapsed_time):
    WIN.blit(BG,(0,0))
    time_text=FONT.render(f"Time:{round(elapsed_time)}s",1,"white")
    WIN.blit(time_text,(10,10))
    pygame.draw.rect(WIN,"orange",player)
    pygame.display.update()

def main():
    run=True

    player = pygame.Rect(500,HEIGHT-PLAYER_HEIGHT,PLAYER_WIDTH,PLAYER_HEIGHT)
    clock=pygame.time.Clock()
    start_time=time.time()
    elapsed_time=0

    while run:
        clock.tick(60)
        elapsed_time=time.time()-start_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                break

        keys = pygame.key.get_pressed() 
        if keys[pygame.K_a] and player.x-PLAYER_VELOCITY >=0:
            player.x-=PLAYER_VELOCITY
        if keys[pygame.K_d] and player.x+PLAYER_VELOCITY+PLAYER_WIDTH<=WIDTH:
            player.x+=PLAYER_VELOCITY 

        draw(player,elapsed_time)

    pygame.quit()

if __name__=="__main__":
    main()
