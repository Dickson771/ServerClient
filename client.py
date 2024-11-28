import socket
import tkinter as tk
from tkinter import messagebox

class FileTransferClient:
    def __init__(self, root):
        self.root = root
        self.root.title("File Transfer Client")

        # MY UI components
        self.label_filename = tk.Label(root, text="Enter filename (with .txt extension):")
        self.label_filename.pack(pady=10)

        self.entry_filename = tk.Entry(root, width=40)
        self.entry_filename.pack(pady=10)

        self.label_content = tk.Label(root, text="Enter the content of the file:")
        self.label_content.pack(pady=10)

        self.text_content = tk.Text(root, height=10, width=40)
        self.text_content.pack(pady=10)

        self.send_button = tk.Button(root, text="Send File", command=self.send_file)
        self.send_button.pack(pady=20)

    def send_file(self):
        # Get filename and content from the UI
        file_name = self.entry_filename.get()
        content = self.text_content.get("1.0", tk.END).strip()

        if not file_name or not content:
            messagebox.showerror("Error", "Both filename and content are required.")
            return

        # Create the file and write content
        try:
            with open(file_name, 'w') as file:
                file.write(content)

            messagebox.showinfo("Success", f"File '{file_name}' created and written to successfully.")

            # Send the file to the server
            server_ip = '127.0.0.1'
            server_port = 12345
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((server_ip, server_port))

            # Open the file in binary mode and send it
            with open(file_name, 'rb') as file:
                file_data = file.read()
                client_socket.sendall(file_data)

            messagebox.showinfo("Success", "File sent successfully to the server.")
            client_socket.close()

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    # start the main window
    root = tk.Tk()
    # Initialize the client
    app = FileTransferClient(root)
    # execute the Tkinter event loop
    root.mainloop()
