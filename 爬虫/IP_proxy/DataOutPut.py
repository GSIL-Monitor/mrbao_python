from http_proxy import proxy
import pymysql
ip_content=proxy(1)
for result in ip_content:
    print(result)
    print(result[1])