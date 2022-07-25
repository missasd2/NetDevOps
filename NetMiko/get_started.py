from netmiko import ConnectHandler
import logging

# 开启日志
logging.basicConfig(filename="netmiko.log", level=logging.DEBUG)
# 获取一个名为netmiko的Logger对象，一般名称对应模块名、文件名
Logger = logging.getLogger("netmiko")

huawei = {
    "device_type": "huawei",
    "host": "192.168.56.100",
    "username": "python",
    "password": "Huawei12#$",
    "port": 22,

}

# 创建长连接对象
net_connect = ConnectHandler(**huawei)


output = net_connect.send_command("dis ip int bri")
print(output)

# 执行配置修改命令
config_commands = [
                   "int g1/0/0",
                   "description to cloud g0/0/1",
                   "quit",
                   "commit",
                   ]
output1 = net_connect.send_config_set(config_commands=config_commands)
print(output1)


# 断开连接
net_connect.disconnect()

