#  Simple Port Scanner

This repository contains hands-on cybersecurity tools for learning network scanning and threat detection. It includes a Python-based port scanner and a honeypot simulation for logging unauthorized access attempts.

A basic Python port scanner built for hands-on cybersecurity practice. This tool scans common ports on a target IP address and logs the results to a timestamped file.

##  Features

- Scans ports: 21, 22, 80, 443, 8080  
- Logs results to `scan_results.txt`  
- Includes timestamp for each scan  
- Displays open/closed ports in terminal and log file

##  Requirements

- Python 3.x  
- Internet connection (for scanning external IPs)

##  How to Run

1. Clone or download the repository  
2. Open `port_scanner.py` in your Python environment or Codespaces  
3. Run the script:python port_scanner.py
4. Enter a target IP address (e.g. `scanme.nmap.org`)  
5. View results in the terminal and in `scan_results.txt`

##  Example Output (scan_results.txt)
Scan started at 2025-09-25 14:12:03 Scanning scanme.nmap.org...

Port 21 is CLOSED Port 22 is OPEN Port 80 is OPEN Port 443 is CLOSED Port 8080 is CLOSED

##  About This Project

This project was built as part of my transition into cybersecurity. It demonstrates practical skills in socket programming, logging, and GitHub workflow management. I used Codespaces to build and test the tool, and documented the process for portfolio visibility.
## Related Projects

- [Honeypot Simulation](honeypot/README.md): A Python honeypot that logs unauthorized access attempts for threat detection practice.


## Skills Demonstrated

- Python scripting for network tools
- Logging and incident documentation
- Threat detection fundamentals
- Ethical cybersecurity practices




