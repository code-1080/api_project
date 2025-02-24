import requests
from io import BytesIO


def show_map(params=None, server=None):
    # key = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"
    #
    # url = f"https://static-maps.yandex.ru/v1?ll={lon},{lat}&spn={spn[0]},{spn[1]}&apikey={key}"

    response = requests.get(server, params=params)

    if response.status_code == 200:
        image = BytesIO(response.content)

        return image


# show_map("37.123", "37.123", [1.6, 0.6])

