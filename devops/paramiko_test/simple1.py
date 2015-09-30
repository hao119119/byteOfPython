import paramiko
import os

hostname = '10.106.1.74'
username = 'cc'
password = 'hao119119'
port = 22

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=hostname, username=username, password=password)
stdin, stout, sterr = ssh.exec_command('free -m')
print stout.read()
ssh.close()


try:
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)

    sftp.put('/home/cc/tmp.txt', '/home/cc/tmp_remote.txt')
    sftp.get('/home/cc/tmp_remote.txt', '/home/cc/tmp_local.txt')
    sftp.mkdir('/home/cc/test', 0755)
    sftp.rmdir('/home/cc/test')
    sftp.rename('/home/cc/tmp_remote.txt')
    print sftp.stat('/home/cc/tmp.txt')
    print sftp.listdir('home/cc/test')
    t.close()
except Exception as e:
    print type(e)


ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
private_key = os.path.expanduser('/home/key/id_rsa')
key = paramiko.RSAKey.from_private_key_file(private_key)

ssh.connect(hostname=hostname, username=username, pkey=key)
stdin, stdout, stderr = ssh.exec_command('free -m')
print stdout.read()
ssh.close()
