"""
模型文件放置位置：
    .pb   --> graph/
    .yaml --> model/

启动识别程序：
    python flask_server.py

启动测试脚本：
    运行此脚本
"""

import glob
import json
import base64
import requests


c = f = 0
for filename in glob.glob('./h_val/*.jpg'):  # 测试集
    fp = open(filename, "rb")  # 以二进制读取图片
    base64data = base64.b64encode(fp.read())  # 得到 byte 编码的数据
    base64data = str(base64data, 'utf-8')  # 重新编码数据
    res = requests.post('http://localhost:19951/captcha/v1', json={"image": base64data})

    ans = json.loads(res.text)['message']
    a = filename.split('/')[-1][:-4].lower()

    if a == ans:
        c += 1
        print(f"√ {a}, 识别: {ans}")
    else:
        print(f"× {a}, 识别: {ans}")
        f += 1
print(f"正确：{c}，错误：{f}")
print("识别率：", (c/float(c+f))*100, "%")
