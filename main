import pygame
from api_file import show_map
from TimurTextInput import TextBox
from button import Button
import requests


def change_theme():
    global params
    if params['theme'] == 'light':
        params['theme'] = 'dark'
    else:
        params['theme'] = 'light'


def find_object(search_server=None, search_params=None):
    global params, server
    response = requests.get(search_server, params=search_params)
    if not response:
        # обработка ошибочной ситуации
        pass
    json_response = response.json()
    # Получаем первый топоним из ответа геокодера.
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    # Координаты центра топонима:
    toponym_coodrinates = toponym["Point"]["pos"]
    # Долгота и широта:
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    params['ll'] = ",".join((toponym_longitude, toponym_lattitude))
    return show_map(params=params, server=server)


if __name__ == "__main__":
    pygame.init()
    size = (600, 500)
    w, h = input("Введите координаты места: ").split()
    spn = input("Введите масштаб: ").split()

    screen = pygame.display.set_mode(size)

    server = 'https://static-maps.yandex.ru/v1'

    search_server = "http://geocode-maps.yandex.ru/1.x/"

    params = {'ll': ",".join((w, h)),
              'apikey': "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13",
              "spn": ",".join(spn),
              'theme': 'light'}

    search_params = {
        "apikey": "8013b162-6b42-4997-9691-77b7074026e0",
        "geocode": '',
        "format": "json"}

    img_data = show_map(params=params, server=server)
    if img_data:
        img = pygame.image.load(img_data)
    else:
        print("Не удалось загрузить карту")
        pygame.quit()

    place_input = TextBox(5, 455, 200, 40, 20)

    search_btn = Button(210, 455, 'Искать')

    theme_btn = Button(310, 455, 'Сменить тему')

    point = None
    point_coords = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if search_btn.is_hovered:
                        search_params["geocode"] = place_input.text
                        img = pygame.image.load(find_object(search_server=search_server, search_params=search_params))
                        point = pygame.transform.scale(pygame.image.load('Map-Pin.png'), (10, 20))
                        point_coords = (size[0] // 2 - 5, (size[1] - 50) // 2 - 20)
                    if theme_btn.is_hovered:
                        change_theme()
                        img = pygame.image.load(show_map(params=params, server=server))
            place_input.input(event)

        if pygame.key.get_pressed()[pygame.K_RETURN]:
            search_params["geocode"] = place_input.text
            img = pygame.image.load(find_object(search_server=search_server, search_params=search_params))
            point = pygame.transform.scale(pygame.image.load('Map-Pin.png'), (10, 20))
            point_coords = (size[0] // 2 - 5, (size[1] - 50) // 2 - 20)

        screen.fill((255, 255, 255))
        screen.blit(img, (0, 0))
        place_input.draw(screen)
        search_btn.draw(screen)
        theme_btn.draw(screen)
        search_btn.update(pygame.mouse.get_pos())
        theme_btn.update(pygame.mouse.get_pos())
        if point is not None:
            screen.blit(point, point_coords)
        pygame.display.flip()

    pygame.quit()
