import requests

from config import CONFIG

def send(payload):

    print(payload)

    """
    response = requests.post(
        CONFIG["odoo"]["url"],
        json=payload,
        headers={
            "Authorization":
            f'Bearer {CONFIG["odoo"]["token"]}'
        }
    )

    return response.status_code
    """

    return 200