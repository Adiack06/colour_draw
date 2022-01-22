import socket, threading

connections = []
threads = []


def handle_client(conn): #runs when client connects
    global connections
    connections.append(conn)
    with conn: #conn is like the socket
        print(f"Connected to {addr}")
        while True: #closes if conn cant recive data e.g disconected
            data = conn.recv(1024)
            if not data: break #closes if no data
            for c in connections:
                if c is not conn:
                    c.sendall(data)
    connections.remove(conn)  #after conn closed it removes it from the connections list
HOST = ''
PORT = 6996
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(10)
    while True:
        conn, addr = s.accept()
        t = threading.Thread(target=handle_client, args=(conn,))
        t.start()
        threads.append(t)

for t in threads:
    t.join()