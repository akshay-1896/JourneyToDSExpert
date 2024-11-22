import socket
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
                    press (2) for text file: """
    send_data_code = int(input(DATA_TYPE))
    if send_data_code == 1:
        message = input("Enter your message: ")
        encrypted_message = message.encode('ascii') # encryption
        s.sendto(encrypted_message,target_address)
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
            encrypted_file_content = file_content.encode('ascii')
            s.sendto(encrypted_file_content,target_address)
            print("Successfully sent message")
            checkmark = input("Do you want to quit? ")
            if checkmark.lower() == "y":
                quiet = True
            else:
                pass

            

            
        



















