# coding=utf-8
# @Time : 2025/11/22 14:37
# @File : user.py
# @Project : git-test-v0

class User:
    def __init__(self):
        self.uid = '10010'
        self.name = 'Hason'

    def _printInfo(self):
        print(f"[ INFO ] uid: {self.uid}\n\t\tname: {self.name}")

    def run(self):
        # print
        self._printInfo()


if __name__ == '__main__':
    app = User()
    app.run()
