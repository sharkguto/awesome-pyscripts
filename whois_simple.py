import sys
import socket
import re

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("whois.iana.org", 43))

#convert string to bytes, socket need bytes

domain_check = "sbt.show" #sys.argv[1]

s.send(( domain_check + "\r\n").encode())

#declares a bytes
response = b""
while True:
    data = s.recv(4096)
    response += data
    if not data:
        break
s.close()

del(s)

#convert bytes to string
text_parse = response.decode()

# parse refer whois server
refer_whois = re.findall(r'^refer\:\s+(.*)',text_parse,re.MULTILINE)

print(refer_whois)

for i in refer_whois:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((i, 43))
    s.send(( domain_check + "\r\n").encode())
    #declares a bytes
    response = b""
    while True:
        data = s.recv(1024)
        response += data
        if not data:
            break
    s.close()
    text_zum = response.decode()
    print(text_zum)

