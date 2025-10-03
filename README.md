# ⚡ Simple Python Port Scanner 

A lightweight synchronous TCP port scanner implemented in Python.
Useful for quick service discovery on hosts you own or are authorized to test.

> **Warning:** Only scan systems you have explicit permission to test. Unauthorized scanning may be illegal.

## 🚀 Features

* Simple, easy-to-read synchronous scanner
* DNS resolution of target hostnames
* Validates port ranges and handles errors gracefully
* No external dependencies (uses Python standard library)

## 📦 Installation
Clone the repository and install dependencies:
```
git clone
cd port_scanner 
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## ▶️ Usage

```bash
python3 port_scanner.py TARGET START_PORT END_PORT
```

Example:

```bash
python3 port_scanner.py example.com 1 1024
```

## 📂 Output

The script prints progress and lists open ports when discovered. Example:

```
Scanning port 22...
[+] Port 22 is open
Scanning port 23...
...
Scan finished.
Open ports: [22, 80]
Time taken: 2.34 seconds
```

## 🛡 Legal & Ethical

This tool is provided for educational and authorized security testing only. Do **not** use it on systems you do not own or have explicit permission to test.

## ⚖️ License

MIT License — see `LICENSE` for details.
