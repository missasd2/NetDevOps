"""
配置备份范例
"""
import time
from netmiko import ConnectHandler
import logging
import pandas as pd

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

def get_batch_backup_dev_infos(filename="inventory.xlsx"):
    '''
        读取Excel表格加载网络设备基本信息和其配置备份的命令，结果返回一个元组的列表
        :param filename: 表格名称，默认值是inventory.xlsx
        :return: [(<netmiko连接设备所需基本信息的字典>,<配置备份的命令>)]
        示例：
        [({'host': '192.168.137.201',
           'device_type': 'huawei',
           'username': 'netdevops',
           'password': 'Admin123~',
           'secret': nan,
           'timeout': 180,
           'conn_timeout': 20},
           'display current-configuration'),
        ]
        '''
    with pd.read_excel(filename) as df:
        items = df.to_dict(orient="records")
        # 构建返回的结果,dev_infos是一个元组的列表
        dev_infos = []
        for i in items:
            backup_cmd = i["backup_cmd"]
            del i["backup_cmd"]
            dev = i
            dev_infos.append((dev, backup_cmd))
        return dev_infos




# 备份单个设备配置
def network_device_backup(dev:dict, cmd:str=None):
    with ConnectHandler(**dev) as conn:
        output = conn.send_command(command_string="dis cur configuration")
        filename = "%s-%s.txt" % (dev["host"], time.strftime("%Y-%m-%d", time.localtime()))
        with open(filename, "w", encoding="utf8") as txt:
            txt.write(output)
            print('{}执行备份成功'.format(huawei['host']))


if __name__ == '__main__':
    print(get_batch_backup_dev_infos())