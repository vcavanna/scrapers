"""A module to make webscraping requests easier."""

import requests

class Requester:
    CONFIG_KEYS = ["url","headers","payload"]

    def __init__(self, config: dict):
        assert(all(key in config for key in Requester.CONFIG_KEYS)), \
            "Config is missing one or more keys in the following list: {0}\nConfig: {1}"\
            .format(Requester.CONFIG_KEYS, config)
        self.config = config
        self.url = config["url"]
        self.headers = config["headers"]
        self.payload = config["payload"]

    def makeRequest(self, time):
        response = requests.request("GET", self.url, headers = self.headers, data = self.payload, timeout = time)
        return response
    
    def makePersistentRequest(self):
        """Returns a GET request. Makes the request 5 times."""

        for time in range(1,6):
            try:
                response = self.makeRequest(time)
                break
            except requests.exceptions.ReadTimeout:
                continue
        if(response):
            return response
        else:
            raise requests.exceptions.RequestError("makePersistentRequest failed after 5 attempts")