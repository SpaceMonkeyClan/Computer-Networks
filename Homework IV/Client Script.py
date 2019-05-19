## Homework No V - V 1.0.0 - Client Script
## Author: Dena, Rene
## Last Modified: 5/11/19

#________________________________________________________Script_________________________________________________________
print("\n\n")
import socket

def main():
    #Port and host variables
    host = '64.183.98.170'
    port = 3800

    #Use of socket function
    s = socket.socket()
    s.connect((host, port))

    #Connection verification
    print('Connecting to ' + host + '     Port: ' + str(port))

    #Severs initial start prompts
    data = s.recv(1024)
    print('\nCharPrompt: ' + str(data))
    data = s.recv(1024)
    print('\nCharSelect: ' + str(data))

    character = input('\nSelect your character: ')
    s.send(character)

    #Array storage later used for game board display
    bl = []

    i = 1
    while i <= 4:

        #Send the clients move and stores move in array
        move = int(input('\nYour Move: '))
        bl.insert(move-1, character)
        s.send(move)

        #Recives servers move and stores in array
        data = s.recv(1024)
        bl.insert(data-1, serverCharacter)
        print('\nClientMove: ' + str(data))

        i += 1

    # Send the clients move and stores move in array
    move = int(input('\nYour Move: '))
    bl.insert(move - 1, character)
    s.send(move)

    #Prints final results and disconnection verification
    data = s.recv(1024)
    print('\nWinner: ' + str(data))
    data = s.recv(1024)
    print('\nHost: ' + str(data))

    #Game Board Layout
    print('\n')
    print(bl[0] + '|' + bl[1] + '|' + bl[2])
    print('_+_+_')
    print(bl[3] + '|' + bl[4] + '|' + bl[5])
    print('_+_+_')
    print(bl[6] + '|' + bl[7] + '|' + bl[8])
    print('\n')

    #Closes connection to host
    s.close()

if __name__ == '__main__':
    main()
