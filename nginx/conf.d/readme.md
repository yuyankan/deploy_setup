#  fast api 外部访问：
# IP: 8010(ngnix port)/korean_api/images/xxxxxx
 : ip transfer:
 1. input: IP: 8010(ngnix port)/korean_api/images/xxxxxx-->server1: recevied by nginx: 
 2. nginx规则匹配：/korean_api/images/xxxxxx: --> /korean_api/
 3. 代理到 http://fasapi-service: 8000/images/xxxxxx
    :note： 8000后的反斜杠： 有即带着匹配规则字符korean_api， 没有就不带
