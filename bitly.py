import argparse
from urllib.parse import urlparse

import requests
from environs import Env


BITLY_API_URL = "https://api-ssl.bitly.com/v4"


def shorten_link(headers, url):
    response = requests.post(
        f"{BITLY_API_URL}/shorten",
        headers=headers,
        json={"long_url": url},
    )
    response.raise_for_status()
    return response.json()["link"]


def count_clicks(headers, link):
    parsed_url = urlparse(link)
    bitlink = f"{parsed_url.netloc}{parsed_url.path}"
    response = requests.get(
        f"{BITLY_API_URL}/bitlinks/{bitlink}/clicks/summary",
        headers=headers,
    )
    response.raise_for_status()
    return response.json()["total_clicks"]


def is_bitlink(headers, link):
    parsed_url = urlparse(link)
    bitlink = f"{parsed_url.netloc}{parsed_url.path}"
    response = requests.get(
        f"{BITLY_API_URL}/bitlinks/{bitlink}",
        headers=headers,
    )
    return response.ok


def parse_arguments():
    parser = argparse.ArgumentParser(
        description=(
            "The script allows you to quickly shorten a long link with Bitly "
            "or get total clicks for a bitlink."
        )
    )
    parser.add_argument(
        "input_url",
        help="Bitlink or long url to be shortened",
    )
    return parser.parse_args()


if __name__ == "__main__":
    env = Env()
    env.read_env() 

    api_token = env.str("BITLY_TOKEN")
    headers = {"Authorization": f"Bearer {api_token}"}

    args = parse_arguments()
    input_url = args.input_url

    if is_bitlink(headers, input_url):
        print(count_clicks(headers, input_url))
        exit()

    try:
        short_link = shorten_link(headers, input_url)
    except requests.exceptions.HTTPError as err:
        print(err)
        exit("Make sure the url is correct")
    print(short_link)
