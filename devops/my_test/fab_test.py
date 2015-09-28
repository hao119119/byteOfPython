from fabric.api import *

env.user = 'cc'
env.hosts = ['10.106.1.74', '10.106.1.75']
env.password = 'hao119119'


def remote_task():
    with cd('/home/cc'):
        run("ls -l")

remote_task()