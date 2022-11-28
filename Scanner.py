from re import L
import socket
import threading,pyttsx3
import sys
import time
import pandas as pd
csv = pd.read_csv("nmap-services.csv")

if sys.argv[1] == "-h":
    print("python <ip> or <dns>")
    sys.exit()
try:
    IP = socket.gethostbyname(sys.argv[1])
    
except socket.gaierror:
    print("Somethong wrong!")
    sys.exit()
lis=[]
def scan(port):
    time.sleep(1)
    s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    send = s.connect_ex((IP, port))
    if (not send):
        l = []
        for i in csv["port"]:
            l.append(i)
        for i in l:
            if port == i and port in l:
                try:
                    print(csv["port"][i],csv["protocol"][i],csv["description"][i])
                    lis.append([csv["port"][i],csv["description"][i]])
                except Exception:
                    print(port,"something wrong")
            else:
                pass
        if port not in l:
            print(f"unknown port {port}")
            lis.append([port,'unknown'])
        #print("=======================================================================================================")
        #print()
        #print("=======================================================================================================")
        
        
    s.close()

for i in range (1,65535):
    th = threading.Thread(target=scan, args=(i,)).start()
#print(lis)
for j in lis:
    speak(f"port no {j[0]} {j[1]} is open")
sys.exit()
