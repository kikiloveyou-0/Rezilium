import pygame

def main():
    pygame.init()

    taille_ecran = (800, 600)
    ecran = pygame.display.set_mode(taille_ecran)

    enter = pygame.image.load("D:\Rezilium\press_enter.png")
    fleches = pygame.image.load("D:\Rezilium\pleches.png")
    E = pygame.image.load("D:\Rezilium\E.png")
    noms = pygame.image.load("D:\Rezilium\noms.png")
    jeu_en_cours = True

    while jeu_en_cours:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jeu_en_cours = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    jeu_en_cours = False
                elif event.key == pygame.K_RETURN:
                    print("303")

        ecran.blit(enter, (370,270))
        ecran.blit(fleches, (20,20))
        ecran.blit(E, (150,40))
        ecran.blit(noms, (600,400))
        pygame.display.flip()



    pygame.quit()

if __name__ == "__main__":
    main()

