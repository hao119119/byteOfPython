from fabric.api import *
# fabric env attribute
# env.host = '10.106.1.74'
# env.hosts = ['10.106.1.74', '10.106.1.75']
# env.exclude_hosts
# env.user
# env.port   default port is 22
# env.password
# env.passwords = {
#       'root@10.106.1.74':'123456a?'
#       'cc@10.106.1.75':'123456a?'
#   }
# env.gateway gateway model, use it as fortress machine
# env.roledefs = {
#       'webservers': ['10.106.1.74', '10.106.1.75']
#       'dbservers': ['10.106.1.74', '10.106.1.75']
#   }

# fabric api list
# local: local('uname -s') exec cmd in local
# lcd: lcd('/home') change local pwd
# cd: cd('/data/log') change remote pwd
# run: run('free -m) exec cmd in remote
# sudo: sudo('/etc/init.d/httpd start) exec cmd in remote as sudo
# put: put('/home/user.info', '/data/user.info) upload local file to remote server
# get: get('/data/user.info', '/home/user.info) download from remote server to local
# prompt: prompt('please input user password:') get user input
# confirm: confirm('Tests failed. Continue[Y/N]?') get confirm info
# reboot: reboot()
# @task: mark the function can be exec by fab
# @run_once mark the function only be exec once, not be effected by multi-hosts

env.user = 'cc'
env.hosts = ['10.106.1.74', '10.106.1.75']
env.password = 'hao119119'


@runs_once
def local_task():
    local('uname -a')


def remote_task():
    with cd('/home/cc'):
        run("ls -l")

