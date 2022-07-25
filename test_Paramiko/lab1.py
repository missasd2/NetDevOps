import paramiko
import time
R2_ip = "127.0.0.1:5001"
username = "root"
password = "123456"


def main():
    print("main function")
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=R2_ip, username=username, password=password)

    print("Sucessfully login to ", R2_ip)

    ssh_client.close()

if __name__ == '__main__':
    print()

    main()
