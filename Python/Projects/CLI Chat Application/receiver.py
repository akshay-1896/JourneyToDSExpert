import socket
import os
import base64
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
    data = s.recvfrom(1000000)
    message = data[0]
    decoded_message = message.decode('ascii')

    ip_address = data[1][0]
    # print(f"IP Address: {ip_address} \n")
    print(f"IP Address: {ip_address} \n Message: {decoded_message}")
    # print(decoded_message[0])

    if decoded_message[0] == '1':
        inbox_folder_path = os.path.join(data_folder_path, 'Inbox Files')
        os.makedirs(inbox_folder_path, exist_ok=True)

        filename = ip_address + '.txt'
        file_path = os.path.join(inbox_folder_path, filename)
        print("Inbox Folder Created!!")

        decoded_msg_ls= decoded_message.split('|')
        original_msg = decoded_msg_ls[1]
        with open(file_path, 'a') as file:
            file.write(original_msg + '\n')

    elif decoded_message[0] == '2':
        text_folder_path = os.path.join(data_folder_path, 'Text Files')
        os.makedirs(text_folder_path, exist_ok=True)

        ls = decoded_message.split('/', maxsplit=2)
        # ls_filename = ls[1].split(' | ', maxsplit=1)
        filename = ls[1]
        file_path = os.path.join(text_folder_path, filename)
        print("Text File created!!")

        with open(file_path, 'a') as file:
            file.write(ls[2])
            
    elif decoded_message[0] == '3':
        pdf_folder_path = os.path.join(data_folder_path, 'PDF Files')
        os.makedirs(pdf_folder_path, exist_ok=True)
        splitted_data = decoded_message.split('/',maxsplit=2)
        
        filename = splitted_data[1]
        pdf_path = os.path.join(pdf_folder_path,filename)
        print("PDF file created!")

        with open(pdf_path,'ab') as file:
            file.write(splitted_data[2])
            
        remaining = True
        while remaining:
            received_data = s.recvfrom(2048)