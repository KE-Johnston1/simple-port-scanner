# simple-port-scanner
A basic Phython port scanner for cybersecurity practice
## Python Script

```python
import socket

target = input("Enter target IP address: ")
ports = [21, 22, 80, 443, 8080]

print(f"\nScanning {target}...\n")

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")
    s.close()
How to Run

Open PowerShell

Type: python port_scanner.py

When prompted, enter a target IP like 127.0.0.1 or scanme.nmap.org

You’ll see which ports are open or closed
