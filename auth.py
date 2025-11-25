# coding=utf-8
# @Time : 2025/11/25 02:03
# @File : auth.py
# @Project : git-test-v1

class AuthLogin:
    def __init__(self):
        print("login auth control.")

    def login(self, username, password):
        """

        :param username:
        :param password:
        :return:
        """

        # TODO 1. 根据用户名查询用户信息
        # TODO 2. 判断用户是否存在
        # TODO 2.1 不存在,则直接返回空集合

        # TODO 3. 比对数据库密码和前端传入的密码是否一致

        # TODO 3.1 密码错误,则直接返回非法用户

        # TODO 4. 密码正确,生成 jwt token

        # TODO 5. 封装返回结果 { uid: xxx ,token: xxx-xxx-xxx,requestId: '1A0U78XceK' }
        return True
