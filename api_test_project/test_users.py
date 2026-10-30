# def test_get_users(client):
#     res=client.get("/users")
#     assert res.status_code ==200
#     data =res.json()
#     assert isinstance(data,list)
#     assert len(data)>0