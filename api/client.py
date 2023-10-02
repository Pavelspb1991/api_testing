import requests


class Client:

    @staticmethod
    def get(url):
        return requests.request("GET", url)

    @staticmethod
    def post(url, headers, payload):
        return requests.request("POST", url, headers=headers, data=payload)

    @staticmethod
    def delete(url):
        return requests.request("DELETE", url)
