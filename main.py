import os
import subprocess

def is_root():
    return os.geteuid() == 0




if is_root() == True:
    temp = True
    while temp:
        ip_address = input("What is the IP Address:- ")
        domain_name = input("What is the Domain name:- ")
        print("*************************\n")
        print(f"{ip_address=}")
        print(f"{domain_name=}")
        check = input("Is this corrrect y/n:- ")
        if(check == 'y'):
            temp = False
        
    
    command = f"sudo echo '{ip_address} {domain_name}' >> /etc/hosts"
    print(command)
    os.system(command)


else:
    print("need root permissions")