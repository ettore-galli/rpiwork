import socket


def response_page():
    return """<html><body><h1>Hello, world!</h1></body></html>"""

def server_main(address='', port=80, listen=5):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((address, port))
    s.listen(listen)


    while True:
      conn, addr = s.accept()
      print('Got a connection from %s' % str(addr))
      request = conn.recv(1024)
      request = str(request)
      
      print('Content = %s' % request)
         
      response = response_page()
      
      conn.send('HTTP/1.1 200 OK\n')
      conn.send('Content-Type: text/html\n')
      conn.send('Connection: close\n\n')
      conn.sendall(response)
      conn.close()
