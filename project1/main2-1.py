# 외부 및 내부 ip 확인
import re
import requests
import socket

in_addr = socket.gethostbyname(socket.gethostname())
# print(in_addr)

#in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#in_addr.connect(("www.google.co.kr", 433))
# print(in_addr.getsockname()[0])


req = requests.get("http://ipconfig.kr")
out_addr = re.search(
    r' IP Address: (\d{1, 3}\. \d{1, 3}\. \d{1, 3}\. \d{1, 3})', req.text)[1]
print(out_addr)
