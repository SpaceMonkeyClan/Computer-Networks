## Homework No III - V 1.0.0 - Client Script
## Author: Dena, Rene
## Last Modified: 3/19/19

#________________________________________________________Script_________________________________________________________
print("\n\n")
import socket

def main():
    host = '64.183.98.170'
    port = 3800

    s = socket.socket()
    s.connect((host, port))

    data = s.recv(1024)
    print('Connecting to ' + host + ':' + str(port) + '...' + str(data) + '\n')
    s.send(b'version\n')
    data = s.recv(1024)
    s.close()

    print('Version info: ' + str(data))

if __name__ == '__main__':
    main()
