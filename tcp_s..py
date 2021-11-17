import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sockettt:
    sockettt.bind(('0.0.0.0',50007))
    sockettt.listen(1)
    while True:
        connection, from_adder = sockettt.accept()
        with connection:
            while True:
                Receive_Data = connection.recv(1024)
                if not Receive_Data:
                    break
                print(' data : {}, addr: {}'.format(Receive_Data,from_adder))
                #connection.sendall(b'received')
