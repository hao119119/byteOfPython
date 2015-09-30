import paramiko
import os, sys, time

fortress_ip = '10.106.1.74'
fortress_user = 'cc'
fortress_password = 'hao119119'

hostname = '10.106.1.75'
username = 'cc'
password = 'hao119119'

port = 22
passinfo = '\'s password: '

paramiko.util.log_to_file('syslogin.log')

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=fortress_ip, username=fortress_user, password=fortress_password)

channel = ssh.invoke_shell()
# channel.settimeout(10)

buff = ''
resp = ''
channel.send('ssh '+username+'@'+hostname+'\n')
while not buff.endswith(passinfo):
    try:
        resp = channel.recv(9999)
    except Exception as e:
        print 'error', type(e)
        channel.close()
        ssh.close()
        sys.exit()
    buff += resp
    print buff
    if not buff.find('yes/no') == -1:
        channel.send('yes\n')
        buff = ''
channel.send(password+'\n')

buff = ''
while not buff.endswith('~$ '):
    resp = channel.recv(9999)
    if not resp.find(passinfo) == -1:
        print 'Error info: Authentication failed.'
        channel.close()
        ssh.close()
        sys.exit()
    buff += resp

channel.send('ifconfig\n')
buff = ''
try:
    while buff.find('~$ ') == -1:
        resp = channel.recv(9999)
        buff += resp
except Exception as e:
    print 'error', type(e)

print buff
channel.close()
ssh.close()

