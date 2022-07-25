
from netaddr import IPAddress
import pprint



if __name__ == '__main__':
    ip = IPAddress("192.168.1.1")
    print(type(ip), ip)
    print(ip)
    print("")

    # ipv6
    ipv6 = IPAddress("2001:0db8:3c4d:0015:0000:0000:1a2f:1a2b")
    print(ipv6)

    """
    多进制表示方法
    """
    ip1 = IPAddress("192.168.1.0")
    print(ip1)
    print(bin(ip)) # 使用内置函数转换
    print(ip.bin)  # 使用对象的属性
    print(int(ip)) # 转换为整数 3232235777

    """
    点分十进制表示
    """
    ip2 = IPAddress("192.168.1.12")
    print(ip2.bits())
    print(type(ip2.bits())) # str





