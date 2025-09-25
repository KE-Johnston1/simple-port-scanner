# Honeypot Project

This Python honeypot listens on common ports and logs connection attempts. It simulates vulnerable services to help practice threat detection and incident response.

## Features
- Monitors ports: 21, 22, 23, 80, 443
- Logs IP addresses and timestamps
- Sends fake service banner to simulate interaction

## How to Run
```bash
python honeypot.py
2025-09-25 17:06:03 - Connection from ('192.168.1.10', 54321) on port 22
## Purpose
This honeypot simulates vulnerable services to attract and log unauthorized access attempts. It's designed for learning threat detection, incident response, and log analysis.

## Features
- Listens on common ports (21, 22, 23, 80, 443)
- Logs IP addresses and timestamps
- Sends fake service banner to simulate interaction
- Easy to run and test with a port scanner

## How to Test
Use the `port_scanner.py` script in the main repo to scan the honeypot ports. This will trigger log entries in `honeypot_logs.txt`.

## Ethical Use
This honeypot is for educational and testing purposes only. Do not deploy it on public-facing systems without proper authorization.
## Sample Incident Summary

On 2025-09-25 at 17:06, a connection was logged from IP 192.168.1.10 on port 22. The honeypot responded with a fake SSH banner. No further interaction occurred. This suggests a basic scan or probing attempt. No escalation or payload delivery was detected.
