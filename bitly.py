from urllib.parse import urlparse

import requests
from environs import Env


BITLY_API_URL = "https://api-ssl.bitly.com/v4"


def shorten_link(token, url):
    response = requests.post(
        f"{BITLY_API_URL}/shorten",
        headers = {"Authorization": f"Bearer {token}"},
        json = {"long_url": url},
    )
    response.raise_for_status()
    return response.json()["link"]


def count_clicks(token, link):
    parsed_url = urlparse(link)
    bitlink = f"{parsed_url.netloc}{parsed_url.path}"
    response = requests.get(
        f"{BITLY_API_URL}/bitlinks/{bitlink}/clicks/summary",
        headers = {"Authorization": f"Bearer {token}"},
    )
    response.raise_for_status()
    return response.json()["total_clicks"]


def is_bitlink(token, link):
    parsed_url = urlparse(link)
    bitlink = f"{parsed_url.netloc}{parsed_url.path}"
    response = requests.get(
        f"{BITLY_API_URL}/bitlinks/{bitlink}",
        headers = {"Authorization": f"Bearer {token}"},
    )
    return response.ok


if __name__ == "__main__":
    env = Env()
    env.read_env() 

    api_token = env.str("BITLY_TOKEN")

    input_url = input("Enter a url: ").strip()
    if not input_url:
        exit("Make sure the url is correct")

    if is_bitlink(api_token, input_url):
        print(count_clicks(api_token, input_url))
        exit()

    try:
        short_link = shorten_link(api_token, input_url)
    except requests.exceptions.HTTPError as err:
        print(err)
        exit("Make sure the url is correct")
    print(short_link)
