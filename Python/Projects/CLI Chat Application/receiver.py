import socket
import os
# UDP --> User Datagram Protocol
# DGRAM = DataGram , SOCK_DGRAM -> UDP Protocol
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # SOCK_STREAM-> TCP Protocol

# ip_address = "192.168.01.80" # private address of the system
ip_address = "127.0.0.1"
port_no = 2535  # address of the application

complete_address = (ip_address, port_no)
s.bind(complete_address)

print("Hey! I am receiving messages")
os.makedirs('media', exist_ok=True)
current_working_dir_path = os.getcwd()
data_folder_path = os.path.join(current_working_dir_path, 'media')
# print(data_folder_path)

while True:  # infinite loop for continuous data receiving
    data = s.recvfrom(500)
    message = data[0]
    decoded_message = message.decode('ascii')

    ip_address = data[1][0]
    # print(f"IP Address: {ip_address} \n")
    print(f"IP Address: {ip_address} \n Message: {decoded_message}")
    # print(decoded_message[0])

    if decoded_message[0] == '0':
        inbox_folder_path = os.path.join(data_folder_path, 'Inbox Files')
        os.makedirs(inbox_folder_path, exist_ok=True)

        filename = ip_address + '.txt'
        file_path = os.path.join(inbox_folder_path, filename)
        print("Inbox Folder Created!!")

        with open(file_path, 'a') as file:
            file.write(decoded_message + '\n')

    elif decoded_message[0] == '1':
        text_folder_path = os.path.join(data_folder_path, 'Text Files')
        os.makedirs(text_folder_path, exist_ok=True)
        # print("Text Folder created!!")

        ls = decoded_message.split(' ', maxsplit=1)
        ls_filename = ls[1].split(' | ', maxsplit=1)
        filename = ls_filename[0]
        file_path = os.path.join(text_folder_path, filename)

        with open(file_path, 'a') as file:
            file.write(ls_filename[1])