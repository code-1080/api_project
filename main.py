import pygame
from api_file import show_map
from TimurTextInput import TextBox
from button import Button


def change_theme():
    global params
    if params['theme'] == 'light':
        params['theme'] = 'dark'
    else:
        params['theme'] = 'light'


if __name__ == "__main__":
    pygame.init()
    size = (600, 500)
    w, h = input("Введите координаты места: ").split()
    spn = input("Введите масштаб: ").split()

    screen = pygame.display.set_mode(size)

    search_server = 'https://static-maps.yandex.ru/v1'

    params = {'ll': ",".join((w, h)),
              'apikey': "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13",
              "spn": ",".join(spn),
              'theme': 'light'}

    img_data = show_map(search_params=params, server=search_server)
    if img_data:
        img = pygame.image.load(img_data)
    else:
        print("Не удалось загрузить карту")
        pygame.quit()

    place_input = TextBox(5, 455, 100, 40, 20)

    search_btn = Button(110, 455, 'Искать')

    theme_btn = Button(210, 455, 'Сменить тему')

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if search_btn.is_hovered:
                        pass
                    if theme_btn.is_hovered:
                        change_theme()
                        img = pygame.image.load(show_map(search_params=params, server=search_server))
            place_input.input(event)

        screen.fill((255, 255, 255))
        screen.blit(img, (0, 0))
        place_input.draw(screen)
        search_btn.draw(screen)
        theme_btn.draw(screen)
        search_btn.update(pygame.mouse.get_pos())
        theme_btn.update(pygame.mouse.get_pos())
        pygame.display.flip()

    pygame.quit()
