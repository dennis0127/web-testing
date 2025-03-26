#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess


def commit(msg: str):
    subprocess.run(["git", "add", "."], cwd=r"D:\workspace\python\web-testing")
    subprocess.run(["git", "commit", "-m", msg], cwd=r"D:\workspace\python\web-testing")
    subprocess.run(["git", "push"], cwd=r"D:\workspace\python\web-testing")


if __name__ == "__main__":
    msg = input("请输入提交信息:")
    commit(msg)
