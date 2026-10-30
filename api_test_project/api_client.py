import requests
class APIClient:
    def __init__(self):
        self.base_url="https://jsonplaceholder.typicode.com"
        self.token=None
    def set_token(self,token):
        self.token=token
    def get_headers(self):
        headers={}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers
    def get(self,path):
        url=f"{self.base_url}{path}"
        headers=self.get_headers()
        res=requests.get(url,timeout=10)
        return res

    def post(self,path,payload):
        url=f"{self.base_url}{path}"
        headers =self.get_headers()
        res=requests.post(
            url,
            json=payload,
            timeout=10
        )
        return res
    def put(self,path,payload):
        url=f"{self.base_url}{path}"
        headers=self.get_headers()
        res =requests.put(
            url,
            json=payload,
            timeout=10
        )
        return res
    def delete(self,path):
        url = f"{self.base_url}{path}"
        headers=self.get_headers()
        res =requests.delete(url,timeout =10)
        return res

