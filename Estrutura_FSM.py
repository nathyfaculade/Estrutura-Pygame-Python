import pygame
import sys

#(Variaveis globais, parte de inicialização)

#Funções de Estados
def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_ESCAPE:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
                    sys.exit()

            #Renderização do Menu
            screen.fill(BLACK)

            #Desenho o titulo e as instruções
            pygame.display.flip()



def game_loop():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        #Setar a bola e as raquete, colisão.

        #Controle, Colisão, Score

        #Rendelizar Score e o FPS




