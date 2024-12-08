import socket
import base64
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# ip_address = "192.168.24.13" # 127.0.0.1 (local host address) --> for self transfer of data
ip_address = "127.0.0.1" # (local host address) --> for self transfer of data
port_no = 2535
target_address = (ip_address,port_no)

# print("Hey I am receiving")
quiet = False
while not quiet:
    DATA_TYPE = """What do you want to send:
                    press (1) for message
                    press (2) for text file 
                    press (3) for pdf file: """
    send_data_code = int(input(DATA_TYPE))
    if send_data_code == 1:
        message = input("Enter your message: ")
        encrypted_message = message.encode('ascii') # encryption
        msg_label = '1' + 'MSG' + '|'
        encrypted_msg_label = msg_label.encode('ascii')
        encrypted_msg_data = encrypted_msg_label + encrypted_message
        s.sendto(encrypted_msg_data,target_address)
        print("Successfully sent message")
        # s.sendto()
        checkmark = input("Do you want to quit? ")
        if checkmark.lower() == "y":
            quiet = True
        else:
            pass
        
    elif send_data_code == 2:
        input_path = input("Enter the Path: ")
        with open(input_path,'r') as file:
            file_content = file.read()
            ls_path = input_path.rsplit('\\', maxsplit=1)
            encrypted_file_content = file_content.encode('ascii')
            file_label = '2/' + ls_path[1] + '/'
            encrypted_file_label = file_label.encode('ascii')
            file_data = encrypted_file_label + encrypted_file_content
            s.sendto(file_data,target_address)
            print("Successfully sent message")
            checkmark = input("Do you want to quit? ")
            if checkmark.lower() == "y":
                quiet = True
            else:
                pass
            
    elif send_data_code == 3:
        input_path = input("Enter the Path: ")
        with open(input_path,'rb') as pdf:
            pdf_content = pdf.read()
            ls_path = input_path.rsplit('\\',maxsplit=1)
            pdf_label = '3/' + ls_path[1] + '/'
            encrypted_pdf_label = pdf_label.encode('ascii')
            pdf_data = encrypted_pdf_label + pdf_content
            s.sendto(pdf_data,target_address)
            print("Successfully sent pdf")
            checkmark = input("Do you want to quit? ")
            if checkmark.lower() == 'y':
                quiet = True
            else:
                pass
        

            

            
        



















