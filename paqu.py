# coding=utf-8
import requests
import re
import time


def get_html(n, doma):
    if doma == "欧美":
        region = "oumei"
    elif doma == "日韩":
        region = "rihan"
    elif doma == "国内":
        region = "china"
    if n == 1:
        n = ''
    else:
        n = '_' + str(n)
    url = "http://www.dygod.net/html/gndy/" + region + "/index" + n + ".html"
    return requests.get(url).content.decode("GBK")


def content_parse(content):
    re_str = "ulink[\s\S]*?title=\"[\s\S]*?\">([\s\S]*?)</a>[\s\S]*?点击：([\s\S]*?)<"
    result = re.findall(re_str, content)
    return result


def get_pair_html(n, region):
    result = []
    while not result:
        c = get_html(n, region)
        result = content_parse(c)
        if len(result) == 0:
            print("list is empty, reget")
            time.sleep(10)
        else:
            break
    print("Success " + str(n))
    return result


def write_list(l):
    f = open("dygod.csv", "a+")
    for i in l:
        f.write(i[0] + "," + i[1] + '\n')
    f.close()

# --test


region = raw_input("select region:")
n = raw_input("max_page_num = ")
for i in range(1, int(n)):
    try:
        l = get_pair_html(i, region)
        write_list(l)
    except:
        print("fail")
        pass
