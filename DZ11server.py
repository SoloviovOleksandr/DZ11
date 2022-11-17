import socket

def server(ip, port):
    sock = socket.socket()
    sock.bind(("127.0.0.1", 8000))
    sock.listen()
    print("listening")

    client_sock, client_address = sock.accept()
    message_client = client_sock.recv(1024)
    format_msg_client = message_client.decode("UTF-8")
    result_list = format_msg_client.split()
    to_send = str(len(result_list))
    client_sock.send(to_send.encode())
    client_sock.close()
server("127.0.0.1", 8000)