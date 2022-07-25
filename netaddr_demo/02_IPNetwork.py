from netaddr import IPNetwork
from netaddr.core import N,NOHOST


if __name__ == '__main__':
    # 1 掩码表达方式
    # 1.1 cidr的prefix方式
    ip_network = IPNetwork("192.168.1.1")
    print(ip_network) # 192.168.1.1/32
    print(ip_network.__repr__()) #  IPNetwork('192.168.1.1/32')

    # 1.2 netmask方式
    ip_network_1 = IPNetwork("192.168.1.1/255.255.255.0")
    print(ip_network_1) # 192.168.1.1/24
    print(repr(ip_network_1)) # IPNetwork('192.168.1.1/24')




    print(" ")

    # 1.3

    """
    IPNetwork('192.1.0.30/25')
    IPAddress('192.1.0.0')
    25 <class 'int'>
    IPAddress('255.255.255.128')
    """
    ip_network_2 = IPNetwork("192.1.0.30/25")
    print(repr(ip_network_2)) # IPNetwork('192.1.0.29/25')
    print(repr(ip_network_2.network)) # 网络位IPAddress('192.1.0.0'),返回类型是IPAddress
    print(repr(ip_network_2.prefixlen), type(ip_network_2.prefixlen)) # 25, int
    print(repr(ip_network_2.netmask)) # IPAddress('255.255.255.128')
    print("===========")

    """
    flags，意思是如何计算它的主机位，有一种方式是NOHOST，就是去除主机位
    192.1.0.0/25
    IPNetwork('192.1.0.0/25')
    IPAddress('192.1.0.0')
    25 <class 'int'>
    IPAddress('255.255.255.128')
    """
    ip_network_3 = IPNetwork("192.1.0.29/25", flags=N)
    print(ip_network_3)  # 192.1.0.29/25
    print(repr(ip_network_3))  # IPNetwork('192.1.0.29/25')
    print(repr(ip_network_3.network))  # 网络位IPAddress('192.1.0.0'),返回类型是IPAddress
    print(repr(ip_network_3.prefixlen), type(ip_network_3.prefixlen))  # 25, int
    print(repr(ip_network_3.netmask))  # IPAddress('255.255.255.128')

    # 判断IP地址或者网段之间的归属关系
    ip_n1 = IPNetwork("192.168.1.25") # 默认掩码 32
    ip_n2 = IPNetwork("192.168.1.0/25")

    if ip_n1 in ip_n2:  # ip_n1 归属 ip_n2
        print("ip_n1 归属 ip_n2")
    else:
        print("ip_n1 不归属 ip_n2")

    ip_n1 = IPNetwork("192.168.1.129")  # 默认掩码 32
    ip_n2 = IPNetwork("192.168.1.0/25")

    if ip_n1 in ip_n2:  # ip_n1 不归属 ip_n2
        print("ip_n1 归属 ip_n2")
    else:
        print("ip_n1 不归属 ip_n2")
