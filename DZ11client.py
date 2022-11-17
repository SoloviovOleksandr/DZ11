import socket

def client(message,ip,port):
    sock = socket.socket()
    sock.connect((ip, port))
    format_msg = message.encode()
    sock.send(format_msg)
    message_server = sock.recv(1024)
    print(message_server)
    sock.close()
    return message_server
message = "IM client"
message_t = "Hello Im student I want to drink"
client(message_t, "127.0.0.1", 8000)