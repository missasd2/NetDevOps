# ssh 连接 ensp中router
import paramiko
import time

username = "ssh001"
password = "ssh001"
ip = "192.168.182.233"

def ensp():
    # 创建SSH对象
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(hostname=ip, port=22, username=username, password=password,
                look_for_keys=False, allow_agent=False)
    # 执行命令
    print("进入网络设备", ip)

    command = ssh.invoke_shell() # 激活terminal

    command.send("dis ip int bri\n")
    command.send("quit")

    time.sleep(3)
    output = command.recv(65535)
    print(output.decode().strip())
    ssh.close()


def ensp1():
    ssh = paramiko.SSHClient()
    # 允许连接不在know_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(hostname="192.168.182.233",   username="ssh001",
                password="ssh001", look_for_keys=False, allow_agent=False)
    # ssh.connect(hostname="127.0.0.1", port=2000, username="ssh001", password="ssh001",  timeout=10, auth_timeout=5)
    command = ssh.invoke_shell()
    # 执行命令
    command.send("dis ip int bri\n")
    command.send("quit")
    # 获取命令结果

    time.sleep(2)
    output = command.recv(65535)

    print(output.decode("ascii"))
    # 关闭连接
    ssh.close()


# 基于基于用户名和密码的 transport 方式登录
def ensp2():
    trans = paramiko.Transport((ip, 22))
    # 建立连接
    trans.connect(username=username, password=password,)

    # 将sshclient的对象的transport指定为以上的trans
    ssh = paramiko.SSHClient()
    ssh._transport = trans
    # 执行命令，和传统方法一样
    stdin, stdout, stderr = ssh.exec_command('dis ip int bri')
    print(stdout.read().decode())

    # 关闭连接
    trans.close()


def ensp3():
    trans = paramiko.Transport(("104.225.157.227", 26357))
    # 建立连接
    trans.connect(username="root", password="asd159357")

    # 将sshclient的对象的transport指定为以上的trans
    ssh = paramiko.SSHClient()
    ssh._transport = trans
    # 执行命令，和传统方法一样
    stdin, stdout, stderr = ssh.exec_command('df -hl')
    print(stdout.read().decode())

    # 关闭连接
    trans.close()


if __name__ == '__main__':
    # ensp("dis ip int bri")
    ensp()
