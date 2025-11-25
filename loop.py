# coding=utf-8
# @Time : 2025/11/22 14:27
# @File : loop.py
# @Project : git-test-v0

# range()
for i in range(10):
    print(f"loop_{i}")


def split_line():
    print("\n")
    print("*" * 100)
    # print("\n")


split_line()

# list 数组
j = 0
for name in ['apple', 'python', 'java', 'php', 'redis', 'shell', 'mybatis', 'mybatis-plugin']:
    print(f"{j}){name}")
    j = j + 1
