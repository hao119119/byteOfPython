import os
import sys

import gen_ssh_key

if __name__ == '__main__':
    cmd_length = len(sys.argv)
    if cmd_length == 1:
        cmd = 'start'
    else:
        cmd = sys.argv[1]
    properties = gen_ssh_key.get_properties('./test.properties')
    zookeeper_path = properties.get('zookeeper_path')
    zkSever = os.path.join(zookeeper_path, 'bin/zkServer.sh')
    hosts = properties.get('hosts')
    hosts = hosts.split(',')
    zkServer_cmd = ' '.join([zkSever, cmd])
    user = properties.get('username')
    password = properties.get('password')
    os.system(zkServer_cmd)
    for host in hosts:
        gen_ssh_key.exe_cmd(zkServer_cmd, host, 22, user, password)
