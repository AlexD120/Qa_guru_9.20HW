import logging
import allure
import curlify
import requests
from allure_commons.types import AttachmentType

BASE_URL = "https://demowebshop.tricentis.com/"


def post_request(url, **kwargs):
    url = BASE_URL + url
    with allure.step(f"POST {url}"):
        response = requests.post(url, **kwargs)
        curl = curlify.to_curl(response.request)
        allure.attach(
            body=curl, name="curl", attachment_type=AttachmentType.TEXT, extension="txt"
        )
        logging.info(curlify.to_curl(response.request))
        return response
