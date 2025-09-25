import socket
import threading
import logging

logging.basicConfig(filename='honeypot_logs.txt', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

def start_honeypot(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', port))
    s.listen(5)
    logging.info(f"Honeypot listening on port {port}")
    while True:
        conn, addr = s.accept()
        logging.info(f"Connection from {addr} on port {port}")
        conn.send(b"Welcome to a fake service!\n")
        conn.close()

ports = [21, 22, 23, 80, 443]
for port in ports:
    thread = threading.Thread(target=start_honeypot, args=(port,))
    thread.start()
