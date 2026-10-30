# import requests
# def test_login():
#     url="https://httpbin.org/post"
#     payload={
#         "username":"test_user",
#         "password":"123456"
#     }
#     res=requests.post(url,json=payload,timeout=10)
#     assert res.status_code ==200
#     data=res.json()
#     assert data["json"]["username"]=="test_user"
#     assert data["json"]["password"]=="123456"


# def test_extract_token():
#     data={
#         "code":0,
#         "message":"登录成功",
#         "data":{
#             "token":"abc123456"
#         }
#     }
#     assert data["code"]==0
#     token=data["data"]["token"]
#     assert token
#     assert isinstance(token,str)
#     print("获取到的Token:",token)



# def test_token_header():
#     token="abc123456"
#     headers={
#         "Authorization":f"Bearer {token}"
#     }
#     assert "Authorization" in headers
#     assert headers["Authorization"]== "Bearer abc123456"


# from api_client import APIClient
# def test_client_token():
#     client=APIClient()
#     client.set_token("abc123456")
#     headers=client.get_headers()
#     assert headers["Authorization"]=="Bearer abc123456"




from api_client import APIClient
def testt_token_authentication():
    client =APIClient()
    assert client.get_headers()=={}
    client.set_token("abc123456")
    headers=client.get_headers()
    assert headers["Authorization"]=="Bearer abc123456"