"""
1.3.3 paramiko 测试sftp
"""

import paramiko

user = "python"
pw = "Huawei123#$"
ip = "192.168.182.128"


tran = paramiko.Transport(ip, 22)
tran.connect(username=user, password=pw)
sftp = paramiko.SFTPClient.from_transport(tran)
# local_path = r"C:\Users\dell\Documents\sftp_tmp"
local_path = r"./"
remote_path = "/vrpcfg.cfg"
sftp.get(remote_path, local_path)
# sftp.put(local_path, "trac_msi.og")
tran.close()