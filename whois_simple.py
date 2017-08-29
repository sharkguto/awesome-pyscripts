import socket
import re


def check_domain(domain, whoisserver="whois.iana.org"):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((whoisserver, 43))

    s.send((domain + "\r\n").encode())
    response = b""
    while True:
        data = s.recv(4096)
        response += data
        if not data:
            break
    s.close()
    del(s)

    refer_whois = re.findall(r'^refer\:\s+(.*)',response.decode(),re.MULTILINE)
    if refer_whois:
        return check_domain(domain, refer_whois[0])
    else:
        return response.decode()

print(check_domain("google.com"))
