import paramiko
import os, sys, time

fortress_ip = '10.106.1.74'
fortress_user = 'cc'
fortress_password = 'hao119119'

hostname = '10.106.1.75'
username = 'cc'
password = 'hao119119'

tmp_dir = '/tmp'
remote_dir = '/home/cc'
local_path = '/home/cc/test.tar.gz'
tmp_path = tmp_dir+'/test.tar.gz'
remote_path = remote_dir+'/test.tar.gz'

port = 22
passinfo = '\'s password: '
paramiko.util.log_to_file('syslogin.log')

t = paramiko.Transport(fortress_ip, port)
t.connect(username=fortress_user, password=fortress_password)
sftp = paramiko.SFTPClient.from_transport(t)
sftp.put(local_path, tmp_path)
sftp.close()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=fortress_ip, username=fortress_user, password=fortress_password)

channel = ssh.invoke_shell()
channel.settimeout(10)

buff = ''
resp = ''

channel.send('scp '+tmp_path+' '+username+'@'+hostname+':'+remote_path+'\n')
while not buff.endswith(passinfo):
    try:
        resp = channel.recv(9999)
    except Exception as e:
        print 'error', type(e)
        channel.close()
        ssh.close()
        sys.exit()
    buff += resp
    if not buff.find('yes/no') == -1:
        channel.send('yes\n')
        buff = ''
channel.send(password+'\n')


buff = ''
while not buff.endswith('~$ '):
    resp = channel.recv(9999)
    if not resp.find(passinfo) == -1:
        print 'error info: Authentication failed'
        channel.close()
        ssh.close()
        sys.exit()
    buff += resp

print buff
channel.close()
ssh.close()


