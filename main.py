try:
    import usocket as socket
except:
    import socket

response_404 = """HTTP/1.1 404 NOT FOUND
<h1>404 Not Found :(</h1>
"""

response_500 = """HTTP/1.1 500 INTERNAL SERVER ERROR
<h1>500 Internal Server Error :O</h1>
"""

response_template = """HTTP/1.1 200 OK

%s
"""

import machine
import ntptime, utime
from machine import RTC

seconds = ntptime.time()
rtc = RTC()
rtc.datetime(utime.localtime(seconds))

outlet = machine.Pin(16, machine.Pin.OUT)
def set_outlet(post):
    # Change outlet's value based on input from site
    if 'on' in post:
        outlet.on()
    elif 'off' in post:
        outlet.off()
        
    body = """<html>
    <body>
    <h2>Smart Outlet Switch</h2>
    <h3>Currently: {}</h3>
    <form action="" method="POST">
    <button name="on" value="on">Turn on!</button><br>
    </form>
    <form action="" method="POST">
    <button name="off" value="off">Turn off</button>
    </form>
    </body>
    </html>
    """.format(outlet.value())
    
    return response_template % body



func_pins = {
    'outlet': 16,
}

handlers = {
    '': set_outlet,
    'time': time,
    'set_outlet': set_outlet,
}

def main():
    s = socket.socket()
    s_addr_info = socket.getaddrinfo("0.0.0.0", 8080)
    addr = s_addr_info[0][-1]
    
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    s.bind(addr)
    s.listen(5)
    
    print("make sure the functions are connected to the correct pins")
    for func, pin in func_pins.items():
        print(func + ": " + str(pin))

    print("Listening, connect your browser to http://<this_host>:8080/")
    
    while True:
        res = s.accept()
        client_s = res[0]
        client_addr = res[1]
        req = client_s.recv(4096)
        print("Request:")
        print(req)
        
        # The first line of a request looks like "GET /arbitrary/path/ HTTP/1.1".
        # This grabs that first line and whittles it down to just
        # "/arbitrary/path/"
        path = req.decode().split("\r\n")[0].split(" ")[1]
        print(path)
        req = req.decode().split("\r\n")
        print(req)
        # Given the path, identify the correct handler to use
        try:
            handler = handlers[path.strip('/').split('/')[0]]
            response = handler(req[-1])
        except KeyError:
            response = response_404
        except Exception as e:
            response = response_500
            print(e)
        
        # A handler returns an entire response in the form of a multi-line string.
        # This breaks up the response into single strings, byte-encodes them, and
        # joins them back together with b"\r\n". Then it sends that to the client.
        client_s.send(b"\r\n".join([line.encode() for line in response.split("\n")]))

        client_s.close()
        print()
        
main()
