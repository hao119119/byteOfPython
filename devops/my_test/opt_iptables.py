import sys
import os

import gen_ssh_key

if __name__ == '__main__':
    cmd_length = len(sys.argv)
    if cmd_length == 1:
        cmd = 'start'
    else:
        cmd = sys.argv[1]
    properties = gen_ssh_key.get_properties('./test.properties')
    hosts = properties.get('hosts')
    hosts = hosts.split(',')
    iptalbe_cmd = ' '.join(['service iptables ', cmd])
    user = properties.get('username')
    password = properties.get('password')
    os.system(iptalbe_cmd)
    for host in hosts:
        gen_ssh_key.exe_cmd(iptalbe_cmd, host, 22, user, password)
