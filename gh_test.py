import requests
from utils import showIP


def github_test():
    print("Github test")
    showIP()
    xk = requests.get(url="http://xk.autoisp.shu.edu.cn/", timeout=30)
    print([u.url for u in xk.history] + [xk.url])
