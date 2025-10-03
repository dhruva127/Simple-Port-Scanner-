'''
Simple Port Scanner 

Author: Dhruv Bhoir

License: MIT

Version: 1.0
'''

import socket, sys
import time
usage = "Python3 port_scanner.py TARGET START_PORT END_PORT"

print("*" * 20)
print("Python Port Scanner")
print("*" * 20)

target = sys.argv[1]
target = socket.gethostbyname(target) #DNS Resolve 
start_port = int(sys.argv[2])
end_port = int(sys.argv[3])
if not target or not str(start_port) or not end_port:
    print(usage)
    exit()

start_time = time.time()

for port in range(start_port, end_port + 1):
    print("Scanning For Port {}...".format(port))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    conn = s.connect_ex((target, port))
    if not conn:
        print("[+] Port {} is open ".format(port))


end_time = time.time()
print("Time taken: {}".format(end_time - start_time))


