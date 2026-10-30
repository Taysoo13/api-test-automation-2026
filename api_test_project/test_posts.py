# # from api_client import APIClient
# # def test_get_posts():
# #     client=APIClient()
# #     res=client.get("/posts")
# #     assert res.status_code ==200
# #     data=res.json()
# #     assert isinstance(data,list)
# #     assert len(data)>0
# #     for post in data:
# #         assert "userId" in post
# #         assert isinstance(post["id"],int) and post["id"]>0
# #         assert isinstance(post["title"],str) and post["title"] !=""
# #         assert "body" in post
# #
# # import pytest
# # from api_client import APIClient
# # @pytest.mark.parametrize("path,expected_status",[
# #     ("/users",200),
# #     ("/posts",200),
# #     ("/invalid-path",404),
# # ])
# # def test_api_status_code(path,expected_status):
# #     client=APIClient()
# #     res=client.get(path)
# #     assert res.status_code==expected_status
# #
# #
# # def test_get_single_post(client):
# #     res=client.get("/posts/1")
# #     assert res.status_code ==200,(
# #         f"预期状态码为 200，实际为{res.status_code}"
# #     )
# #     data=res.json()
# #     assert isinstance(data,dict)
# #     assert data["id"]==1
# #     assert isinstance(data["title"],str) and data["title"]!=""
# #
# #
# # def test_get_nonexistent_post(client):
# #     res = client.get("/posts/9999")
# #     assert res.status_code ==404,(
# #         f"预期状态码为 404，实际为{res.status_code}")
#
#
# @pytest.mark.parametrize("ID,expected_status",[
#     ("1",200),
#     ("2",200),
#     ("9999",404),
# ])
# def test_get_post_status(client,ID,expected_status):
#     res=client.get(f"/posts/{ID}")
#     assert res.status_code ==expected_status,(
#         f"预期状态码为{expected_status},实际为{res.status_code}"
#     )
# import pytest
# POST_CASES=[
#     (1,200),
#     (2,200),
#     (3,200),
#     (9999,404)
# ]
# @pytest.mark.parametrize("post_id,expected_status",POST_CASES)
# def test_get_posts_status(client,post_id,expected_status):
#     res=client.get(f"/posts/{post_id}")
#     assert res.status_code == expected_status,(
#         f"文章ID={post_id},预期状态码={expected_status},"
#         f"实际状态码={res.status_code}"
#     )


# def test_create_post(client):
#     payload ={
#         "title":"API test",
#         "body":"This is a test post",
#         "userId":1
#     }
#     print("开始发送 POST 请求")
#     res=client.post("/posts",payload)
#     print("收到响应：",res.status_code)
#     assert res.status_code ==201
#     data=res.json()
#     assert data["title"]=="API test"

# def test_update_post(client):
#     payload ={
#         "id":1,
#         "title":"Updated title",
#         "body":"Updated body",
#         "userId":1
#     }
#     res=client.put("/posts/1",payload)
#     assert res.status_code == 200
#     data=res.json()
#     assert data["title"]=="Updated title"


# def test_delete_post(client):
#     res=client.delete("/posts/1")
#     assert res.status_code ==200,(
#         f"预期状态码为：200,实际为：res.status_code"
#     )

# def test_update_post(client):
#     payload ={
#         "id":1,
#         "title":"Updated title",
#         "body":"Updated body",
#         "userId":1
#     }
#     res =client.put("/posts/1",payload)
#     assert res.status_code ==200,(
#         f"预期状态码 200，实际为{res.status_code}"
#     )
#     data=res.json()
#     assert data["title"] ==payload["title"]
#     assert data["body"]== payload["body"]

import pytest
@pytest.mark.parametrize("post_id,expected_status",[
    (1,200),
    (2,200),
    (3,200),
    (9999,404),
    (10000,404)
])
def test_post_status(client,post_id,expected_status):
    res=client.get(f"/posts/{post_id}")
    assert res.status_code ==expected_status,(
        f"文章ID={post_id},"
        f"预期状态码={expected_status},"
        f"实际状态码={res.status_code}"
    )