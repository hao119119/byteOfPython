import paramiko
import os
import pexpect


def exe_cmd(cmd, hostname, port, username, password):
    paramiko.util.log_to_file('paramiko.log')
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.connect(hostname, port, username, password)
    stdin, stdout, sterr = s.exec_command(cmd)
    print stdout.read()
    s.close()


def get_file(remote_file, hostname, port, username, password):
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.get(remote_file, os.path.basename(remote_file))
    t.close()


# def put_file(local_file, remote_file):
#     t = paramiko.Transport((hostname, port))
#     t.connect(username=username, password=password)
#     sftp = paramiko.SFTPClient.from_transport(t)
#     sftp.put(local_file, remote_file)
#     t.close()


def gen_sshkey(child):
    if child is None:
        child = pexpect.spawn('ssh-keygen -t dsa')
    else:
        child.sendline('ssh-keygen -t dsa')
    try:
        child.expect('save the key')
        child.sendline('')
        i = child.expect(['passphrase', 'Overwrite (y/n)?'])
        if i == 0:
            print 'create new key'
            child.sendline('')
            child.expect('again:')
            child.sendline('')
        else:
            print 'override key'
            child.sendline('y')
            child.expect('no passphrase')
            child.sendline('')
            child.expect('again:')
            child.sendline('')
    except pexpect.EOF:
        print ""
        return


def get_properties(properties_file):
    try:
        pro_file = open(properties_file, 'r')
        properties = {}
        for line in pro_file:
            if line.startswith('#'):
                continue
            if line.find('=') > 0:
                strs = line.replace('\n', '').split('=')
                properties[strs[0].strip()] = strs[1].strip()
    except Exception, e:
        raise e
    else:
        pro_file.close()
        return properties


def hosts_gen_sshkey(hosts, user, password):
    for i in range(len(hosts)):
        hosts[i] = hosts[i].strip()
    for host in hosts:
        child = pexpect.spawn('ssh %s@%s' % (user, host))
        i = child.expect(['(yes/no)?', 'password:'])
        if i == 0:
            child.sendline('yes')
            child.expect('password:')
        child.sendline(password)
        child.expect('[$|#]')
        gen_sshkey(child)
        child.sendline('exit')
        child.close()


def get_auth_file(user):
    if user == 'root':
        prefix = '/root'
    else:
        prefix = '/home/' + user
    path = os.path.join(prefix, '.ssh/id_dsa.pub')
    return path


def get_host_auth_file(host, user, port, password):
    path = get_auth_file(user)
    get_file(path, host, port, user, password)
    base_name = os.path.basename(path)
    auth_file = open(base_name)
    lines = []
    for line in auth_file:
        lines.append(line)
    return lines


if __name__ == '__main__':
    # get properties
    properties = get_properties('test.properties')
    user = properties.get('username')
    password = properties.get('password')
    hosts = properties.get('hosts')
    hosts = hosts.split(',')
    # gen local ssh key
    gen_sshkey(None)
    # gen remote ssh key
    hosts_gen_sshkey(hosts, user, password)

    # get auth
    lines = []
    # get local auth
    local_path = get_auth_file(user)
    local_auth = open(local_path, 'r')
    for line in local_auth:
        lines.append(line)
    # get remote auth
    for host in hosts:
        auth_lines = get_host_auth_file(host, user, 22, password)
        lines.extend(auth_lines)
    print lines

