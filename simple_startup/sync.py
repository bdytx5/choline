import socket
import time

def write_to_file(filename, data):
    with open(filename, 'a') as f:
        f.write(data + "\n")

def serve_file(filename, address, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((address, port))
    s.listen(1)
    
    print(f"Listening for connections on {address}:{port}")

    conn, addr = s.accept()
    print(f"Connection from {addr}")
    
    try:
        with open(filename, 'r') as f:
            while True:
                where = f.tell()
                line = f.readline()
                if not line:
                    time.sleep(1)
                    f.seek(where)
                else:
                    print(f"Sending data: {line.strip()}")
                    conn.sendall(line.encode('utf-8'))
    except KeyboardInterrupt:
        print("Stopping server.")
    finally:
        conn.close()

if __name__ == "__main__":
    filename = "log.txt"
    address = "localhost"
    port = 5000

    for i in range(10):
        write_to_file(filename, f"Log entry {i}")
        time.sleep(1)

    serve_file(filename, address, port)
