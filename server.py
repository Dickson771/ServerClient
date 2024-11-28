import socket

def receive_and_save_file(server_ip, server_port, save_path):
    #initialize a socket and bind to the ip and port 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))

   
    server_socket.listen(1)
    print("Server is listening for incoming connections...")

    # Accept a new connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    # Open the file to save the received data
    with open(save_path, 'wb') as file:
        print(f"Receiving file and saving it as {save_path}")
        file_data = client_socket.recv(1024)  # Receive data in chunks
        while file_data:
            file.write(file_data)
            file_data = client_socket.recv(1024)

    print(f"File received and saved successfully as {save_path}")
    
    # Close the client connection
    client_socket.close()

    # Read the file contents
    with open(save_path, 'r') as file:
        file_contents = file.read()
        print("Contents of the received file:")
        print(file_contents)

if __name__ == "__main__":
   
    server_ip = '127.0.0.1'  # Server IP address
    server_port = 12345      # Server Port

  
    save_path = 'risivd.txt'  #file contents are saved here once they are received
    
    receive_and_save_file(server_ip, server_port, save_path)
