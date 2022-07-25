import paramiko
import time


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname='192.168.52.2', port=22, username='python', password='Origin@159357', look_for_keys=False)  # 使用私钥

cli = ssh.invoke_shell()  # 获取交互式shell
cli.send('screen-length 0 temporary\n')
cli.send('display cur\n')
time.sleep(3)

disp_cur = cli.recv(999999).decode()
# f = open('huawei_ce12800_conf.txt', 'w')
# f.write(disp_cur)
# f.close()
print(disp_cur)

ssh.close()
