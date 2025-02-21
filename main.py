import pygame
from api_file import show_map


def main():
    pygame.init()
    size = (600, 450)
    w, h = input("Введите координаты места: ").split()
    spn = input("Введите масштаб: ").split()

    img_data = show_map(w, h, spn)
    if img_data:
        img = pygame.image.load(img_data)
    else:
        print("Не удалось загрузить карту")
        return 
    
    screen = pygame.display.set_mode(size)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        screen.blit(img, (0, 0))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
