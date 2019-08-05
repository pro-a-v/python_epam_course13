from http_client.httpclient import _HttpClient
import requests

class HttpClient(_HttpClient):
    def get(self, url: str) -> str:


        # if no schema in url add http://
        if (url.find('http') == -1):
            url = 'http://' + url

        req = requests.get(url)
        if req.status_code == 200:
            return req.content.decode(req.encoding)

        return None