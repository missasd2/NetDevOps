from netmiko import ConnectHandler,NetmikoTimeoutException,NetmikoAuthenticationException #引入netmiko连接模块、报错模块
import netmiko
import getpass #引入密码模块
import time #引入时间模块
date = time.strftime('%Y%m%d', time.localtime()) #赋予date变量
password = getpass.getpass('Password:') #赋予password变量


ip = '192.168.182.233'


with netmiko.ConnectHandler(device_type='huawei', ip=ip, username='ssh001', password='ssh001') as connect:
    print('已经成功登录： 192.168.182.233 '  + '\n')
    output = connect.send_command('display cpu-usage')
    print()
print(output)

